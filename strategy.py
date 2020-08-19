import datetime
import re

import requests
import tkinter as tk

from my_share import get_yesterday_amount, get_distance_of_delivery_day
from spider import YangQiETFSpider, YangQiIndexSpider, IFSpider, HS300ETF, HS300IndexSpider, HS300IOPV, \
    Germany30SPIFSpider, Germany30ETFSpider

"""
策略模式
Created by MinChengWen on 2020/8/12
"""


class Strategy(object):
    """
    创建策略对象
    """

    def __init__(self, ):
        pass

    @staticmethod
    def trans(*args):
        pass

    def get_result(self):
        pass


class ShareBondDifference(Strategy):
    """
    可转债转股和股票的价差
        :param p1: 股票价格(指数)
        :param p2: 可转债价格(对标指数)
        :param convertible_share_price: 转股价格
        :param buy1: 买一价
        :param sell1: 卖一价
        :param discount_percent1: 折价率1
        :param discount_percent2: 折价率2
        :param volume_of_transaction: 成交量
        :param amount_of_transaction: 成交金额
    """

    def __init__(self, threshold=None, stock=None, bond=None, p1=None, p2=None, convertible_share_price=None, buy1=None,
                 sell1=None, discount_percent1=None,
                 discount_percent2=None, volume_of_transaction=None, amount_of_transaction=None, strategy_name=None):
        super(ShareBondDifference, self).__init__()
        # 每一个策略实例都有一个标签对象
        self.var = tk.StringVar()  # 文本储存器
        self.l = tk.Label(textvar=self.var, font='Helvetica -30 bold', width=100,
                          height=4)  # 参数textvar不同于text,bg是backgroud
        self.l.pack()  # 放置标签

        self.threshold = threshold
        self.stock = stock
        self.bond = bond
        self.p1 = p1
        self.p2 = p2
        self.convertible_share_price = convertible_share_price
        self.buy1 = buy1
        self.sell1 = sell1
        self.discount_percent1 = discount_percent1
        self.discount_percent2 = discount_percent2
        self.volume_of_transaction = volume_of_transaction
        self.amount_of_transaction = amount_of_transaction
        self.strategy_name = strategy_name

    def get_result(self):
        headers = {
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        }
        try:
            stock, bond, _ = requests.get(
                "http://hq.sinajs.cn/?format=json&list={0},{1}".format(self.stock, self.bond),
                headers=headers).text.split(";")
            p1 = stock.split(",")[3]
            p2 = bond.split(",")[3]
        except requests.exceptions.ConnectionError:
            print("Connection refused")
            return

        # 有时数据现价为0，直接过就好
        if float(p1) == 0 or float(p2) == 0:
            return
        c = self.trans(p1, p2, self.convertible_share_price)
        if c < -self.threshold:
            msg = ("买入{0}，卖出{1},p1={2},p2={3},阈值为{4}".format(self.bond, self.stock, p1, p2, c))
            self.l["bg"] = "red"
            self.var.set(msg)
            return
        if c > self.threshold:
            msg = ("买入{0}，卖出{1},p1={0},p2={1},阈值为{4}".format(self.stock, self.bond, p1, p2, c))
            self.l["bg"] = "red"
            self.var.set(msg)
            return
        else:
            msg = ("股票{0}和转债{1}阈值为{2}，不操作,p1={3},p2={4}".format(self.stock, self.bond, c, p1, p2))
            self.l["bg"] = "yellow"
            self.var.set(msg)
            return

    @staticmethod
    def trans(p1, p2, convertible_share_price):
        """
        :param p1: 股票价格
        :param p2: 可转债价格
        :param convertible_share_price: 转股价格
        :return:
        """
        return float(p2) / (100 / convertible_share_price * float(p1)) - 1


class YangQiETF(Strategy):
    """
    515600，515680，515900，159974四个央企创新ETF，跟踪的指数为中证央企创新驱动指数000861
    4个ETF的昨日净值，叠加当日指数的涨跌，得出的实时净值，或者IOPV，和股市的卖一交易价相比，如果折价0.4%---0.6%为绿色，0.6%以上为红色。同时需要满足，前一日交易额大于500万。
    """

    def __init__(self, code1, code2, code3, code4, threshold1, threshold2):
        super(YangQiETF, self).__init__()
        self.code1 = code1
        self.code2 = code2
        self.code3 = code3
        self.code4 = code4
        self.threshold1 = threshold1
        self.threshold2 = threshold2
        # 创建四个标签
        self.var1 = tk.StringVar()  # 文本储存器
        self.var2 = tk.StringVar()  # 文本储存器
        self.var3 = tk.StringVar()  # 文本储存器
        self.var4 = tk.StringVar()  # 文本储存器
        self.l1 = tk.Label(textvar=self.var1, font='Helvetica -30 bold', width=100,
                           height=4)
        self.l2 = tk.Label(textvar=self.var2, font='Helvetica -30 bold', width=100,
                           height=4)
        self.l3 = tk.Label(textvar=self.var3, font='Helvetica -30 bold', width=100,
                           height=4)
        self.l4 = tk.Label(textvar=self.var4, font='Helvetica -30 bold', width=100,
                           height=4)
        self.l1.pack()  # 放置标签 self.var1 = tk.StringVar()  # 文本储存器
        self.l2.pack()  # 放置标签 self.var1 = tk.StringVar()  # 文本储存器
        self.l3.pack()  # 放置标签 self.var1 = tk.StringVar()  # 文本储存器
        self.l4.pack()  # 放置标签

        # 创建爬虫
        self.spider1 = YangQiETFSpider("sh515600")
        self.spider2 = YangQiETFSpider("sh515680")
        self.spider3 = YangQiETFSpider("sh515900")
        self.spider4 = YangQiETFSpider("sz159974")
        self.spider5 = YangQiIndexSpider()  # 央企创新指数
        # 获取昨日成交额
        self.yesterday_amount1 = get_yesterday_amount(self.code1)
        self.yesterday_amount2 = get_yesterday_amount(self.code2)
        self.yesterday_amount3 = get_yesterday_amount(self.code3)
        self.yesterday_amount4 = get_yesterday_amount(self.code4)
        # 获取昨日净值
        self.yesterday_value1 = self.spider1.get_result()
        self.yesterday_value2 = self.spider2.get_result()
        self.yesterday_value3 = self.spider3.get_result()
        self.yesterday_value4 = self.spider4.get_result()

    @staticmethod
    def get_sell1(code):
        headers = {
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        }
        try:
            sell1 = float(requests.get(
                "http://hq.sinajs.cn/?format=json&list={0}".format(code),
                headers=headers).text.split(",")[21])
        except:
            print("sell1获取失败")
            return
        return sell1

    def get_result(self):
        premium_rate_list = {}
        try:
            # 获取指数涨跌幅
            yang_qi_index = self.spider5.get_increase()
        except:
            print("获取指数错误")
            return

        iopv1 = self.yesterday_value1 * (1 + yang_qi_index)
        iopv2 = self.yesterday_value2 * (1 + yang_qi_index)
        iopv3 = self.yesterday_value3 * (1 + yang_qi_index)
        iopv4 = self.yesterday_value4 * (1 + yang_qi_index)
        sell1_1 = self.get_sell1(self.code1)
        sell1_2 = self.get_sell1(self.code2)
        sell1_3 = self.get_sell1(self.code3)
        sell1_4 = self.get_sell1(self.code4)
        print(self.yesterday_value1)
        print(yang_qi_index)
        print(iopv1)
        print(sell1_1)
        premium_rate1 = (sell1_1 - iopv1) / iopv1
        premium_rate2 = (sell1_2 - iopv2) / iopv2
        premium_rate3 = (sell1_3 - iopv3) / iopv3
        premium_rate4 = (sell1_4 - iopv4) / iopv4
        print(premium_rate1)
        premium_rate_list[self.code1] = [premium_rate1, self.yesterday_amount1, self.l1, self.var1]
        premium_rate_list[self.code2] = [premium_rate2, self.yesterday_amount2, self.l2, self.var2]
        premium_rate_list[self.code3] = [premium_rate3, self.yesterday_amount3, self.l3, self.var3]
        premium_rate_list[self.code4] = [premium_rate4, self.yesterday_amount4, self.l4, self.var4]
        for k, v in premium_rate_list.items():
            if self.threshold1 <= abs(v[0]) <= self.threshold2 and v[1] > 500:
                # 每一个策略实例都有一个标签对象
                msg = ("{0}，溢价率为{1},昨日成交额{2}万".format(k, '%.3f%%' % (v[0] * 100), v[1]))
                v[2]["bg"] = "green"
                v[3].set(msg)
                continue
            if abs(v[0]) > self.threshold2 and v[1] > 500:
                msg = ("{0}，溢价率为{1},昨日成交额为{2}万元".format(k, '%.3f%%' % (v[0] * 100), v[1]))
                v[2]["bg"] = "red"
                v[3].set(msg)
                continue
            else:
                msg = ("{0}，溢价率为{1},昨日成交额{2}万元".format(k, '%.3f%%' % (v[0] * 100), v[1]))
                v[2]["bg"] = "green"
                v[3].set(msg)
                continue


class IF300ETF(Strategy):
    """
    抓取IF当月连续合约实时价格，当月合约到期时间，000300沪深300指数实时价格。
当月贴水率=(沪深300指数实时价格-IF当月合约实时价格)/沪深300指数实时价格
当月年化贴水率=当月贴水率*365/当月合约到期时间
当月年化贴水率大于8%时，显示红色
当月年化贴水率介于6%至8%时，显示黄色
当月年化贴水率小于2%时，显示蓝色


抓取ETF基金510300，510310，510380，159919，515660，515360实时买一盘口价，卖一盘口价，实时IOPV，成交量。
当IF显示蓝色时，抓取的这些基金的(卖一盘口价/IOPV-1)里面最小值+0.1%的所有数据，成交量最大的基金显示青色。
当IF显示红色时，抓取的这些基金的(买一盘口价/IOPV-1)里面最大值-0.1%的所有数据，成交量最大的基金显示橙色。
    """

    def __init__(self, code1, code2, code3, code4, code5, code6):
        super(IF300ETF).__init__()
        self.current_month = datetime.datetime.now().month
        self.code1 = code1
        self.code2 = code2
        self.code3 = code3
        self.code4 = code4
        self.code5 = code5
        self.code6 = code6
        self.spider1 = HS300IndexSpider()  # 沪深300的爬虫
        self.spider2 = IFSpider()  # IF连续的指数
        self.spider3 = HS300ETF(code1, code2, code3, code4, code5, code6)  # 获取沪深300ETF的爬虫

        self.spider4 = HS300IOPV(code1)
        self.spider5 = HS300IOPV(code2)
        self.spider6 = HS300IOPV(code3)
        self.spider7 = HS300IOPV(code4)
        self.spider8 = HS300IOPV(code5)
        self.spider9 = HS300IOPV(code6)
        self.var1 = tk.StringVar()  # 文本储存器
        self.var2 = tk.StringVar()  # 文本储存器
        self.l1 = tk.Label(textvar=self.var1, font='Helvetica -30 bold', width=80,
                           height=3)
        self.l1.pack()  # 放置标签 self.var1 = tk.StringVar()  # 文本储存器
        self.l2 = tk.Label(textvar=self.var2, font='Helvetica -30 bold', width=80,
                           height=10)
        self.l2.pack()

    def get_if_delivery_day(self):
        year = datetime.date.today().year
        month = datetime.date.today().month
        first_day = datetime.date(year=year, month=month, day=1)
        print(first_day)

    def get_result(self):
        HS300index = self.spider1.get_result()
        print("300指数", HS300index)
        IFindex = self.spider2.get_result()
        print("IF指数", IFindex)
        contango_rate = (HS300index - IFindex) / HS300index
        have_days = get_distance_of_delivery_day()
        print(have_days)
        contango_rate_of_year = contango_rate * 365 / have_days
        print("年化贴水率", contango_rate_of_year)
        if contango_rate_of_year < 0.02:
            self.l1["bg"] = "blue"
            msg = "当月年化贴水率{}".format('%.3f%%' % (contango_rate_of_year * 100))
            self.var1.set(msg)
            IOPV_1 = self.spider4.get_result()
            IOPV_2 = self.spider5.get_result()
            IOPV_3 = self.spider6.get_result()
            IOPV_4 = self.spider7.get_result()
            IOPV_5 = self.spider8.get_result()
            IOPV_6 = self.spider9.get_result()
            # 买1卖1成交量
            info_list = self.spider3.get_result()
            info_list[0]["IOPV"] = IOPV_1
            info_list[1]["IOPV"] = IOPV_2
            info_list[2]["IOPV"] = IOPV_3
            info_list[3]["IOPV"] = IOPV_4
            info_list[4]["IOPV"] = IOPV_5
            info_list[5]["IOPV"] = IOPV_6
            result = []
            for i in info_list:
                result.append(
                    {"rate": float(i["buy1"]) / float(i["IOPV"]) - 1, "buy1": i["buy1"], "sell1": i["sell1"],
                     "buy1_num": i["buy1_num"], "sell1_num": i["sell1_num"], "volume": i["volume"], "code": i["name"]})
            # 排序
            result = sorted(result, key=lambda x: x["rate"])
            # 获取溢价率最小值
            min_rate = result[0]["rate"]
            new_result = []
            for i in result:
                if i["rate"] < min_rate + 0.001:
                    new_result.append(i)
            # max_volume_etf = max(new_result, key=lambda x: x["volume"])
            # comment = re.compile(r's(.*?),', re.S)
            # comment1 = comment.findall(max_volume_etf["code"])
            msg = ""
            for i in new_result:
                code = i["code"][13:21]
                msg1 = "基金为{},sell1/IOPV-1的值为{},成交量为{}万,买1盘口数量为{}\n\n".format(
                    code.replace("h", "").replace("=", ""),
                    '%.3f%%' % (i["rate"] * 100), float(i["volume"])/10000, i["buy1_num"])
                msg += msg1
            self.l2["bg"] = "green"
            self.var2.set(msg)

        if 0.02 <= contango_rate_of_year < 0.08:
            self.l1["bg"] = "white"
            msg = "当月年化贴水率{}".format('%.3f%%' % (contango_rate_of_year * 100))
            self.var1.set(msg)
            self.l2["bg"] = "white"
            self.var2.set("")
        elif 0.06 < contango_rate_of_year <= 0.08:
            self.l1["bg"] = "yellow"
            msg = "当月年化贴水率{}".format('%.3f%%' % (contango_rate_of_year * 100))
            self.var1.set(msg)
        elif contango_rate_of_year > 0.08:
            self.l1["bg"] = "red"
            msg = "当月年化贴水率{}".format('%.3f%%' % (contango_rate_of_year * 100))
            self.var1.set(msg)
            IOPV_1 = self.spider4.get_result()
            IOPV_2 = self.spider5.get_result()
            IOPV_3 = self.spider6.get_result()
            IOPV_4 = self.spider7.get_result()
            IOPV_5 = self.spider8.get_result()
            IOPV_6 = self.spider9.get_result()
            # 买1卖1成交量
            info_list = self.spider3.get_result()
            info_list[0]["IOPV"] = IOPV_1
            info_list[1]["IOPV"] = IOPV_2
            info_list[2]["IOPV"] = IOPV_3
            info_list[3]["IOPV"] = IOPV_4
            info_list[4]["IOPV"] = IOPV_5
            info_list[5]["IOPV"] = IOPV_6
            result = []
            for i in info_list:
                result.append(
                    {"rate": float(i["buy1"]) / float(i["IOPV"]) - 1, "buy1": i["buy1"], "sell1": i["sell1"],
                     "buy1_num": i["buy1_num"], "sell1_num": i["sell1_num"], "volume": i["volume"], "code": i["name"]})
            # 排序
            result = sorted(result, key=lambda x: x["rate"])
            # 获取溢价率最小值
            max_rate = result[5]["rate"]
            new_result = []
            for i in result:
                if i["rate"] > max_rate - 0.001:
                    new_result.append(i)
            msg = ""
            for i in new_result:
                # print(new_result)
                # max_volume_etf = max(new_result, key=lambda x: x["volume"])
                code = i["code"][13:21]
                msg1 = "基金为{},buy1/IOPV-1的值为{},成交量为{}万,卖1盘口数量为{}\n\n".format(
                    code.replace("h", "").replace("=", ""),
                    '%.3f%%' % (i["rate"] * 100), float(i["volume"])/10000, i["sell1_num"])
                msg += msg1
            self.l2["bg"] = "orange"
            self.var2.set(msg)

    @staticmethod
    def get_sell1_buy1(code):
        headers = {
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        }
        try:
            sell1 = float(requests.get(
                "http://hq.sinajs.cn/?format=json&list={0}".format(code),
                headers=headers).text.split(",")[21])
        except:
            print("sell1获取失败")
            return
        return sell1


class Germany30Strategy(Strategy):
    """德国30交易策略"""

    def __init__(self):
        super(Germany30Strategy, self).__init__()
        self.spider1 = Germany30SPIFSpider()
        self.spider2 = Germany30ETFSpider()
        # T-2日513030净值
        # T-1日德国30指数涨跌幅
        # T-1日德国30指数收盘值
        # T-1日欧元人民币中间价汇率
        # T日欧元人民币中间价汇率
        self.l1 = tk.Label(text="T-2日513030净值: ", bg="white").grid(row=0, column=0, padx=10, pady=5)
        self.entry1 = tk.Entry(width=20)
        self.entry1.grid(row=0, column=1, padx=10, pady=5)
        self.l2 = tk.Label(text="T-1德国30指数涨跌幅：", bg="white").grid(row=1, column=0, padx=10, pady=5)
        self.entry2 = tk.Entry(width=20)
        self.entry2.grid(row=1, column=1, padx=10, pady=5)
        self.l3 = tk.Label(text="T-1日德国30指数收盘值：", bg="white").grid(row=2, column=0, padx=10, pady=5)
        self.entry3 = tk.Entry(width=20)
        self.entry3.grid(row=2, column=1, padx=10, pady=5)
        self.l4 = tk.Label(text="T-1日欧元人民币中间价：", bg="white").grid(row=3, column=0, padx=10, pady=5)
        self.entry4 = tk.Entry(width=20)
        self.entry4.grid(row=3, column=1, padx=10, pady=5)
        self.l5 = tk.Label(text="T日欧元人民币中间价：", bg="white").grid(row=4, column=0, padx=10, pady=5)
        self.entry5 = tk.Entry(width=20)
        self.entry5.grid(row=4, column=1, padx=10, pady=5)
        tk.Button(text="启动", width=10, bg="grey", command=self.flag_).grid(row=6, column=0,
                                                                           padx=10, pady=5)
        tk.Button(text="停止", width=10, bg="grey", command=self.flag__).grid(row=6, column=1,
                                                                            padx=10, pady=5)
        # show Lable
        self.var = tk.StringVar()  # 文本储存器
        self.l6 = tk.Label(textvar=self.var, font='Helvetica -30 bold', width=30, height=3)
        self.l6.grid( row=5,columnspan=2,padx=10, pady=5)
        self.my_flag = False

    def get_result(self):
        if not self.my_flag:
            return
        # T日德国30股指期货实时点数
        p5 = float(self.spider1.get_result())
        # T日513030实时价格
        p6 = float(self.spider2.get_result())
        p1 = float(self.entry1.get())
        p2 = float(self.entry2.get())
        p20 = float(self.entry3.get())
        p3 = float(self.entry4.get())
        p4 = float(self.entry5.get())

        p7 = p1 * (1 + p2 * 0.95) * (1 + p3)
        p8 = p7 * (1 + (p5 / p20 - 1) * 0.95) * (1 + p4)

        # 条件：
        # 1）当P6 / P8 - 1 < -0.01
        # 时，买入513030，卖出德国30指数期货
        # 2）当P6 / P8 - 1 > 0.01
        # 时，申购513030
        result= p6 / p8 - 1
        print(result)
        if result < -0.01:
            self.var.set("买入513030，卖出德国30指数期货\nr={}".format(result))
            self.l6["bg"]="red"
            return
        if -0.01<result<0.01:
            self.var.set("无操作")
            self.l6["bg"]="white"
            return
        if result > 0.01:
            self.l6["bg"]="red"
            self.var.set("申购513030\nr={}".format(result))
            return

    def flag_(self):
        # T-1日513030估值
        self.my_flag = True
        return

    def flag__(self):
        self.my_flag = False
        return

    def valuation_t(self):
        # T日513030估值
        pass


class Context(object):
    def __init__(self, strategy):
        """初始化策略对象"""
        self.strategy = strategy

    def make_result(self):
        self.strategy.get_result()
        return
