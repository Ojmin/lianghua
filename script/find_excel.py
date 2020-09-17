import pandas as pd
search_str=input("请输入要找的关键字：")
search_excel=input("请输入要查找的excel：")
data = pd.read_excel(search_excel, sheet_name=None)
writer = pd.ExcelWriter("result.xlsx")
for k, v in data.items():
    print(k)# sheet
    my_dict = {"证券代码": [], "证券名称": [], "name": []}
    v = v.dropna(axis=0, how="any")
    for _, row in v.iterrows():  # hang
        for i in row[2:]:
            for name in i.split(","):  # 单元格
                if search_str in name:
                    my_dict["证券代码"].append(row["证券代码"])
                    my_dict["证券名称"].append(row["证券名称"])
                    my_dict["name"].append(name)

    pd.DataFrame(my_dict).to_excel(writer, sheet_name=k)
writer.save()
