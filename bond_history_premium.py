# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals

import datetime
# from gm.api import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds
from matplotlib import ticker


# set_token("64530fa8930fec8fc135b8da3210ee75ffe2aba6")


class Draw(object):
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.fig = plt.figure(num=1, figsize=(15, 8), dpi=80)
        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))  # 密度总坐标数除70
        plt.xticks(rotation=90)  # 设置横坐标显示的角度，角度是逆时针，自己看
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        plt.rcParams['axes.unicode_minus'] = False

    # def get_history_data(self, code, frequency='60s'):
    #     return history(symbol=code, frequency=frequency, start_time=self.start_time,
    #                    end_time=self.end_time,
    #                    df=False)

    def get_x_y(self, code, trans_price):
        # stock_history_data = self.get_history_data(code)
        stock_history_data = pds.read_excel("data/K线导出_{}_1分钟数据.xls".format(code.strip("SHSE.").strip("SZSE.")))
        stock_history_data = stock_history_data[["交易时间", "收盘价"]][
            (stock_history_data["交易时间"] > self.start_time) & (stock_history_data["交易时间"] < self.end_time)].dropna(
            axis=0,
            how="any")
        # stock_history_data = stock_history_data[["交易时间", "收盘价"]]
        bond_history_data = pds.read_excel("data/{}.xls".format(code))
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
            premium_rt = bond_price / (100 / trans_price * y_value_) - 1
            x_time.append(x_time_.strftime("%Y-%m-%d %H:%M:%S"))
            y_value.append(premium_rt)
        return x_time, y_value

    def draw(self, code, trans_price, color, label):
        x1, y1 = self.get_x_y(code, trans_price)
        plt.yticks(np.arange(-0.05, 0.05, 0.01))
        plt.plot(x1, y1, color, label=label)

    def run(self):
        self.draw("SHSE.601137", 11.29, "r", label="博威合金")
        self.draw("SHSE.600326", 7.16, "b", label="西藏天路")
        # self.draw("SHSE.603023", 3.99, "c", label="威帝股份")
        self.draw("SHSE.603179", 14.22, "g", label="新泉股份")
        self.draw("SHSE.601966", 18.12, "k", label="玲珑轮胎")
        self.draw("SHSE.603180", 44.14, "m", label="金牌橱柜")
        self.draw("SZSE.002013", 7.57, "y", label="中航机电")
        plt.legend()
        plt.savefig('my_picture/{}.png'.format(self.start_time.strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]), dpi=500,
                    bbox_inches='tight')
        plt.show()


# class PremiumHistory(object):
#     def __init__(self, code, start_time, end_time, file, trans_price, name):
#         # self.history_data = history(symbol=code, frequency='60s', start_time=start_time,
#         #                             end_time=end_time,
#         #                             df=False)
#         self.x_time = []
#         self.y_value = []
#         self.file = file
#         self.trans_price = trans_price
#         self.name = name
#         # 设置坐标轴名称
#         plt.xlabel('时间')
#         plt.ylabel(self.name + '溢价率')
#
#     def read_bond_excel(self):
#         """获取可转债的分钟行情"""
#
#         return pds.read_excel(self.file, sheet_name=0, usecols=[2, 6])
#
#     def draw_picture(self):
#         data = self.read_bond_excel()
#         for bar in self.history_data:
#             x_time_ = pds.to_datetime(bar["eob"]).tz_localize(None)
#             bond_price = data[data["交易时间"] == x_time_]["收盘价"]
#             y_value_ = bar["close"]
#             premium_rt = bond_price / (100 / self.trans_price * y_value_) - 1
#             self.x_time.append(x_time_.strftime("%Y-%m-%d %H:%M:%S"))
#             self.y_value.append(premium_rt)
#         x = np.array(self.x_time)
#         y = np.array(self.y_value)
#         plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))  # 密度总坐标数除70
#         plt.xticks(rotation=90)  # 设置横坐标显示的角度，角度是逆时针，自己看
#         plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
#         plt.rcParams['axes.unicode_minus'] = False
#         plt.plot(x, y, "r")
#         plt.show()


def run(start_time, days):
    day = 0
    num = 0
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    while True:
        print("num", num)
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

    run("2020-08-6 9:30:00", 10)
