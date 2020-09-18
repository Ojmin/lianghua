import pymysql
from EmQuantAPI import *
import pandas as pd

c.start(options='ForceLogin=1')
CONFIG = {
    "host": '127.0.0.1',
    "user": 'root',
    "pwd": '',
    'db': 'quantization'
}
code_str = ""
conn = pymysql.connect(CONFIG['host'], CONFIG['user'], CONFIG['pwd'],database=CONFIG['db'])
df = pd.read_excel("C:/Users/Administrator/Desktop/data/全部股票的名称代码.xlsx")
df = df.dropna(axis=0, how="any")
for _, row in df.iterrows():
    code_str += row["thscode"] + ","
cursor = conn.cursor()
data = c.csd("000001.SZ,000002.SZ",
             "open,close,high,low,preclose,change,pctchange,volume,amount,turn,amplitude,tnum,ISSTSTOCK,ISXSTSTOCK,HIGHLIMIT,LOWLIMIT",
             "20160701", "20160701", options="Ispandas=1,RowIndex=2")
print(data)
tuple_more=()
for _, row in data.iterrows():
    print(row)
    tuple_one=(row["CODES"],row["OPEN"],row["CLOSE"],row["HIGH"],row["LOW"],row["PRECLOSE"],row["CHANGE"],row["PCTCHANGE"],row["VOLUME"],row["AMOUNT"],row["TURN"],row["AMPLITUDE"],row["TNUM"],row["ISSTSTOCK"],row["ISXSTSTOCK"],row["HIGHLIMIT"],row["LOWLIMIT"],_,)
    tuple_more+=tuple_one
sql = 'insert into history_data_202008(`code`,`open`,`close`,`high`,`low`,`preclose`,`change`,`pctchange`,`volume`,`amount`,`turn`,`amplitude`,`tnum`,`ISSTSTOCK`,`ISXSTSTOCK`,`HIGHLIMIT`,`LOWLIMIT`,`time`)values{}'.format(tuple_more)
print(sql)
cursor.execute(sql)

conn.commit()
  
cursor.close()
# 关闭connection对象
conn.close()