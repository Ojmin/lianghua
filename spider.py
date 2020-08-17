import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Spider(object):
    """基类"""

    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--hide-scrollbars")
        self.options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        self.driver = webdriver.Chrome(options=self.options,
                                       executable_path='C:/Users/Administrator/PycharmProjects/pythonProject/chromedriver.exe')
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


class IFSpider(Spider):
    """IF当月连续爬虫"""

    def __init__(self):
        super(IFSpider, self).__init__()
        self.driver.get("http://quote.eastmoney.com/gzqh/ifdylx.html")

    def get_result(self):
        try:
            if_index = self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/p[1]/i[1]").text
        except Exception as e:
            print("获取当月连续指数失败", e)
            return "0"
        print("if_index", if_index)
        return if_index


class HS300ETF(Spider):
    def __init__(self, code1, code2, code3, code4, code5, code6):
        super(HS300ETF, self).__init__()
        self.code1 = code1
        self.code2 = code2
        self.code3 = code3
        self.code4 = code4
        self.code5 = code5
        self.code6 = code6

    def get_result(self):
        requests.get(
            "http://hq.sinajs.cn/?format=json&list={0},{1},{2},{3},{4},{5}".format(self.code1, self.code2, self.code3,
                                                                                   self.code4, self.code5, self.code6))


if __name__ == '__main__':
    YangQiETFSpider("sh515600").get_result()
