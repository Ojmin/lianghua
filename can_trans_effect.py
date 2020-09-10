import json

import requests


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
        print(rows)
        return rows

if __name__ == '__main__':
    JISILUConvertibleBond().get_result()
