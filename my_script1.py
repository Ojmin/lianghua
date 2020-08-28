# -*- coding: utf-8 -*-
import json
import os
import xmltodict


def xml_to_json(xml_str):
    # parse是的xml解析器
    xml_parse = xmltodict.parse(xml_str)
    # json库dumps()是将dict转化成json格式,loads()是将json转化成dict格式。
    # dumps()方法的ident=1,格式化json
    json_str = json.dumps(xml_parse, indent=1)
    return json_str


path_list = os.listdir("测试/")
path_list.sort()
for filename in path_list:
    suffix = filename.split(".")[1]

    if suffix == "ETF":
        code = ""
        all_value = ""
        info = ""
        with open("测试/" + filename, "r", encoding="gbk") as f:
            a = f.readlines()
        for i in a:
            if i.find("NAVperCU") != -1:
                all_value = i.split("=")[1]
            if i.find("Fundid1") != -1:
                code = i.split('=')[1]
            if i.find("000877") == -1:
                continue
            else:
                info = i.strip(" ")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write("code:" + code + "NAVperCU:" + all_value + "提取的信息:" + info + "\n")
    if suffix == "xml":
        info = ""
        code = ""
        NAVperCU = ""
        with  open("测试/" + filename, "r", encoding="utf-8") as f:
            a = f.read()
            b = xml_to_json(a)
            dict_b = json.loads(b)
            items = dict_b["PCFFile"]["Components"]['Component']
            for item in items:
                if item["UnderlyingSecurityID"] == "000877":
                    code = dict_b["PCFFile"]["SecurityID"]
                    NAVperCU = dict_b["PCFFile"]["NAVperCU"]
                    info = json.dumps(item)
                    with open("result.txt", "a+", encoding="utf-8") as f:
                        f.write("code:" + code+"\n" + "NAVperCU:" + NAVperCU +"\n"+ "提取的信息:" + info + "\n")
