import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Spider(object):
    def __init__(self):
        self.options = Options()
        # self.options.add_argument('--headless')
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
    def __init__(self, code):
        super(YangQiETFSpider, self).__init__()
        self.code = code
        self.driver.get("https://xueqiu.com/S/{}".format(self.code))

    def get_result(self, ):
        try:
            yesterday_value = float(self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div[5]/table/tbody/tr[3]/td[3]/span').text)  # 昨日净值

        except Exception as e:
            print("获取净值失败",e)
            return 0.00
        return yesterday_value


if __name__ == '__main__':
    YangQiETFSpider("sh515600").get_result()
