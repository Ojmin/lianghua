# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from gm.api import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds
from matplotlib import ticker

set_token("a451fcb820aff8a8344f52fce3089d4e192fc3a4")
history_data = history(symbol='SHSE.603336', frequency='60s', start_time='2020-8-26 9:40:0',
                       end_time='2020-8-26 15:00:0',
                       df=False)
print(history_data)
x_time = []
y_value = []

# 设置坐标轴名称
plt.xlabel('时间')
plt.ylabel('溢价率')

data = pds.read_excel("aaa.xls", sheet_name=0, usecols=[2, 6])
for bar in history_data:
    x_time_ = pds.to_datetime(bar["eob"]).tz_localize(None)
    bond_price = data[data["交易时间"] == x_time_]["收盘价"]
    y_value_ = bar["close"]
    premium_rt = bond_price / (100 / 10 * y_value_) - 1
    x_time.append(x_time_.strftime("%Y-%m-%d %H:%M:%S"))
    y_value.append(premium_rt)

x = np.array(x_time)
y = np.array(y_value)
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))  # 密度总坐标数除70
plt.xticks(rotation=90)  # 设置横坐标显示的角度，角度是逆时针，自己看
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x, y, "r")
plt.show()
