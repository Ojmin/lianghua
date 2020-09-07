import json
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Spider(object):
    """基类"""

    def __init__(self):
        self.options = Options()
        # self.options.add_argument('--headless')
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--hide-scrollbars")
        self.options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        self.driver = webdriver.Chrome(options=self.options,
                                       executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()

    def set_options(self, *args):
        for arg in args:
            self.options.add_argument(arg)

    def get_result(self):
        pass


class YangQiIndexSpider(Spider):
    """央企创新指数爬虫"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super(YangQiIndexSpider, self).__init__()
        self.driver.get("https://xueqiu.com/S/CSI000861")

    def get_increase(self):
        """获取中证央企创新驱动指数000861的涨跌幅"""
        point, increase = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[2]').text.split(" ")
        return float(increase.strip('%')) / 100


class YangQiETFSpider(Spider):
    """央企创新ETF爬虫"""

    def __init__(self, code):
        super(YangQiETFSpider, self).__init__()
        self.code = code
        self.driver.get("https://xueqiu.com/S/{}".format(self.code))

    def get_result(self, ):
        try:
            yesterday_value = float(self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/table/tbody/tr[3]/td[3]/span').text)  # 昨日净值

        except Exception as e:
            print("获取净值失败", e)
            return 0.00
        return yesterday_value


class HS300IndexSpider(Spider):
    """获取沪深300指数"""

    def __init__(self):
        super(HS300IndexSpider, self).__init__()
        self.driver.get("https://xueqiu.com/S/SH000300")

    def get_result(self):
        try:
            hs300_index = float(self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong').text)
        except:
            time.sleep(1)
            hs300_index = float(self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong').text)
            print("抓取错误")
        return hs300_index


class IFSpider(Spider):
    """IF当月连续爬虫"""

    def __init__(self):
        super(IFSpider, self).__init__()
        self.driver.get("http://quote.eastmoney.com/gzqh/ifdylx.html")

    def get_result(self):
        try:
            if_index = float(self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/p[1]/i[1]").text)
        except Exception as e:
            print("获取当月连续指数失败", e)
            return 0
        print("if_index", if_index)
        return if_index


class HS300IOPV(Spider):
    def __init__(self, code):
        super(HS300IOPV, self).__init__()
        self.code = code
        self.driver.get("https://xueqiu.com/S/{}".format(self.code))

    def get_result(self):
        try:
            current_value = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong').text.replace("¥", "")
            premium_rate = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/table/tbody/tr[4]/td[2]/span').text
        except:
            print("获取300ETF错误", self.code)
            time.sleep(1)
            current_value = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong').text.replace("¥", "")
            premium_rate = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/table/tbody/tr[4]/td[2]/span').text
        premium_rate = float(premium_rate.strip('%')) / 100
        IOPV = float(current_value) / (1 + premium_rate)
        return IOPV


class HS300ETF(object):
    """获取沪深300ETF的卖1买1成交量"""

    def __init__(self, code1, code2, code3, code4, code5, code6):
        self.code1 = code1
        self.code2 = code2
        self.code3 = code3
        self.code4 = code4
        self.code5 = code5
        self.code6 = code6

        self.headers = {
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        }

    def get_result(self):
        info_1, info_2, info_3, info_4, info_5, info_6, _ = requests.get(
            "http://hq.sinajs.cn/?format=json&list={0},{1},{2},{3},{4},{5}".format(self.code1, self.code2, self.code3,
                                                                                   self.code4, self.code5, self.code6),
            headers=self.headers).text.split(";")
        info_list = []
        for i in (info_1, info_2, info_3, info_4, info_5, info_6):
            info = i.split(",")
            info_list.append(
                {"name": info[0], "current_price": info[3], "buy1": info[11], "buy1_num": info[10], "sell1": info[21],
                 "sell1_num": info[20], "volume": info[8]})
        return info_list


class Germany30SPIFSpider(Spider):
    def __init__(self):
        super(Germany30SPIFSpider, self).__init__()
        self.driver.get("https://cn.investing.com/indices/germany-30-futures")

    def get_result(self):
        germany30_spif = float(self.driver.find_element_by_xpath('//*[@id="last_last"]').text.replace(",", ""))
        return germany30_spif

    def get_result2(self):
        increase = self.driver.find_element_by_xpath(
            '//*[@id="quotes_summary_current_data"]/div[1]/div[2]/div[1]/span[4]').text
        return float(increase.strip("%")) / 100


class Germany30ETFSpider(Spider):
    def __init__(self):
        super().__init__()
        self.driver.get("https://xueqiu.com/S/SH513030")

    def get_result(self):
        germany30_etf = float(self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong').text.replace("¥", ""))
        return germany30_etf


class TencentSpider(Spider):
    def __init__(self):
        super().__init__()
        self.driver.get("https://xueqiu.com/S/00700")
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/a').click()

    def get_result(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div/div[3]/i').click()
        time.sleep(0.2)
        try:
            price = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong').text.replace("HK$", "")
            change = \
                self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[2]').text.split(
                    " ")[
                    1]
            change = float(change.strip("%")) / 100

        except:
            return (1, "0")
        return (float(price), change)


class XGHLSpider(Spider):
    def __init__(self):
        super().__init__()
        self.driver.get("https://xueqiu.com/S/SZ164906")

    def get_result(self):
        price = float(self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong').text.replace("¥", ""))
        change = \
            self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[2]').text.split(" ")[
                1]
        change = float(change.strip("%")) / 100
        return (price, change)


class CNNETETF(Spider):
    def __init__(self):
        super().__init__()
        self.driver.get("https://xueqiu.com/S/SH513050")

    def get_result(self):
        try:
            price = float(self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong').text.replace("¥", ""))
            change = \
                self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[2]').text.split(
                    " ")[
                    1]
            change = float(change.strip("%")) / 100
        except:
            return (0, 0)
        return (price, change)


class JISILUConvertibleBond(object):
    # def __init__(self):
    #     super().__init__()
    #     self.driver.get("https://www.jisilu.cn/data/cbnew/#cb")
    # def get_result(self):
    #     time.sleep(5)
    #     a = self.driver.find_element_by_xpath('//*[@id="flex_cb"]/tbody')
    #     print(a.text.split("\n"))
    def __init__(self):
        self.url = 'https://www.jisilu.cn/data/cbnew/cb_list/'

    def get_result(self):
        r = json.loads(requests.get(self.url).text)
        rows = r["rows"]
        return rows


class NetWorth(Spider):
    def __init__(self, code):
        super().__init__()
        self.code = code
        self.driver.get("http://fund.eastmoney.com/{}.html".format(self.code))

    def get_result(self):
        # T-2净值
        net_worth_t_2 = self.driver.find_element_by_xpath('//*[@id="Li1"]/div[1]/table/tbody/tr[2]/td[2]').text
        self.close()
        return float(net_worth_t_2)


if __name__ == '__main__':
    print(Germany30SPIFSpider().get_result2())
