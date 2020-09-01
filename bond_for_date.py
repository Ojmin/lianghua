import datetime
import math

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

from bond_history_premium import Draw


def chunks(arr, m):
    n = int(math.ceil(len(arr) / float(m)))
    return [arr[i:i + n] for i in range(0, len(arr), n)]


class NewDraw(Draw):
    def __init__(self, start_time, end_time):
        super().__init__(start_time=start_time, end_time=end_time)

    def run(self):
        pass


my_dict = {"蓝晓转债": {"bond_id": "123027", "stock_id": "300487", "trans_price": 29.33, "color": "#FF0000"},
           "科森转债": {"bond_id": "113521", "stock_id": "603626", "trans_price": 8.7, "color": "b"},
           "新莱转债": {"bond_id": "123037", "stock_id": "300260", "trans_price": 11.08, "color": "#00FFFF"},
           "一心转债": {"bond_id": "128067", "stock_id": "002727", "trans_price": 26.83, "color": "#7FFFD4"},
           "金牌转债": {"bond_id": "113553", "stock_id": "603180", "trans_price": 44.14, "color": "m"},
           "新泉转债": {"bond_id": "113509", "stock_id": "603179", "trans_price": 14.22, "color": "g"},
           "石英转债": {"bond_id": "113548", "stock_id": "603688", "trans_price": 15.1, "color": "#FFDAB9"},
           "正裕转债": {"bond_id": "113561", "stock_id": "603089", "trans_price": 10.23, "color": "#444444"},
           "联得转债": {"bond_id": "123038", "stock_id": "300545", "trans_price": 25.29, "color": "#FFE4C4"},
           "索发转债": {"bond_id": "113547", "stock_id": "603612", "trans_price": 10.52, "color": "#660033"},
           "常汽转债": {"bond_id": "113550", "stock_id": "603035", "trans_price": 9.65, "color": "#FF8C00"},
           "玲珑转债": {"bond_id": "113019", "stock_id": "601966", "trans_price": 18.12, "color": "k"},
           "百合转债": {"bond_id": "113520", "stock_id": "603313", "trans_price": 14.28, "color": "#00FFFF"},
           "仙鹤转债": {"bond_id": "113554", "stock_id": "603733", "trans_price": 13.27, "color": "#BDB76B"},
           "唐人转债": {"bond_id": "128092", "stock_id": "002567", "trans_price": 8.63, "color": "#ADFF2F"},
           "环境转债": {"bond_id": "113028", "stock_id": "601200", "trans_price": 10.36, "color": "#EE82EE"},
           "木森转债": {"bond_id": "128084", "stock_id": "002745", "trans_price": 12.80, "color": "#8B0000"},
           "永鼎转债": {"bond_id": "110058", "stock_id": "600105", "trans_price": 5.04, "color": "#E9967A"},
           "航电转债": {"bond_id": "110042", "stock_id": "600372", "trans_price": 14.12, "color": "#2F4F4F"},
           "天路转债": {"bond_id": "110060", "stock_id": "600326", "trans_price": 7.16, "color": "#808080"},
           "远东转债": {"bond_id": "128075", "stock_id": "002406", "trans_price": 5.54, "color": "#00BFFF"},
           "长信转债": {"bond_id": "123022", "stock_id": "300088", "trans_price": 6.15, "color": "red"},

           "博威转债": {"bond_id": "113031", "stock_id": "601137", "trans_price": 11.29, "color": "red"},
           "东财转2": {"bond_id": "123041", "stock_id": "300059", "trans_price": 13.13, "color": "red"},
           "国轩转债": {"bond_id": "123022", "stock_id": "002074", "trans_price": 12.19, "color": "red"},
           "国祯转债": {"bond_id": "123002", "stock_id": "300388", "trans_price": 8.48, "color": "red"},
           "威帝转债": {"bond_id": "113514", "stock_id": "603023", "trans_price": 3.99, "color": "red"},

           "艾华转债": {"bond_id": "113504", "stock_id": "603989", "trans_price": 21.13, "color": "red"},
           "顾家转债": {"bond_id": "113518", "stock_id": "603816", "trans_price": 35.42, "color": "red"},
           "机电转债": {"bond_id": "128045", "stock_id": "002013", "trans_price": 7.57, "color": "red"},  # 中航机电
           "欧派转债": {"bond_id": "113543", "stock_id": "603833", "trans_price": 71.69, "color": "red"},
           "兄弟转债": {"bond_id": "128021", "stock_id": "002562", "trans_price": 5.25, "color": "red"},
           "浙商转债": {"bond_id": "113022", "stock_id": "601878", "trans_price": 12.37, "color": "red"},
           "振德转债": {"bond_id": "113555", "stock_id": "603301", "trans_price": 14.01, "color": "red"},
           "太阳转债": {"bond_id": "128029", "stock_id": "002078", "trans_price": 8.55, "color": "red"},
           "桃李转债": {"bond_id": "113544", "stock_id": "603866", "trans_price": 46.54, "color": "red"},
           "金禾转债": {"bond_id": "128017", "stock_id": "002597", "trans_price": 22.42, "color": "red"},
           "英科转债": {"bond_id": "123029", "stock_id": "300677", "trans_price": 16.11, "color": "red"},
           "汽模转2": {"bond_id": "128090", "stock_id": "002510", "trans_price": 4.21, "color": "red"},
           "华钰转债": {"bond_id": "113027", "stock_id": "601020", "trans_price": 10.17, "color": "red"},
           "日月转债": {"bond_id": "113558", "stock_id": "603218", "trans_price": 13.84, "color": "red"},
           "深南转债": {"bond_id": "128088", "stock_id": "002916", "trans_price": 105.79, "color": "red"},
           "麦米转债": {"bond_id": "128089", "stock_id": "002851", "trans_price": 20.15, "color": "red"},
           "视源转债": {"bond_id": "128059", "stock_id": "002841", "trans_price": 74.97, "color": "red"},
           "海印转债": {"bond_id": "127003", "stock_id": "000861", "trans_price": 3.00, "color": "red"},
           "电气转债": {"bond_id": "113008", "stock_id": "601727", "trans_price": 5.13, "color": "red"},
           "太极转债": {"bond_id": "128078", "stock_id": "002368", "trans_price": 22.4, "color": "red"},
           "中环转债": {"bond_id": "123026", "stock_id": "300692", "trans_price": 12.25, "color": "red"},
           "众信转债": {"bond_id": "128022", "stock_id": "002707", "trans_price": 7.91, "color": "red"},
           "东音转债": {"bond_id": "128043", "stock_id": "002793", "trans_price": 6.22, "color": "red"},
           "克来转债": {"bond_id": "113552", "stock_id": "603960", "trans_price": 19.78, "color": "red"},
           "富祥转债": {"bond_id": "123020", "stock_id": "300497", "trans_price": 9.28, "color": "red"},
           "九洲转债": {"bond_id": "110034", "stock_id": "600998", "trans_price": 18.32, "color": "red"},
           "乐普转债": {"bond_id": "123022", "stock_id": "300003", "trans_price": 32.19, "color": "red"},
           "三星转债": {"bond_id": "113536", "stock_id": "603578", "trans_price": 19.54, "color": "red"},

           }


def config():
    plt.grid()  # 生成网格
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))  # 密度总坐标数除70
    plt.xticks(rotation=60, fontsize=3)  # 设置横坐标显示的角度，角度是逆时针，自己看
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False


df = pd.read_excel("bond_of_day/每日折价转债.xlsx")
for i in range(len(df.columns.values)):
    names = df.iloc[:, i].values
    names = [x for x in names if not pd.isnull(x)]
    print(names)
    date = df.columns.values[i]
    bond_num = len(names)
    my_list = chunks(names, 4)
    lenth = len(my_list)
    plt.figure(num=1, figsize=(15, 8), dpi=80)
    obj = NewDraw(start_time=pd.to_datetime(date, format='%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=9.5),
                  end_time=pd.to_datetime(date, format='%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=15))
    for j in range(lenth):
        plt.subplot(2, 2, j + 1)
        config()
        for k in range(len(my_list[j])):
            if pd.isnull(my_list[j][k]):  # is name
                break
            info = my_dict[my_list[j][k]]

            obj.draw(
                code=info["stock_id"], bond_code=info["bond_id"], trans_price=info["trans_price"], color=info["color"],
                label=my_list[j][k])
        plt.legend(fontsize=3)
    plt.savefig('my_picture1/{}.png'.format(
        pd.to_datetime(date, format='%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]), dpi=500,
                bbox_inches='tight')
    plt.show()
# if __name__ == '__main__':
#     print(chunks([1, 2, 3, 4, 3], 3))
