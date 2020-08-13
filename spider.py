from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Spider(object):
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


class YangQiETFSpider(Spider):
    def __init__(self, code):
        super(YangQiETFSpider, self).__init__()
        self.code = code

    def get_result(self, ):
        self.driver.get("https://xueqiu.com/S/{}".format(self.code))
        premium_rate = self.driver.find_element_by_xpath(
            "//*[@id='app']/div[2]/div[2]/div[5]/table/tbody/tr[4]/td[2]/span")
        return premium_rate.text


if __name__ == '__main__':
    YangQiETFSpider("sh515600").get_result()
