# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals

import datetime
import matplotlib.pyplot as plt
import pandas as pds
from matplotlib import ticker


# set_token("64530fa8930fec8fc135b8da3210ee75ffe2aba6")


class Draw(object):
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))  # 密度总坐标数除70
        plt.xticks(rotation=90)  # 设置横坐标显示的角度，角度是逆时针，自己看
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        plt.rcParams['axes.unicode_minus'] = False

    def get_x_y(self, code, bond_code, trans_price):
        # stock_history_data = self.get_history_data(code)
        stock_history_data = pds.read_excel("data_202008/K线导出_{}_1分钟数据.xls".format(code))
        stock_history_data = stock_history_data[["交易时间", "收盘价"]][
            (stock_history_data["交易时间"] > self.start_time) & (stock_history_data["交易时间"] < self.end_time)].dropna(
            axis=0,
            how="any")
        # stock_history_data = stock_history_data[["交易时间", "收盘价"]]
        bond_history_data = pds.read_excel("data_202008/K线导出_{}_1分钟数据.xls".format(bond_code))
        x_time = []
        y_value = []
        for _, bar in stock_history_data.iterrows():
            x_time_ = pds.to_datetime(bar["交易时间"]).tz_localize(None)
            bond_price = bond_history_data[bond_history_data["交易时间"] == x_time_]["收盘价"].values
            if len(bond_price) == 1:
                bond_price = bond_price[0]
            else:
                break
            y_value_ = bar["收盘价"]
            premium_rate = bond_price / (100 / trans_price * y_value_) - 1
            premium_rt = premium_rate if premium_rate <= 0.005 else 0.005
            x_time.append(x_time_.strftime("%Y-%m-%d %H:%M:%S"))
            y_value.append(premium_rt)
            print(x_time_,code,bond_code,y_value_,bond_price)
        return x_time, y_value

    @staticmethod
    def config():
        plt.grid()  # 生成网格
        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))  # 密度总坐标数除70
        plt.xticks(rotation=60, fontsize=3)  # 设置横坐标显示的角度，角度是逆时针，自己看
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        plt.rcParams['axes.unicode_minus'] = False

    def draw(self, code, bond_code, trans_price, color, label, linestyle=None):

        x1, y1 = self.get_x_y(code, bond_code, trans_price)
        plt.plot(x1, y1, color, label=label, linestyle=linestyle, linewidth=0.5)

    def run(self):
        plt.figure(num=1, figsize=(15, 8), dpi=80)

        plt.subplot(2, 2, 1)
        self.config()
        self.draw("603626", "113521", 8.7, "b", label="科森转债")
        self.draw("300487", "123027", 29.33, "#FF0000", label="蓝晓转债")
        self.draw("300260", "123037", 11.08, "#00FFFF", label="新莱转债")
        self.draw("002727", "128067", 26.83, "#7FFFD4", label="一心转债")
        self.draw("603180", "113553", 44.14, "m", label="金牌橱柜")
        plt.legend(fontsize=3)

        plt.subplot(2, 2, 2)
        self.config()
        self.draw("603179", "113509", 14.22, "g", label="新泉股份")
        self.draw("603688", "113548", 15.1, "#FFDAB9", label="石英转债")
        self.draw("603089", "113561", 10.23, "#444444", label="正裕转债")
        self.draw("300545", "123038", 25.29, "#FFE4C4", label="联得转债")
        self.draw("603612", "113547", 10.52, "#660033", label="索通发展")
        plt.legend(fontsize=3)

        plt.subplot(2, 2, 3)
        self.config()
        self.draw("603035", "113550", 9.65, "#FF8C00", label="常汽转债")
        self.draw("601966", "113019", 18.12, "k", label="玲珑轮胎")
        self.draw("603313", "113520", 14.28, "#00FFFF", label="百合转债")
        self.draw("603733", "113554", 13.27, "#BDB76B", label="仙鹤转债")
        self.draw("002567", "128092", 8.63, "#ADFF2F", label="唐人转债")
        self.draw("601200", "113028", 10.36, "#EE82EE", label="环境转债")
        plt.legend(fontsize=3)

        plt.subplot(2, 2, 4)
        self.config()
        self.draw("002745", "128084", 12.80, "#8B0000", label="木森转债")
        self.draw("600105", "110058", 5.04, "#E9967A", label="永鼎转债")
        self.draw("600372", "110042", 14.12, "#2F4F4F", label="航电转债")
        self.draw("600326", "110060", 7.16, "#808080", label="天路转债")
        self.draw("002406", "128075", 5.54, "#00BFFF", label="远东转债")
        self.draw("300088", "123022", 6.15, "red", label="长信转债")
        plt.legend(fontsize=3)

        plt.savefig('my_picture/{}.png'.format(self.start_time.strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]), dpi=500,
                    bbox_inches='tight')
        plt.show()


def run(start_time, days):
    day = 0
    num = 0
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    while True:
        if num >= days:
            break

        date = start_time + datetime.timedelta(days=+day)
        weekday = date.weekday()
        if weekday == 5 or weekday == 6:
            print("ssssss")
            day += 1
            continue
        end_date = date + datetime.timedelta(hours=5.5)
        Draw(date, end_date).run()
        day += 1
        num += 1


if __name__ == '__main__':
    # PremiumHistory("SHSE.601137", start_time="2020-08-25 9:00:00", end_time="2020-08-25 15:00:00",
    #                file="data/SHSE.601137.xls", trans_price=11.29, name="博威合金").draw_picture()
    # PremiumHistory("SHSE.600326", start_time="2020-08-25 9:00:00", end_time="2020-08-25 15:00:00",
    #                file="data/SHSE.600326.xls", trans_price=7.16, name="西藏天路").draw_picture()
    # PremiumHistory("SHSE.603023", start_time="2020-08-25 9:00:00", end_time="2020-08-25 15:00:00",
    #                file="data/SHSE.603023.xls", trans_price=3.99, name="威帝股份").draw_picture()
    # PremiumHistory("SHSE.603179", start_time="2020-08-25 9:00:00", end_time="2020-08-25 15:00:00",
    #                file="data/SHSE.603179.xls", trans_price=14.22, name="新泉股份").draw_picture()
    # PremiumHistory("SHSE.601966", start_time="2020-08-25 9:00:00", end_time="2020-08-25 15:00:00",
    #                file="data/SHSE.601966.xls", trans_price=18.12, name="玲珑轮胎").draw_picture()
    # PremiumHistory("SHSE.603180", start_time="2020-08-25 9:00:00", end_time="2020-08-25 15:00:00",
    #                file="data/SHSE.603180.xls", trans_price=44.14, name="金牌橱柜").draw_picture()
    # PremiumHistory("SZSE.002013", start_time="2020-08-25 9:00:00", end_time="2020-08-25 15:00:00",
    #                file="data/SZSE.002013.xls", trans_price=7.57, name="中航机电").draw_picture()

    # Draw("2020-08-25 9:00:00", "2020-08-25 15:00:00").run()

    run("2020-08-5 9:30:00", 18)
