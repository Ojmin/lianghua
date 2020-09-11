# -*- coding:gbk -*-
from xlpython import *
import json

from iFinDPy import *

from spider import Spider

THS_iFinDLogin("jztz093", "165805")


# 纳指100
# 标普500
# 法国cac40


class Germany30SPIFSpider(Spider):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super(Germany30SPIFSpider, self).__init__()
        self.driver.get("https://cn.investing.com/indices/germany-30-futures")

    def get_result(self):
        germany30_spif = float(self.driver.find_element_by_xpath('//*[@id="last_last"]').text.replace(",", ""))
        return germany30_spif


class Na100SPIFSpider(Spider):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super(Na100SPIFSpider, self).__init__()
        self.driver.get("https://cn.investing.com/indices/nq-100-futures")

    def get_result(self):
        index = float(self.driver.find_element_by_xpath('//*[@id="last_last"]').text.replace(",", ""))
        return index


class BiaoPu500SPIFSpider(Spider):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.driver.get("https://cn.investing.com/indices/us-spx-500-futures")

    def get_result(self):
        index = float(self.driver.find_element_by_xpath('//*[@id="last_last"]').text.replace(",", ""))
        return index


class FaguoCACSpider(Spider):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.driver.get("https://cn.investing.com/indices/france-40")

    def get_result(self):
        index = float(self.driver.find_element_by_xpath('//*[@id="last_last"]').text.replace(",", ""))
        return index


class JapanSpider(Spider):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.driver.get("https://cn.investing.com/indices/japan-225-futures")

    def get_result(self):
        index = float(self.driver.find_element_by_xpath('//*[@id="last_last"]').text.replace(",", ""))
        return index


spider1 = Germany30SPIFSpider()
spider2 = Na100SPIFSpider()
spider3 = BiaoPu500SPIFSpider()
spider4 = FaguoCACSpider()
spider5 = JapanSpider()


# 日本
@xlfunc
def get_T_japan_now_index():
    return spider5.get_result()


@xlfunc
def get_T_japan513000_ETF():
    table = json.loads(THS_RealtimeQuotes('513000.OF', 'latest;tradeTime;tradeDate', '', True))["tables"][0][
        "table"]
    return table["latest"][0]


@xlfunc
def get_T_japan513520_ETF():
    table = json.loads(THS_RealtimeQuotes('513520.OF', 'latest;tradeTime;tradeDate', '', True))["tables"][0][
        "table"]
    return table["latest"][0]


@xlfunc
def get_T_japan513880_ETF():
    table = json.loads(THS_RealtimeQuotes('513880.OF', 'latest;tradeTime;tradeDate', '', True))["tables"][0][
        "table"]
    return table["latest"][0]


# 德国

@xlfunc
def get_T_germany_now_index():
    return spider1.get_result()


@xlfunc
def get_T_germany_ETF():
    # 德国30场内价格
    germany_table = json.loads(THS_RealtimeQuotes('513030.OF', 'latest;tradeTime;tradeDate', '', True))["tables"][0][
        "table"]
    return germany_table["latest"][0]


# 呐

@xlfunc
def get_T_na513100_ETF():
    na_table1 = json.loads(THS_RealtimeQuotes("513100.OF", 'latest;tradeTime;tradeDate', '', True))["tables"][0][
        "table"]
    return na_table1["latest"][0]


@xlfunc
def get_T_na100_index():
    return spider2.get_result()


@xlfunc
def get_T_na159941_ETF():
    na_table2 = json.loads(THS_RealtimeQuotes("159941.OF", 'latest;tradeTime;tradeDate', '', True))["tables"][0][
        "table"]

    return na_table2["latest"][0]


# 标普500

@xlfunc
def get_T_biaopu500_ETF():
    biaopu_table = json.loads(THS_RealtimeQuotes("513500.OF", 'latest;tradeTime;tradeDate', '', True))["tables"][0][
        "table"]

    return biaopu_table["latest"][0]


@xlfunc
def get_T_biaopu500_index():
    return spider3.get_result()


# 法国

@xlfunc
def get_T_CAC_ETF():
    cac_table = json.loads(THS_RealtimeQuotes("513080.OF", 'latest;tradeTime;tradeDate', '', True))["tables"][0][
        "table"]

    return cac_table["latest"][0]


@xlfunc
def get_T_CAC_index():
    return spider4.get_result()


if __name__ == '__main__':
    pass
