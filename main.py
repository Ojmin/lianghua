import tkinter as tk
import threading
from strategy import Context, YangQiETF, IF300ETF

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
        self.l = tk.Label(textvar=self.var, font='Helvetica -30 bold', width=50,
                          height=3)  # 参数textvar不同于text,bg是backgroud
        self.l.pack()  # 放置标签
        # self.bg = "yellow"


class Window(tk.Tk):
    """窗口类"""

    def __init__(self, wait_time=1000, *args, **kw):
        super().__init__()
        self.wm_title('提醒')
        self.configure(background='white')
        self.wm_minsize(360, 260)  # 设置窗口最小化大小
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
        t_list = []
        for strategy in strategy_list:
            t = threading.Thread(strategy.make_result(), args=())
            t_list.append(t)
        for t in t_list:
            t.start()

    @staticmethod
    def get_strategy_list():
        """
        在这里添加股票 线程的标签
        :return:
        """
        tip_list = []
        # 转债
        # strategy1 = Context(
        #     ShareBondDifference(threshold=0.01, stock="sh603733", bond="sh113554", convertible_share_price=13.27,
        #                         strategy_name="share_bond_difference"))
        # strategy2 = Context(
        #     ShareBondDifference(threshold=0.005, stock="sz300059", bond="sz123041", convertible_share_price=13.13,
        #                         strategy_name="share_bond_difference"))
        # strategy3 = Context(
        #     ShareBondDifference(threshold=0.005, stock="sz000861", bond="sz127003", convertible_share_price=3,
        #                         strategy_name="share_bond_difference"))
        # strategy4 = Context(
        #     ShareBondDifference(threshold=0.005, stock="sz002567", bond="sz128092", convertible_share_price=8.63,
        #                         strategy_name="share_bond_difference"))
        # strategy5 = Context(
        #     ShareBondDifference(threshold=0.01, stock="sh600998", bond="sh110034", convertible_share_price=18.32,
        #                         strategy_name="share_bond_difference"))
        # tip_list.append(strategy1)
        # tip_list.append(strategy2)
        # tip_list.append(strategy3)
        # tip_list.append(strategy4)
        # tip_list.append(strategy5)
        # 央企创新
        # strategy6 = Context(YangQiETF("sh515600", "sh515680", "sh515900", "sz159974", 0.004, 0.006))
        # tip_list.append(strategy6)
        #IF连续
        strategy7 = Context(IF300ETF("sh510300", "sh510310", "sh510380", "sz159919", "sh515660", "sh515360"))
        tip_list.append(strategy7)
        return tip_list

    def run(self):
        pass


if __name__ == '__main__':
    aa = Window()
    aa.refresh_data(wait_time=500)
