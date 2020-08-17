import datetime
import json
import time

import requests


def get_if_delivery_day():
    """
    获取if连续合约交割日
    :return:
    """
    year = datetime.date.today().year
    month = datetime.date.today().month
    first_day = datetime.date(year=year, month=month, day=1)
    num = 0
    days = 0
    while True:
        date = first_day + datetime.timedelta(days=+days)
        weekday = date.weekday()
        if weekday == 4:
            num += 1
        if num == 3:
            break
        days += 1
    return date


def get_distance_of_delivery_day():
    """
    获取交割日距离当年1月1号的天数
    :return:
    """
    year = datetime.date.today().year
    d1 = datetime.date(year, 1, 1)
    d2 = get_if_delivery_day()
    interval = d2 - d1  # 两日期差距
    return float(interval.days)


def get_yesterday_amount(code):
    """
    获取前一日的成交额
    :return:
    """
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    }
    code = code[2:]
    now_time = datetime.datetime.now()
    date_ = (now_time + datetime.timedelta(days=-1)).strftime("%Y%m%d")
    tt = time.strptime(date_, '%Y%m%d')
    if tt.tm_wday > 5:
        date = (now_time + datetime.timedelta(days=-3)).strftime("%Y%m%d")
        url = "http://q.stock.sohu.com/hisHq?code=cn_{0}&start={1}&end={2}".format(code, date, date)
    else:
        url = "http://q.stock.sohu.com/hisHq?code=cn_{0}&start={1}&end={2}".format(code, date_, date_)
    r = requests.get(url, headers=headers)
    result = json.loads(r.text)
    amount = float(result[0]["hq"][0][8])
    return amount


class Calculation(object):
    def __init__(self):
        pass

    def get_result(self):
        pass


if __name__ == '__main__':
    get_yesterday_amount()
