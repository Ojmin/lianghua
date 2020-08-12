import requests
import tkinter as tk
import threading
from strategy import Context, Strategy, ShareBondDifference

"""
Created by MinChengWen on 2020/8/12
"""


class Tip(object):
    """
    提示标签类
    """

    def __init__(self, threshold, stock, bond, convertible_share_price):
        super().__init__()
        self.threshold = threshold
        self.stock = stock
        self.bond = bond
        self.convertible_share_price = convertible_share_price

        self.var = tk.StringVar()
        self.l = tk.Label(textvar=self.var, font='Helvetica -30 bold', width=100,
                          height=4)  # 参数textvar不同于text,bg是backgroud
        self.l.pack()  # 放置标签
        # self.bg = "yellow"

    # @staticmethod
    # def trans(p1, p2, convertible_share_price):
    #     """
    #     :param p1: 股票价格
    #     :param p2: 可转债价格
    #     :param convertible_share_price: 转股价格
    #     :return:
    #     """
    #     return float(p2) / (100 / convertible_share_price * float(p1)) - 1
    #
    # def tip(self):
    #     """抓取信息并实施策略"""
    #     headers = {
    #         'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
    #
    #     p1 = \
    #         requests.get("http://hq.sinajs.cn/?format=json&list={0}".format(self.stock), headers=headers).text.split(
    #             ",")[3]
    #     p2 = \
    #         requests.get("http://hq.sinajs.cn/?format=json&list={0}".format(self.bond), headers=headers).text.split(
    #             ",")[3]
    #     c = self.trans(p1, p2, self.convertible_share_price)
    #     if c < -self.threshold:
    #         msg = ("买入{0}，卖出{1},p1={2},p2={3},阈值为{4}".format(self.bond, self.stock, p1, p2, c))
    #         self.l["bg"] = "red"
    #         self.var.set(msg)
    #         return
    #     if c > self.threshold:
    #         msg = ("买入{0}，卖出{1},p1={0},p2={1},阈值为{4}".format(self.stock, self.bond, p1, p2, c))
    #         # self.l = tk.Label(textvar=self.var, bg="red", width=200, height=4)  # 参数textvar不同于text,bg是backgroud
    #         # self.l.pack()  # 放置标签
    #         self.l["bg"] = "red"
    #         self.var.set(msg)
    #         return
    #     else:
    #         msg = ("股票{0}和转债{1}阈值为{2}，不操作,p1={3},p2={4}".format(self.stock, self.bond, c, p1, p2))
    #         # self.l = tk.Label(textvar=self.var, bg="yellow", width=200, height=4)  # 参数textvar不同于text,bg是backgroud
    #         # self.l.pack()  # 放置标签
    #         self.l["bg"] = "yellow"
    #         self.var.set(msg)
    #         return


class Window(tk.Tk):
    """窗口类"""

    def __init__(self, wait_time=1000, *args, **kw):
        super().__init__()
        self.wm_title('提醒')
        self.configure(background='white')
        self.wm_minsize(1440, 770)  # 设置窗口最小化大小
        self.wm_maxsize(2880, 1600)  # 设置窗口最大化大小
        self.resizable(width=True, height=True)  # 设置窗口宽度不可变，高度可变

        self.strategy_list = self.get_strategy_list()
        self.run()
        self.refresh_data(wait_time)
        self.mainloop()

    def refresh_data(self, wait_time=1000):
        # 需要刷新数据的操作
        # 代码...
        self.notice(self.strategy_list)

        self.after(wait_time, self.refresh_data)  # 这里的10000单位为毫秒

    @staticmethod
    def notice(strategy_list):
        """
        获取所有要注意的股票，并执行监听
        以后做成异步的
        :param strategy_list: 策略列表
        :param tip_list: 股票列表
        :param tip_thread: 单个股票线程
        :return:
        """
        for strategy in strategy_list:
            t = threading.Thread(strategy.make_result(), args=())
            t.start()

    @staticmethod
    def get_strategy_list():
        """
        在这里添加股票 线程的标签
        :return:
        """
        tip_list = []
        strategy1 = Context(
            ShareBondDifference(threshold=0.01, stock="sh603733", bond="sh113554", convertible_share_price=13.27,
                                strategy_name="share_bond_difference"))
        strategy2 = Context(
            ShareBondDifference(threshold=0.005, stock="sz300059", bond="sz123041", convertible_share_price=13.13,
                                strategy_name="share_bond_difference"))
        strategy3 = Context(
            ShareBondDifference(threshold=0.005, stock="sz000861", bond="sz127003", convertible_share_price=3,
                                strategy_name="share_bond_difference"))
        strategy4 = Context(
            ShareBondDifference(threshold=0.005, stock="sz002567", bond="sz128092", convertible_share_price=8.63,
                                strategy_name="share_bond_difference"))
        # tip1 = Tip(0.01, "sh603733", "sh113554", 13.27)
        # tip2 = Tip(0.005, "sz300059", "sz123041", 13.13)
        # tip3 = Tip(0.005, "sz000861", "sz127003", 3)
        # tip4 = Tip(0.005, "sz002567", "sz128092", 8.63)
        # tip5 = Tip(0.005, "sh600998", "sh110034", 18.32)
        tip_list.append(strategy1)
        tip_list.append(strategy2)
        tip_list.append(strategy3)
        tip_list.append(strategy4)
        # tip_list.append(tip5)
        return tip_list

    def run(self):
        pass


if __name__ == '__main__':
    aa = Window()
    aa.refresh_data()
