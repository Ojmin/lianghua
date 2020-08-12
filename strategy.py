import requests
import tkinter as tk

"""
策略模式
Created by MinChengWen on 2020/8/12
"""


class Strategy(object):
    """
    创建策略对象
    """

    def __init__(self, stock=None, bond=None, threshold=None, p1=None, p2=None, convertible_share_price=None, buy1=None,
                 sell1=None, discount_percent1=None,
                 discount_percent2=None, volume_of_transaction=None, amount_of_transaction=None, strategy_name=None):
        """
        :param p1: 股票价格(指数）
        :param p2: 可转债价格(对标指数）
        :param convertible_share_price: 转股价格
        :param buy1: 买一价
        :param sell1: 卖一价
        :param discount_percent1: 折价率1
        :param discount_percent2: 折价率2
        :param volume_of_transaction: 成交量
        :param amount_of_transaction: 成交金额
        """
        self.stock = stock
        self.bond = bond
        self.threshold = threshold
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
        # 每一个策略实例都有一个标签对象
        self.var = tk.StringVar()  # 文本储存器
        self.l = tk.Label(textvar=self.var, font='Helvetica -30 bold', width=100,
                          height=4)  # 参数textvar不同于text,bg是backgroud
        self.l.pack()  # 放置标签

    @staticmethod
    def trans(p1, p2, convertible_share_price):
        """
        :param p1: 股票价格
        :param p2: 可转债价格
        :param convertible_share_price: 转股价格
        :return:
        """
        return float(p2) / (100 / convertible_share_price * float(p1)) - 1

    def get_result(self):
        pass


class ShareBondDifference(Strategy):
    """
    抓取信息并实施策略
    """

    def __init__(self):
        super().__init__()

    def get_result(self):
        headers = {
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

        p1 = \
            requests.get("http://hq.sinajs.cn/?format=json&list={0}".format(self.stock), headers=headers).text.split(
                ",")[3]
        p2 = \
            requests.get("http://hq.sinajs.cn/?format=json&list={0}".format(self.bond), headers=headers).text.split(
                ",")[3]
        c = self.trans(p1, p2, self.convertible_share_price)
        print(c,1111)
        if c < -self.threshold:
            msg = ("买入{0}，卖出{1},p1={2},p2={3},阈值为{4}".format(self.bond, self.stock, p1, p2, c))
            self.l["bg"] = "red"
            self.var.set(msg)
            return
        if c > self.threshold:
            msg = ("买入{0}，卖出{1},p1={0},p2={1},阈值为{4}".format(self.stock, self.bond, p1, p2, c))
            # self.l = tk.Label(textvar=self.var, bg="red", width=200, height=4)  # 参数textvar不同于text,bg是backgroud
            # self.l.pack()  # 放置标签
            self.l["bg"] = "red"
            self.var.set(msg)
            return
        else:
            msg = ("股票{0}和转债{1}阈值为{2}，不操作,p1={3},p2={4}".format(self.stock, self.bond, c, p1, p2))
            # self.l = tk.Label(textvar=self.var, bg="yellow", width=200, height=4)  # 参数textvar不同于text,bg是backgroud
            # self.l.pack()  # 放置标签
            self.l["bg"] = "yellow"
            self.var.set(msg)
            return


class Context(object):
    def __init__(self, strategy):
        """初始化策略对象"""
        self.strategy = strategy

    def make_result(self, ):
        print(1111)
        print(self.strategy)
        return self.strategy.get_result()
