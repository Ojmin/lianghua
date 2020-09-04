import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
import statsmodels.api as sm

df = pd.read_excel("data_hs300/my_statsmodel.xlsx", sheet_name="历史行情1")
df = df.dropna(axis=0, how="any")
df.columns = ["date", "y", "x1", "x2", "x3", "x4", "x5"]


def looper(limit):
    cols = ['x1', 'x2', 'x3', "x4", 'x5']
    for i in range(len(cols)):
        # df.loc["new"] = [1,1, 1, 1, 1, 1, 1]
        data1 = df[cols]

        x = sm.add_constant(data1)  # 生成自变量
        y = df['y']  # 生成因变量
        model = sm.OLS(y.astype(float), x.astype(float))  # 生成模型
        result = model.fit()  # 模型拟合
        pvalues = result.pvalues  # 得到结果中所有P值
        pvalues.drop('const', inplace=True)  # 把const取得
        pmax = max(pvalues)  # 选出最大的P值
        if pmax > limit:
            ind = pvalues.idxmax()  # 找出最大P值的index
            cols.remove(ind)  # 把这个index从cols中删除
        else:
            return result


def get_c():
    result = looper(0.05)
    return result.params.values


def draw(start_time, end_time):
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))  # 密度总坐标数除70
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    plt.grid()  # 生成网格
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(2))  # 密度总坐标数除70
    plt.xticks(rotation=60, fontsize=3)  # 设置横坐标显示的角度，角度是逆时针
    c = get_c()
    print(c)
    x_time = []
    y_increase = []
    hs_increase = []
    for date1 in df.date[
        (df.date > datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")) & (
                df.date < datetime.datetime.strptime(end_time,
                                                     "%Y-%m-%d %H:%M:%S"))]:
        row = df[df.date == date1]
        k = date1.strftime("%Y-%m-%d")
        x_time.append(k)
        y = c[0] + c[1] * row.x1.values[0] + c[2] * row.x2.values[0] + c[3] * row.x3.values[0] + c[4] * row.x4.values[
            0] + c[5] * row.x5.values[0]
        y_increase.append(y)
        hs_increase.append(row.y.values[0])
    plt.plot(x_time, y_increase, "black", label="拟合曲线")
    plt.scatter(x_time, hs_increase, c="red", label="真实点位")
    plt.legend()
    plt.savefig('my_picture/a.png', dpi=500,
                bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    draw("2018-9-3 00:00:00", "2019-2-3 00:00:00")
    # print(df)
    # print(get_c())
