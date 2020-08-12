import requests
import time
import tkinter as tk


def trans(p1, p2, convertible_share_price):
    """
    :param p1: 股票价格
    :param p2: 可转债价格
    :param convertible_share_price: 转股价格
    :return:
    """
    return float(p2) / (100 / convertible_share_price * float(p1)) - 1


class Tip(object):
    def __init__(self, threshold, stock, bond, convertible_share_price):
        super().__init__()
        self.threshold = threshold
        self.stock = stock
        self.bond = bond
        self.convertible_share_price = convertible_share_price

        self.var = tk.StringVar()
        self.l = tk.Label(textvar=self.var, width=200, height=4)  # 参数textvar不同于text,bg是backgroud
        self.l.pack()  # 放置标签
        # self.bg = "yellow"

    def tip(self):
        # time.sleep(1)

        headers = {
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

        p1 = \
            requests.get("http://hq.sinajs.cn/?format=json&list={0}".format(self.stock), headers=headers).text.split(
                ",")[3]
        p2 = \
            requests.get("http://hq.sinajs.cn/?format=json&list={0}".format(self.bond), headers=headers).text.split(
                ",")[3]
        c = trans(p1, p2, self.convertible_share_price)
        if c < -self.threshold:
            xianhe = ("买入{0}，卖出{1},p1={2},p2={3},阈值为{4}".format(self.bond, self.stock, p1, p2, c))
            self.l["bg"] = "red"
            self.var.set(xianhe)
            return
        if c > self.threshold:
            xianhe = ("买入{0}，卖出{1},p1={0},p2={1},阈值为{4}".format(self.stock, self.bond, p1, p2, c))
            # self.l = tk.Label(textvar=self.var, bg="red", width=200, height=4)  # 参数textvar不同于text,bg是backgroud
            # self.l.pack()  # 放置标签
            self.l["bg"] = "red"
            self.var.set(xianhe)
            return
        else:
            xianhe = ("阈值为{0}，不操作,p1={1},p2={2}".format(c, p1, p2))
            # self.l = tk.Label(textvar=self.var, bg="yellow", width=200, height=4)  # 参数textvar不同于text,bg是backgroud
            # self.l.pack()  # 放置标签
            self.l["bg"] = "blue"
            self.var.set(xianhe)
            return


class Window(tk.Tk):
    def __init__(self, wait_time=1000, *args, **kw):
        super().__init__()
        self.wm_title('提醒')
        self.configure(background='white')
        self.wm_minsize(1440, 770)  # 设置窗口最小化大小
        self.wm_maxsize(2880, 1600)  # 设置窗口最大化大小
        self.resizable(width=True, height=True)  # 设置窗口宽度不可变，高度可变

        self.tip_list = self.get_tip_list()
        self.run()
        self.refresh_data(wait_time)
        self.mainloop()

    def refresh_data(self, wait_time=1000):
        # 需要刷新数据的操作
        # 代码...

        self.notice(self.tip_list)

        self.after(wait_time, self.refresh_data)  # 这里的10000单位为毫秒

    @staticmethod
    def notice(tip_list):
        """
        获取所有要注意的股票，并执行监听
        以后做成异步的
        :param tip: 标签对象
        :return:
        """
        for tip in tip_list:
            tip.tip()

    @staticmethod
    def get_tip_list():
        """
        在这里添加股票的标签
        :return:
        """
        tip_list = []
        tip1 = Tip(0.01, "sh603733", "sh113554", 13.27)
        tip2 = Tip(0.005, "sz300059", "sz123041", 13.13)
        tip_list.append(tip1)
        tip_list.append(tip2)
        return tip_list

    def run(self):
        pass


if __name__ == '__main__':
    aa = Window()

    aa.refresh_data()
