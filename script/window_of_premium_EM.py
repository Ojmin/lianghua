from script.redis_pool import r
import tkinter as tk


class MyLabel2(object):
    def __init__(self, font='Helvetica -20 bold', width=500, height=5):
        self.var = tk.StringVar()
        self.l = tk.Label(textvar=self.var, font=font, width=width,
                          height=height, padx=2)
        self.l.pack()

    def set(self, msg):
        self.var.set(msg)

    def bg(self, bg="red"):
        self.l["bg"] = bg


class Window(tk.Tk):
    """窗口类"""

    def __init__(self, wait_time=1000, *args, **kw):
        super().__init__()
        self.wm_title('提醒')
        self.configure(background='white')
        self.wm_minsize(360, 260)  # 设置窗口最小化大小
        self.wm_maxsize(4880, 2600)  # 设置窗口最大化大小
        self.resizable(width=True, height=True)  # 设置窗口宽度不可变，高度可变

        self.l1 = MyLabel2(height=2, width=150)
        self.l2 = MyLabel2(height=2, width=150)
        self.l3 = MyLabel2(height=2, width=150)
        self.l4 = MyLabel2(height=2, width=150)
        self.l5 = MyLabel2(height=2, width=150)
        self.l6 = MyLabel2(height=2, width=150)
        self.l7 = MyLabel2(height=2, width=150)
        self.l8 = MyLabel2(height=2, width=150)
        self.l9 = MyLabel2(height=2, width=150)
        self.l10 = MyLabel2(height=2, width=150)
        self.l11 = MyLabel2(height=2, width=150)
        self.l12 = MyLabel2(height=2, width=150)
        self.l13 = MyLabel2(height=2, width=150)
        self.l14 = MyLabel2(height=2, width=150)
        self.l15 = MyLabel2(height=2, width=150)
        self.l_list = [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9, self.l10,
                       self.l11, self.l12, self.l13, self.l14, self.l15]
        self.refresh_data(wait_time)
        self.mainloop()

    def refresh_data(self, wait_time=1000):
        # 需要刷新数据的操作
        # 代码...
        # {'113581.SH': {'bond_name': '龙蟠转债', 'premium_rate': -0.1172043085441542}, '123063.SZ': {'bond_name': '大禹转债', 'premium_rate': -0.08589065112212024}}
        data = eval(r.get("result"))
        print(data)
        # 溢价率排序
        # data = sorted(data, key=lambda x: x["premium_rt"])
        # 涨跌幅排序
        data = [i for i in data if i["stock_pctchange"] > 0.08 or i["stock_pctchange"] - i["bond_pctchange"] > 0.05]
        data = sorted(data, key=lambda x: x["stock_pctchange"] - x["bond_pctchange"], reverse=True)
        self.after(wait_time, self.refresh_data)  # 这里的10000单位为毫秒
        # if len(data) < 10:
        #     return
        for i in range(len(data)):
            bond_name = data[i]["bond_name"]
            bond_amount = data[i]["bond_amount"]
            stock_amount = data[i]["stock_amount"]
            premium_rt = data[i]["premium_rt"]
            bond_pctchange = data[i]["bond_pctchange"]
            stock_pctchange = data[i]["stock_pctchange"]
            # bond_price = data[i]["bond_now"]
            self.l_list[i].set(bond_name + "溢价率：" + (str(100 * premium_rt))[:6] + "%" + " 转债涨跌：" + (str(
                bond_pctchange * 100))[:4] + "%" + " 正股涨跌：" + (str(stock_pctchange * 100))[
                                                              :4] + "%" + " 正股涨幅-转债涨幅：" + str((
                                                                                                      stock_pctchange - bond_pctchange) * 100)[
                                                                                          :4] + "%" + " 转债成交额：" + str(
                bond_amount/10000000)+"千万" + " 股票成交额：" + str(stock_amount/10000000)+"千万")
            if stock_pctchange - bond_pctchange > 0.05 and stock_pctchange > 0.08:
                self.l_list[i].bg("red")
            elif stock_pctchange - bond_pctchange > 0.05:
                self.l_list[i].bg("green")
            elif stock_pctchange > 0.08:
                self.l_list[i].bg("orange")
            else:
                self.l_list[i].bg("white")
        for i in range(15 - len(data), 10):
            self.l_list[i].bg("white")
            self.l_list[i].set("")


if __name__ == '__main__':
    aa = Window()
    aa.refresh_data()
