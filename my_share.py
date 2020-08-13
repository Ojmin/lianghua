import datetime
import json

import requests


def get_yesterday_amount(code):
    """
    获取前一日的成交额
    :return:
    """
    code=code[2:]
    now_time = datetime.datetime.now()
    date = (now_time + datetime.timedelta(days=-1)).strftime("%Y%m%d")
    r = requests.get(
        "http://q.stock.sohu.com/hisHq?code=cn{0}&start={1}&end={2}".format(code, date, date))
    result = json.loads(r.text)
    amount = result[0]["hq"][0][8]
    print(amount)
    return amount


if __name__ == '__main__':
    get_yesterday_amount()
