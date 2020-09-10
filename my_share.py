# -*- coding:utf-8 -*-
import datetime
import json
import time

import requests

year = datetime.date.today().year
month = datetime.date.today().month


def get_if_delivery_day(year, month):
    """
    获取if连续合约交割日
    :return:
    """
    first_day = datetime.date(year=year, month=month, day=1)
    num = 0
    days = 0
    while True:
        date = first_day + datetime.timedelta(days=+days)
        weekday = date.weekday()
        if weekday == 4:
            num += 1
        if num == 3:
            if date < datetime.date.today():
                month += 1
                if month > 12:
                    month = 1
                    year += 1
                return get_if_delivery_day(year, month)
            else:
                return date
        days += 1

    # 如果本月已交割，求下一个月的交割日


def get_distance_of_delivery_day():
    """
    获取距离交割日天数
    :return:
    """
    d1 = datetime.date.today()
    d2 = get_if_delivery_day(year, month)
    interval = d2 - d1  # 两日期差距
    if interval.days == 0:
        d2 = get_if_delivery_day(year, month + 1)
        return float((d2 - d1).days)
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
    print(get_distance_of_delivery_day())
