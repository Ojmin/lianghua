# Create By MinChengwen on 2020 9 8
import json
from iFinDPy import *
import tkinter as tk


# import time
# from spider import Spider

# class JSLSpider(Spider):
#     def __init__(self):
#         super().__init__()
#
#         self.driver.get("https://www.jisilu.cn/web/data/cb/list")
#         self.driver.implicitly_wait(10)
#
#     def get_result(self):
#         time.sleep(2)
#         my_list = ""
#         i = 0
#         while True:
#
#             self.driver.execute_script("window.scrollTo(0,{})".format(i))
#
#             time.sleep(2)
#
#             tr = self.driver.find_element_by_xpath(
#                 '//[@id="app"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody').text
#             my_list += tr
#             check_height1 = self.driver.execute_script("return document.body.scrollHeight;")
#
#             if i >= check_height1:
#                 break
#             i += 1000
#         return my_list
#
#
# spider = JSLSpider()
#
#
# def create_my_dict():
#     my_dict = {}
#     bond_list = spider.get_result().split("\n\ue61e\n")
#     for i in bond_list:
#         c = i.split("\n")
#         if c[1] in my_dict.keys():
#             continue
#         my_dict[c[1]] = {"bond_name": c[2], "stock_name": c[6], "bond_code": c[1], "stock_code": c[5],"trans_price":c[10]}
#     print(111111, my_dict)
class MyLabel2(object):
    def __init__(self, font='Helvetica -20 bold', width=500, height=5):
        self.var = tk.StringVar()
        self.l = tk.Label(textvar=self.var, font=font, width=width,
                          height=height,padx=2)
        self.l.pack()

    def set(self, msg):
        self.var.set(msg)

    def bg(self, bg="red"):
        self.l["bg"] = bg


my_dict = {'113581': {'bond_name': '龙蟠转债', 'stock_name': '龙蟠科技', 'bond_code': '113581', 'stock_code': '603906',
                      'trans_price': '9.48'},
           '123063': {'bond_name': '大禹转债', 'stock_name': '大禹节水', 'bond_code': '123063', 'stock_code': '300021',
                      'trans_price': '4.94'},
           '113575': {'bond_name': '东时转债', 'stock_name': '东方时尚R', 'bond_code': '113575', 'stock_code': '603377',
                      'trans_price': '14.56'},
           '123050': {'bond_name': '聚飞转债', 'stock_name': '聚飞光电', 'bond_code': '123050', 'stock_code': '300303',
                      'trans_price': '5.18'},
           '123051': {'bond_name': '今天转债', 'stock_name': '今天国际', 'bond_code': '123051', 'stock_code': '300532',
                      'trans_price': '8.80'},
           '123062': {'bond_name': '三超转债', 'stock_name': '三超新材', 'bond_code': '123062', 'stock_code': '300554',
                      'trans_price': '17.17'},
           '113586': {'bond_name': '上机转债', 'stock_name': '上机数控', 'bond_code': '113586', 'stock_code': '603185',
                      'trans_price': '33.31'},
           '113585': {'bond_name': '寿仙转债', 'stock_name': '寿仙谷', 'bond_code': '113585', 'stock_code': '603896',
                      'trans_price': '28.68'},
           '113580': {'bond_name': '康隆转债', 'stock_name': '康隆达', 'bond_code': '113580', 'stock_code': '603665',
                      'trans_price': '15.51'},
           '123046': {'bond_name': '天铁转债', 'stock_name': '天铁股份', 'bond_code': '123046', 'stock_code': '300587',
                      'trans_price': '10.12'},
           '128108': {'bond_name': '蓝帆转债', 'stock_name': '蓝帆医疗R', 'bond_code': '128108', 'stock_code': '002382',
                      'trans_price': '17.79'},
           '113572': {'bond_name': '三祥转债', 'stock_name': '三祥新材', 'bond_code': '113572', 'stock_code': '603663',
                      'trans_price': '14.19'},
           '123049': {'bond_name': '维尔转债', 'stock_name': '维尔利', 'bond_code': '123049', 'stock_code': '300190',
                      'trans_price': '7.48'},
           '128104': {'bond_name': '裕同转债', 'stock_name': '裕同科技', 'bond_code': '128104', 'stock_code': '002831',
                      'trans_price': '23.24'},
           '113571': {'bond_name': '博特转债', 'stock_name': '苏博特', 'bond_code': '113571', 'stock_code': '603916',
                      'trans_price': '18.88'},
           '123004': {'bond_name': '铁汉转债', 'stock_name': '铁汉生态R', 'bond_code': '123004', 'stock_code': '300197',
                      'trans_price': '3.98'},
           '123048': {'bond_name': '应急转债', 'stock_name': '中船应急R', 'bond_code': '123048', 'stock_code': '300527',
                      'trans_price': '8.90'},
           '128115': {'bond_name': '巨星转债', 'stock_name': '巨星科技R', 'bond_code': '128115', 'stock_code': '002444',
                      'trans_price': '12.28'},
           '123044': {'bond_name': '红相转债', 'stock_name': '红相股份', 'bond_code': '123044', 'stock_code': '300427',
                      'trans_price': '18.80'},
           '113592': {'bond_name': '安20转债', 'stock_name': '安井食品R', 'bond_code': '113592', 'stock_code': '603345',
                      'trans_price': '115.90'},
           '123047': {'bond_name': '久吾转债', 'stock_name': '久吾高科', 'bond_code': '123047', 'stock_code': '300631',
                      'trans_price': '17.61'},
           '123030': {'bond_name': '九洲转债', 'stock_name': '九洲集团', 'bond_code': '123030', 'stock_code': '300040',
                      'trans_price': '5.65'},
           '123037': {'bond_name': '新莱转债 ', 'stock_name': '新莱应材', 'bond_code': '123037', 'stock_code': '300260',
                      'trans_price': '11.08'},
           '128098': {'bond_name': '康弘转债', 'stock_name': '康弘药业R', 'bond_code': '128098', 'stock_code': '002773',
                      'trans_price': '35.30'},
           '123002': {'bond_name': '国祯转债', 'stock_name': '国祯环保', 'bond_code': '123002', 'stock_code': '300388',
                      'trans_price': '8.48'},
           '128071': {'bond_name': '合兴转债', 'stock_name': '合兴包装', 'bond_code': '128071', 'stock_code': '002228',
                      'trans_price': '4.28'},
           '113544': {'bond_name': '桃李转债 ', 'stock_name': '桃李面包R', 'bond_code': '113544', 'stock_code': '603866',
                      'trans_price': '46.54'},
           '113035': {'bond_name': '福莱转债', 'stock_name': '福莱特R', 'bond_code': '113035', 'stock_code': '601865',
                      'trans_price': '13.56'},
           '128102': {'bond_name': '海大转债', 'stock_name': '海大集团R', 'bond_code': '128102', 'stock_code': '002311',
                      'trans_price': '34.74'},
           '123022': {'bond_name': '长信转债 ', 'stock_name': '长信科技R', 'bond_code': '123022', 'stock_code': '300088',
                      'trans_price': '6.15'},
           '113561': {'bond_name': '正裕转债', 'stock_name': '正裕工业', 'bond_code': '113561', 'stock_code': '603089',
                      'trans_price': '10.23'},
           '123056': {'bond_name': '雪榕转债', 'stock_name': '雪榕生物', 'bond_code': '123056', 'stock_code': '300511',
                      'trans_price': '11.89'},
           '113587': {'bond_name': '泛微转债', 'stock_name': '泛微网络', 'bond_code': '113587', 'stock_code': '603039',
                      'trans_price': '64.33'},
           '128097': {'bond_name': '奥佳转债', 'stock_name': '奥佳华', 'bond_code': '128097', 'stock_code': '002614',
                      'trans_price': '10.69'},
           '128084': {'bond_name': '木森转债 ', 'stock_name': '木林森R', 'bond_code': '128084', 'stock_code': '002745',
                      'trans_price': '12.80'},
           '128058': {'bond_name': '拓邦转债', 'stock_name': '拓邦股份', 'bond_code': '128058', 'stock_code': '002139',
                      'trans_price': '5.47'},
           '128067': {'bond_name': '一心转债', 'stock_name': '一心堂R', 'bond_code': '128067', 'stock_code': '002727',
                      'trans_price': '26.83'},
           '110058': {'bond_name': '永鼎转债', 'stock_name': '永鼎股份R', 'bond_code': '110058', 'stock_code': '600105',
                      'trans_price': '5.04'},
           '128092': {'bond_name': '唐人转债 ', 'stock_name': '唐人神R', 'bond_code': '128092', 'stock_code': '002567',
                      'trans_price': '8.63'},
           '113595': {'bond_name': '花王转债', 'stock_name': '花王股份', 'bond_code': '113595', 'stock_code': '603007',
                      'trans_price': '6.94'},
           '113543': {'bond_name': '欧派转债', 'stock_name': '欧派家居R', 'bond_code': '113543', 'stock_code': '603833',
                      'trans_price': '71.69'},
           '113554': {'bond_name': '仙鹤转债 ', 'stock_name': '仙鹤股份', 'bond_code': '113554', 'stock_code': '603733',
                      'trans_price': '13.27'},
           '113566': {'bond_name': '翔港转债', 'stock_name': '翔港科技', 'bond_code': '113566', 'stock_code': '603499',
                      'trans_price': '10.77'},
           '113565': {'bond_name': '宏辉转债', 'stock_name': '宏辉果蔬', 'bond_code': '113565', 'stock_code': '603336',
                      'trans_price': '10.00'},
           '128064': {'bond_name': '司尔转债', 'stock_name': '司尔特R', 'bond_code': '128064', 'stock_code': '002538',
                      'trans_price': '6.07'},
           '113028': {'bond_name': '环境转债 ', 'stock_name': '上海环境', 'bond_code': '113028', 'stock_code': '601200',
                      'trans_price': '10.36'},
           '113020': {'bond_name': '桐昆转债', 'stock_name': '桐昆股份R', 'bond_code': '113020', 'stock_code': '601233',
                      'trans_price': '12.28'},
           '113547': {'bond_name': '索发转债 ', 'stock_name': '索通发展', 'bond_code': '113547', 'stock_code': '603612',
                      'trans_price': '10.52'},
           '113555': {'bond_name': '振德转债 ', 'stock_name': '振德医疗', 'bond_code': '113555', 'stock_code': '603301',
                      'trans_price': '14.01'},
           '123034': {'bond_name': '通光转债 ', 'stock_name': '通光线缆', 'bond_code': '123034', 'stock_code': '300265',
                      'trans_price': '7.97'},
           '128124': {'bond_name': '科华转债', 'stock_name': '科华生物R', 'bond_code': '128124', 'stock_code': '002022',
                      'trans_price': '21.50'},
           '123011': {'bond_name': '德尔转债', 'stock_name': '德尔股份', 'bond_code': '123011', 'stock_code': '300473',
                      'trans_price': '34.54'},
           '113584': {'bond_name': '家悦转债', 'stock_name': '家家悦R', 'bond_code': '113584', 'stock_code': '603708',
                      'trans_price': '37.97'},
           '113596': {'bond_name': '城地转债', 'stock_name': '城地股份', 'bond_code': '113596', 'stock_code': '603887',
                      'trans_price': '29.21'},
           '113527': {'bond_name': '维格转债', 'stock_name': '锦泓集团', 'bond_code': '113527', 'stock_code': '603518',
                      'trans_price': '9.85'},
           '127011': {'bond_name': '中鼎转2', 'stock_name': '中鼎股份R', 'bond_code': '127011', 'stock_code': '000887',
                      'trans_price': '11.59'},
           '128026': {'bond_name': '众兴转债', 'stock_name': '众兴菌业', 'bond_code': '128026', 'stock_code': '002772',
                      'trans_price': '11.45'},
           '127012': {'bond_name': '招路转债', 'stock_name': '招商公路', 'bond_code': '127012', 'stock_code': '001965',
                      'trans_price': '8.81'},
           '113024': {'bond_name': '核建转债', 'stock_name': '中国核建R', 'bond_code': '113024', 'stock_code': '601611',
                      'trans_price': '9.76'},
           '128012': {'bond_name': '辉丰转债', 'stock_name': 'ST辉丰', 'bond_code': '128012', 'stock_code': '002496',
                      'trans_price': '4.38'},
           '113573': {'bond_name': '纵横转债', 'stock_name': '纵横通信R', 'bond_code': '113573', 'stock_code': '603602',
                      'trans_price': '18.81'},
           '127021': {'bond_name': '特发转2', 'stock_name': '特发信息R', 'bond_code': '127021', 'stock_code': '000070',
                      'trans_price': '12.33'},
           '113014': {'bond_name': '林洋转债', 'stock_name': '林洋能源R', 'bond_code': '113014', 'stock_code': '601222',
                      'trans_price': '8.54'},
           '113597': {'bond_name': '佳力转债', 'stock_name': '佳力图', 'bond_code': '113597', 'stock_code': '603912',
                      'trans_price': '23.40'},
           '113026': {'bond_name': '核能转债', 'stock_name': '中国核电R', 'bond_code': '113026', 'stock_code': '601985',
                      'trans_price': '6.08'},
           '113530': {'bond_name': '大丰转债', 'stock_name': '大丰实业', 'bond_code': '113530', 'stock_code': '603081',
                      'trans_price': '16.64'},
           '132014': {'bond_name': '18中化EBQ', 'stock_name': '中国化学R', 'bond_code': '132014', 'stock_code': '601117',
                      'trans_price': '7.35'},
           '128033': {'bond_name': '迪龙转债', 'stock_name': '雪迪龙', 'bond_code': '128033', 'stock_code': '002658',
                      'trans_price': '8.83'},
           '110031': {'bond_name': '航信转债', 'stock_name': '航天信息R', 'bond_code': '110031', 'stock_code': '600271',
                      'trans_price': '21.56'},
           '128101': {'bond_name': '联创转债', 'stock_name': '联创电子R', 'bond_code': '128101', 'stock_code': '002036',
                      'trans_price': '14.48'},
           '128122': {'bond_name': '兴森转债', 'stock_name': '兴森科技R', 'bond_code': '128122', 'stock_code': '002436',
                      'trans_price': '14.18'},
           '113012': {'bond_name': '骆驼转债', 'stock_name': '骆驼股份R', 'bond_code': '113012', 'stock_code': '601311',
                      'trans_price': '10.06'},
           '113589': {'bond_name': '天创转债', 'stock_name': '天创时尚', 'bond_code': '113589', 'stock_code': '603608',
                      'trans_price': '12.64'},
           '127018': {'bond_name': '本钢转债', 'stock_name': '本钢板材R', 'bond_code': '127018', 'stock_code': '000761',
                      'trans_price': '5.03'},
           '128015': {'bond_name': '久其转债', 'stock_name': '久其软件', 'bond_code': '128015', 'stock_code': '002279',
                      'trans_price': '9.48'},
           '128052': {'bond_name': '凯龙转债', 'stock_name': '凯龙股份R', 'bond_code': '128052', 'stock_code': '002783',
                      'trans_price': '6.67'},
           '113535': {'bond_name': '大业转债', 'stock_name': '大业股份', 'bond_code': '113535', 'stock_code': '603278',
                      'trans_price': '12.40'},
           '113574': {'bond_name': '华体转债', 'stock_name': '华体科技', 'bond_code': '113574', 'stock_code': '603679',
                      'trans_price': '33.99'},
           '128126': {'bond_name': '赣锋转2', 'stock_name': '赣锋锂业R', 'bond_code': '128126', 'stock_code': '002460',
                      'trans_price': '61.15'},
           '113021': {'bond_name': '中信转债', 'stock_name': '中信银行R', 'bond_code': '113021', 'stock_code': '601998',
                      'trans_price': '6.98'},
           '128044': {'bond_name': '岭南转债', 'stock_name': '岭南股份', 'bond_code': '128044', 'stock_code': '002717',
                      'trans_price': '5.91'},
           '128032': {'bond_name': '双环转债', 'stock_name': '双环传动', 'bond_code': '128032', 'stock_code': '002472',
                      'trans_price': '9.89'},
           '110059': {'bond_name': '浦发转债', 'stock_name': '浦发银行R', 'bond_code': '110059', 'stock_code': '600000',
                      'trans_price': '14.45'},
           '113508': {'bond_name': '新凤转债', 'stock_name': '新凤鸣', 'bond_code': '113508', 'stock_code': '603225',
                      'trans_price': '15.78'},
           '128014': {'bond_name': '永东转债', 'stock_name': '永东股份', 'bond_code': '128014', 'stock_code': '002753',
                      'trans_price': '12.60'},
           '132008': {'bond_name': '17山高EB', 'stock_name': '山东高速R', 'bond_code': '132008', 'stock_code': '600350',
                      'trans_price': '9.02'},
           '113009': {'bond_name': '广汽转债', 'stock_name': '广汽集团R', 'bond_code': '113009', 'stock_code': '601238',
                      'trans_price': '14.26'},
           '127008': {'bond_name': '特发转债', 'stock_name': '特发信息R', 'bond_code': '127008', 'stock_code': '000070',
                      'trans_price': '5.54'},
           '128072': {'bond_name': '翔鹭转债', 'stock_name': '翔鹭钨业', 'bond_code': '128072', 'stock_code': '002842',
                      'trans_price': '15.31'},
           '128035': {'bond_name': '大族转债', 'stock_name': '大族激光R', 'bond_code': '128035', 'stock_code': '002008',
                      'trans_price': '52.10'},
           '113569': {'bond_name': '科达转债', 'stock_name': '苏州科达R', 'bond_code': '113569', 'stock_code': '603660',
                      'trans_price': '14.84'},
           '132004': {'bond_name': '15国盛EB', 'stock_name': '上海建工R', 'bond_code': '132004', 'stock_code': '600170',
                      'trans_price': '5.30'},
           '123015': {'bond_name': '蓝盾转债', 'stock_name': '蓝盾股份R', 'bond_code': '123015', 'stock_code': '300297',
                      'trans_price': '5.79'},
           '110045': {'bond_name': '海澜转债', 'stock_name': '海澜之家R', 'bond_code': '110045', 'stock_code': '600398',
                      'trans_price': '11.75'},
           '128010': {'bond_name': '顺昌转债', 'stock_name': '澳洋顺昌', 'bond_code': '128010', 'stock_code': '002245',
                      'trans_price': '9.25'},
           '113502': {'bond_name': '嘉澳转债', 'stock_name': '嘉澳环保', 'bond_code': '113502', 'stock_code': '603822',
                      'trans_price': '44.79'},
           '132013': {'bond_name': '17宝武EBQ', 'stock_name': '宝钢股份R', 'bond_code': '132013', 'stock_code': '600019',
                      'trans_price': '8.77'},
           '113016': {'bond_name': '小康转债', 'stock_name': '小康股份R', 'bond_code': '113016', 'stock_code': '601127',
                      'trans_price': '15.70'},
           '128023': {'bond_name': '亚太转债', 'stock_name': '亚太股份', 'bond_code': '128023', 'stock_code': '002284',
                      'trans_price': '10.34'},
           '128041': {'bond_name': '盛路转债', 'stock_name': '盛路通信R', 'bond_code': '128041', 'stock_code': '002446',
                      'trans_price': '6.85'},
           '128100': {'bond_name': '搜特转债', 'stock_name': '搜于特R', 'bond_code': '128100', 'stock_code': '002503',
                      'trans_price': '5.36'},
           '132009': {'bond_name': '17中油EB', 'stock_name': '中国石油R', 'bond_code': '132009', 'stock_code': '601857',
                      'trans_price': '8.41'},
           '132007': {'bond_name': '16凤凰EBQ', 'stock_name': '凤凰传媒R', 'bond_code': '132007', 'stock_code': '601928',
                      'trans_price': '14.20'},
           '127004': {'bond_name': '模塑转债', 'stock_name': '模塑科技R', 'bond_code': '127004', 'stock_code': '000700',
                      'trans_price': '7.46'},
           '132015': {'bond_name': '18中油EB', 'stock_name': '中国石油R', 'bond_code': '132015', 'stock_code': '601857',
                      'trans_price': '8.84'},
           '128037': {'bond_name': '岩土转债', 'stock_name': '中化岩土', 'bond_code': '128037', 'stock_code': '002542',
                      'trans_price': '7.99'},
           '132011': {'bond_name': '17浙报EBQ', 'stock_name': '浙数文化R', 'bond_code': '132011', 'stock_code': '600633',
                      'trans_price': '23.98'},
           '128062': {'bond_name': '亚药转债', 'stock_name': '亚太药业R', 'bond_code': '128062', 'stock_code': '002370',
                      'trans_price': '16.25'},
           '110044': {'bond_name': '广电转债 ', 'stock_name': '广电网络R', 'bond_code': '110044', 'stock_code': '600831',
                      'trans_price': '6.90'},
           '123013': {'bond_name': '横河转债', 'stock_name': '横河模具', 'bond_code': '123013', 'stock_code': '300539',
                      'trans_price': '9.13'},
           '128075': {'bond_name': '远东转债 ', 'stock_name': '远东传动', 'bond_code': '128075', 'stock_code': '002406',
                      'trans_price': '5.54'},
           '123038': {'bond_name': '联得转债', 'stock_name': '联得装备', 'bond_code': '123038', 'stock_code': '300545',
                      'trans_price': '25.29'},
           '127015': {'bond_name': '希望转债', 'stock_name': '新希望R', 'bond_code': '127015', 'stock_code': '000876',
                      'trans_price': '19.63'},
           '128017': {'bond_name': '金禾转债 ', 'stock_name': '金禾实业R', 'bond_code': '128017', 'stock_code': '002597',
                      'trans_price': '22.42'},
           '113548': {'bond_name': '石英转债 ', 'stock_name': '石英股份R', 'bond_code': '113548', 'stock_code': '603688',
                      'trans_price': '15.10'},
           '113564': {'bond_name': '天目转债', 'stock_name': '天目湖', 'bond_code': '113564', 'stock_code': '603136',
                      'trans_price': '23.80'},
           '113541': {'bond_name': '荣晟转债', 'stock_name': '荣晟环保', 'bond_code': '113541', 'stock_code': '603165',
                      'trans_price': '11.54'},
           '113577': {'bond_name': '春秋转债', 'stock_name': '春秋电子R', 'bond_code': '113577', 'stock_code': '603890',
                      'trans_price': '11.06'},
           '113537': {'bond_name': '文灿转债', 'stock_name': '文灿股份', 'bond_code': '113537', 'stock_code': '603348',
                      'trans_price': '19.78'},
           '128112': {'bond_name': '歌尔转2', 'stock_name': '歌尔股份R', 'bond_code': '128112', 'stock_code': '002241',
                      'trans_price': '23.27'},
           '123029': {'bond_name': '英科转债 ', 'stock_name': '英科医疗', 'bond_code': '123029', 'stock_code': '300677',
                      'trans_price': '16.11'},
           '113504': {'bond_name': '艾华转债 ', 'stock_name': '艾华集团R', 'bond_code': '113504', 'stock_code': '603989',
                      'trans_price': '21.13'},
           '113520': {'bond_name': '百合转债 ', 'stock_name': '梦百合', 'bond_code': '113520', 'stock_code': '603313',
                      'trans_price': '14.28'},
           '128078': {'bond_name': '太极转债', 'stock_name': '太极股份R', 'bond_code': '128078', 'stock_code': '002368',
                      'trans_price': '22.40'},
           '123027': {'bond_name': '蓝晓转债', 'stock_name': '蓝晓科技', 'bond_code': '123027', 'stock_code': '300487',
                      'trans_price': '29.33'},
           '113536': {'bond_name': '三星转债', 'stock_name': '三星新材', 'bond_code': '113536', 'stock_code': '603578',
                      'trans_price': '19.54'},
           '113599': {'bond_name': '嘉友转债', 'stock_name': '嘉友国际', 'bond_code': '113599', 'stock_code': '603871',
                      'trans_price': '24.82'},
           '127003': {'bond_name': '海印转债', 'stock_name': '海印股份R', 'bond_code': '127003', 'stock_code': '000861',
                      'trans_price': '3.00'},
           '113582': {'bond_name': '火炬转债', 'stock_name': '火炬电子R', 'bond_code': '113582', 'stock_code': '603678',
                      'trans_price': '25.33'},
           '128099': {'bond_name': '永高转债', 'stock_name': '永高股份', 'bond_code': '128099', 'stock_code': '002641',
                      'trans_price': '6.16'},
           '128105': {'bond_name': '长集转债', 'stock_name': '长青集团', 'bond_code': '128105', 'stock_code': '002616',
                      'trans_price': '8.11'},
           '123059': {'bond_name': '银信转债', 'stock_name': '银信科技', 'bond_code': '123059', 'stock_code': '300231',
                      'trans_price': '9.91'},
           '128073': {'bond_name': '哈尔转债', 'stock_name': '哈尔斯', 'bond_code': '128073', 'stock_code': '002615',
                      'trans_price': '5.72'},
           '123026': {'bond_name': '中环转债 ', 'stock_name': '中环环保', 'bond_code': '123026', 'stock_code': '300692',
                      'trans_price': '12.25'},
           '128057': {'bond_name': '博彦转债', 'stock_name': '博彦科技', 'bond_code': '128057', 'stock_code': '002649',
                      'trans_price': '8.72'},
           '113521': {'bond_name': '科森转债 ', 'stock_name': '科森科技', 'bond_code': '113521', 'stock_code': '603626',
                      'trans_price': '8.70'},

           '128050': {'bond_name': '钧达转债', 'stock_name': '钧达股份', 'bond_code': '128050', 'stock_code': '002865',
                      'trans_price': '14.83'},
           '113553': {'bond_name': '金牌转债 ', 'stock_name': '金牌厨柜', 'bond_code': '113553', 'stock_code': '603180',
                      'trans_price': '44.14'},
           '113578': {'bond_name': '全筑转债', 'stock_name': '全筑股份', 'bond_code': '113578', 'stock_code': '603030',
                      'trans_price': '5.43'},
           '128079': {'bond_name': '英联转债', 'stock_name': '英联股份', 'bond_code': '128079', 'stock_code': '002846',
                      'trans_price': '13.41'},
           '123045': {'bond_name': '雷迪转债', 'stock_name': '雷迪克', 'bond_code': '123045', 'stock_code': '300652',
                      'trans_price': '20.13'},
           '132018': {'bond_name': 'G三峡EB1', 'stock_name': '长江电力R', 'bond_code': '132018', 'stock_code': '600900',
                      'trans_price': '17.44'},
           '113583': {'bond_name': '益丰转债', 'stock_name': '益丰药房R', 'bond_code': '113583', 'stock_code': '603939',
                      'trans_price': '71.82'},
           '123043': {'bond_name': '正元转债', 'stock_name': '正元智慧', 'bond_code': '123043', 'stock_code': '300645',
                      'trans_price': '15.41'},
           '110066': {'bond_name': '盛屯转债', 'stock_name': '盛屯矿业R', 'bond_code': '110066', 'stock_code': '600711',
                      'trans_price': '4.88'},
           '110069': {'bond_name': '瀚蓝转债', 'stock_name': '瀚蓝环境R', 'bond_code': '110069', 'stock_code': '600323',
                      'trans_price': '20.20'},
           '113590': {'bond_name': '海容转债', 'stock_name': '海容冷链', 'bond_code': '113590', 'stock_code': '603187',
                      'trans_price': '36.39'},
           '128066': {'bond_name': '亚泰转债', 'stock_name': '郑中设计', 'bond_code': '128066', 'stock_code': '002811',
                      'trans_price': '9.67'},
           '132021': {'bond_name': '19中电EBQ', 'stock_name': '中国软件R', 'bond_code': '132021', 'stock_code': '600536',
                      'trans_price': '74.21'},
           '128013': {'bond_name': '洪涛转债', 'stock_name': '洪涛股份R', 'bond_code': '128013', 'stock_code': '002325',
                      'trans_price': '3.10'},
           '123054': {'bond_name': '思特转债', 'stock_name': '思特奇', 'bond_code': '123054', 'stock_code': '300608',
                      'trans_price': '16.49'},
           '113027': {'bond_name': '华钰转债 ', 'stock_name': '华钰矿业R', 'bond_code': '113027', 'stock_code': '601020',
                      'trans_price': '10.17'},
           '120003': {'bond_name': '19华菱EBQ', 'stock_name': '华菱钢铁R', 'bond_code': '120003', 'stock_code': '000932',
                      'trans_price': '4.68'},
           '128096': {'bond_name': '奥瑞转债', 'stock_name': '奥瑞金R', 'bond_code': '128096', 'stock_code': '002701',
                      'trans_price': '4.64'},
           '123061': {'bond_name': '航新转债', 'stock_name': '航新科技', 'bond_code': '123061', 'stock_code': '300424',
                      'trans_price': '14.86'},
           '128021': {'bond_name': '兄弟转债', 'stock_name': '兄弟科技', 'bond_code': '128021', 'stock_code': '002562',
                      'trans_price': '5.25'},
           '113598': {'bond_name': '法兰转债', 'stock_name': '法兰泰克', 'bond_code': '113598', 'stock_code': '603966',
                      'trans_price': '13.88'},
           '113008': {'bond_name': '电气转债', 'stock_name': '上海电气R', 'bond_code': '113008', 'stock_code': '601727',
                      'trans_price': '5.13'},
           '128043': {'bond_name': '东音转债', 'stock_name': '罗欣药业', 'bond_code': '128043', 'stock_code': '002793',
                      'trans_price': '6.22'},
           '113556': {'bond_name': '至纯转债 ', 'stock_name': '至纯科技', 'bond_code': '113556', 'stock_code': '603690',
                      'trans_price': '29.37'},
           '128056': {'bond_name': '今飞转债', 'stock_name': '今飞凯达', 'bond_code': '128056', 'stock_code': '002863',
                      'trans_price': '6.76'},
           '123028': {'bond_name': '清水转债', 'stock_name': '清水源', 'bond_code': '123028', 'stock_code': '300437',
                      'trans_price': '11.84'},
           '123018': {'bond_name': '溢利转债', 'stock_name': '溢多利', 'bond_code': '123018', 'stock_code': '300381',
                      'trans_price': '8.29'},
           '123057': {'bond_name': '美联转债', 'stock_name': '美联新材', 'bond_code': '123057', 'stock_code': '300586',
                      'trans_price': '9.91'},
           '128019': {'bond_name': '久立转2', 'stock_name': '久立特材R', 'bond_code': '128019', 'stock_code': '002318',
                      'trans_price': '7.62'},
           '128095': {'bond_name': '恩捷转债', 'stock_name': '恩捷股份R', 'bond_code': '128095', 'stock_code': '002812',
                      'trans_price': '65.09'},
           '127019': {'bond_name': '国城转债', 'stock_name': '国城矿业', 'bond_code': '127019', 'stock_code': '000688',
                      'trans_price': '21.07'},
           '123010': {'bond_name': '博世转债', 'stock_name': '博世科', 'bond_code': '123010', 'stock_code': '300422',
                      'trans_price': '12.20'},
           '123035': {'bond_name': '利德转债', 'stock_name': '利亚德R', 'bond_code': '123035', 'stock_code': '300296',
                      'trans_price': '6.98'},
           '128051': {'bond_name': '光华转债', 'stock_name': '光华科技', 'bond_code': '128051', 'stock_code': '002741',
                      'trans_price': '12.72'},
           '123012': {'bond_name': '万顺转债', 'stock_name': '万顺新材', 'bond_code': '123012', 'stock_code': '300057',
                      'trans_price': '5.31'},
           '110055': {'bond_name': '伊力转债', 'stock_name': '伊力特R', 'bond_code': '110055', 'stock_code': '600197',
                      'trans_price': '16.81'},
           '128039': {'bond_name': '三力转债', 'stock_name': '三力士', 'bond_code': '128039', 'stock_code': '002224',
                      'trans_price': '5.81'},
           '128119': {'bond_name': '龙大转债', 'stock_name': '龙大肉食R', 'bond_code': '128119', 'stock_code': '002726',
                      'trans_price': '9.56'},
           '128082': {'bond_name': '华锋转债', 'stock_name': '华锋股份', 'bond_code': '128082', 'stock_code': '002806',
                      'trans_price': '11.71'},
           '128090': {'bond_name': '汽模转2', 'stock_name': '天汽模', 'bond_code': '128090', 'stock_code': '002510',
                      'trans_price': '4.21'},
           '128114': {'bond_name': '正邦转债', 'stock_name': '正邦科技R', 'bond_code': '128114', 'stock_code': '002157',
                      'trans_price': '16.09'},
           '128106': {'bond_name': '华统转债', 'stock_name': '华统股份', 'bond_code': '128106', 'stock_code': '002840',
                      'trans_price': '9.39'},
           '110060': {'bond_name': '天路转债 ', 'stock_name': '西藏天路R', 'bond_code': '110060', 'stock_code': '600326',
                      'trans_price': '7.16'},
           '123055': {'bond_name': '晨光转债', 'stock_name': '晨光生物', 'bond_code': '123055', 'stock_code': '300138',
                      'trans_price': '12.25'},
           '128074': {'bond_name': '游族转债', 'stock_name': '游族网络R', 'bond_code': '128074', 'stock_code': '002174',
                      'trans_price': '16.97'},
           '123023': {'bond_name': '迪森转债', 'stock_name': '迪森股份', 'bond_code': '123023', 'stock_code': '300335',
                      'trans_price': '7.04'},
           '113570': {'bond_name': '百达转债', 'stock_name': '百达精工', 'bond_code': '113570', 'stock_code': '603331',
                      'trans_price': '11.54'},
           '128030': {'bond_name': '天康转债', 'stock_name': '天康生物R', 'bond_code': '128030', 'stock_code': '002100',
                      'trans_price': '7.85'},
           '128022': {'bond_name': '众信转债', 'stock_name': '众信旅游', 'bond_code': '128022', 'stock_code': '002707',
                      'trans_price': '7.91'},
           '113525': {'bond_name': '台华转债', 'stock_name': '台华新材', 'bond_code': '113525', 'stock_code': '603055',
                      'trans_price': '8.03'},
           '120004': {'bond_name': '20华菱EBQ', 'stock_name': '华菱钢铁R', 'bond_code': '120004', 'stock_code': '000932',
                      'trans_price': '5.13'},
           '113034': {'bond_name': '滨化转债', 'stock_name': '滨化股份R', 'bond_code': '113034', 'stock_code': '601678',
                      'trans_price': '4.68'},
           '113567': {'bond_name': '君禾转债', 'stock_name': '君禾股份', 'bond_code': '113567', 'stock_code': '603617',
                      'trans_price': '11.46'},
           '110065': {'bond_name': '淮矿转债', 'stock_name': '淮北矿业', 'bond_code': '110065', 'stock_code': '600985',
                      'trans_price': '9.33'},
           '113545': {'bond_name': '金能转债', 'stock_name': '金能科技R', 'bond_code': '113545', 'stock_code': '603113',
                      'trans_price': '11.40'},
           '128094': {'bond_name': '星帅转债', 'stock_name': '星帅尔', 'bond_code': '128094', 'stock_code': '002860',
                      'trans_price': '13.95'},
           '113557': {'bond_name': '森特转债', 'stock_name': '森特股份', 'bond_code': '113557', 'stock_code': '603098',
                      'trans_price': '10.11'},
           '110071': {'bond_name': '湖盐转债', 'stock_name': '湖南盐业R', 'bond_code': '110071', 'stock_code': '600929',
                      'trans_price': '6.60'},
           '128046': {'bond_name': '利尔转债', 'stock_name': '利尔化学R', 'bond_code': '128046', 'stock_code': '002258',
                      'trans_price': '18.62'},
           '113029': {'bond_name': '明阳转债', 'stock_name': '明阳智能R', 'bond_code': '113029', 'stock_code': '601615',
                      'trans_price': '12.46'},
           '113576': {'bond_name': '起步转债', 'stock_name': '起步股份', 'bond_code': '113576', 'stock_code': '603557',
                      'trans_price': '10.55'},
           '113546': {'bond_name': '迪贝转债', 'stock_name': '迪贝电气', 'bond_code': '113546', 'stock_code': '603320',
                      'trans_price': '14.10'},
           '113568': {'bond_name': '新春转债', 'stock_name': '五洲新春', 'bond_code': '113568', 'stock_code': '603667',
                      'trans_price': '8.91'},
           '128107': {'bond_name': '交科转债', 'stock_name': '浙江交科', 'bond_code': '128107', 'stock_code': '002061',
                      'trans_price': '5.36'},
           '128085': {'bond_name': '鸿达转债', 'stock_name': '鸿达兴业R', 'bond_code': '128085', 'stock_code': '002002',
                      'trans_price': '3.92'},
           '127005': {'bond_name': '长证转债', 'stock_name': '长江证券R', 'bond_code': '127005', 'stock_code': '000783',
                      'trans_price': '7.28'},
           '123025': {'bond_name': '精测转债 ', 'stock_name': '精测电子R', 'bond_code': '123025', 'stock_code': '300567',
                      'trans_price': '49.95'},
           '113038': {'bond_name': '隆20转债', 'stock_name': '隆基股份R', 'bond_code': '113038', 'stock_code': '601012',
                      'trans_price': '52.77'},
           '113542': {'bond_name': '好客转债', 'stock_name': '好莱客', 'bond_code': '113542', 'stock_code': '603898',
                      'trans_price': '16.27'},
           '123014': {'bond_name': '凯发转债', 'stock_name': '凯发电气', 'bond_code': '123014', 'stock_code': '300407',
                      'trans_price': '8.12'},
           '113549': {'bond_name': '白电转债', 'stock_name': '白云电器', 'bond_code': '113549', 'stock_code': '603861',
                      'trans_price': '8.88'},
           '128125': {'bond_name': '华阳转债', 'stock_name': '华阳国际', 'bond_code': '128125', 'stock_code': '002949',
                      'trans_price': '25.79'},
           '128069': {'bond_name': '华森转债', 'stock_name': '华森制药', 'bond_code': '128069', 'stock_code': '002907',
                      'trans_price': '18.04'},
           '110051': {'bond_name': '中天转债', 'stock_name': '中天科技R', 'bond_code': '110051', 'stock_code': '600522',
                      'trans_price': '10.09'},
           '123017': {'bond_name': '寒锐转债 ', 'stock_name': '寒锐钴业R', 'bond_code': '123017', 'stock_code': '300618',
                      'trans_price': '57.40'},
           '113562': {'bond_name': '璞泰转债', 'stock_name': '璞泰来R', 'bond_code': '113562', 'stock_code': '603659',
                      'trans_price': '82.73'},
           '113032': {'bond_name': '桐20转债', 'stock_name': '桐昆股份R', 'bond_code': '113032', 'stock_code': '601233',
                      'trans_price': '14.35'},
           '110056': {'bond_name': '亨通转债', 'stock_name': '亨通光电R', 'bond_code': '110056', 'stock_code': '600487',
                      'trans_price': '15.58'},
           '128110': {'bond_name': '永兴转债', 'stock_name': '永兴材料', 'bond_code': '128110', 'stock_code': '002756',
                      'trans_price': '17.16'},
           '128109': {'bond_name': '楚江转债', 'stock_name': '楚江新材R', 'bond_code': '128109', 'stock_code': '002171',
                      'trans_price': '8.73'},
           '128028': {'bond_name': '赣锋转债', 'stock_name': '赣锋锂业R', 'bond_code': '128028', 'stock_code': '002460',
                      'trans_price': '41.98'},
           '128025': {'bond_name': '特一转债', 'stock_name': '特一药业', 'bond_code': '128025', 'stock_code': '002728',
                      'trans_price': '14.70'},
           '113033': {'bond_name': '利群转债', 'stock_name': '利群股份', 'bond_code': '113033', 'stock_code': '601366',
                      'trans_price': '7.01'},
           '128111': {'bond_name': '中矿转债', 'stock_name': '中矿资源', 'bond_code': '128111', 'stock_code': '002738',
                      'trans_price': '15.53'},
           '123058': {'bond_name': '欣旺转债', 'stock_name': '欣旺达R', 'bond_code': '123058', 'stock_code': '300207',
                      'trans_price': '21.28'},
           '123042': {'bond_name': '银河转债', 'stock_name': '金银河', 'bond_code': '123042', 'stock_code': '300619',
                      'trans_price': '24.40'},
           '110033': {'bond_name': '国贸转债', 'stock_name': '厦门国贸R', 'bond_code': '110033', 'stock_code': '600755',
                      'trans_price': '7.19'},
           '110057': {'bond_name': '现代转债', 'stock_name': '现代制药', 'bond_code': '110057', 'stock_code': '600420',
                      'trans_price': '9.89'},
           '128117': {'bond_name': '道恩转债', 'stock_name': '道恩股份R', 'bond_code': '128117', 'stock_code': '002838',
                      'trans_price': '29.32'},
           '123053': {'bond_name': '宝通转债', 'stock_name': '宝通科技', 'bond_code': '123053', 'stock_code': '300031',
                      'trans_price': '20.80'},
           '127017': {'bond_name': '万青转债', 'stock_name': '万年青R', 'bond_code': '127017', 'stock_code': '000789',
                      'trans_price': '14.16'},
           '110038': {'bond_name': '济川转债', 'stock_name': '济川药业R', 'bond_code': '110038', 'stock_code': '600566',
                      'trans_price': '24.27'},
           '113036': {'bond_name': '宁建转债', 'stock_name': '宁波建工R', 'bond_code': '113036', 'stock_code': '601789',
                      'trans_price': '4.86'},
           '128103': {'bond_name': '同德转债', 'stock_name': '同德化工', 'bond_code': '128103', 'stock_code': '002360',
                      'trans_price': '5.18'},
           '110041': {'bond_name': '蒙电转债', 'stock_name': '内蒙华电R', 'bond_code': '110041', 'stock_code': '600863',
                      'trans_price': '2.69'},
           '128048': {'bond_name': '张行转债', 'stock_name': '张家港行R', 'bond_code': '128048', 'stock_code': '002839',
                      'trans_price': '5.76'},
           '127007': {'bond_name': '湖广转债', 'stock_name': '湖北广电R', 'bond_code': '127007', 'stock_code': '000665',
                      'trans_price': '5.58'},
           '110068': {'bond_name': '龙净转债', 'stock_name': '龙净环保R', 'bond_code': '110068', 'stock_code': '600388',
                      'trans_price': '10.73'},
           '113591': {'bond_name': '胜达转债', 'stock_name': '大胜达', 'bond_code': '113591', 'stock_code': '603687',
                      'trans_price': '14.73'},
           '128065': {'bond_name': '雅化转债', 'stock_name': '雅化集团R', 'bond_code': '128065', 'stock_code': '002497',
                      'trans_price': '8.95'},
           '128120': {'bond_name': '联诚转债', 'stock_name': '联诚精密', 'bond_code': '128120', 'stock_code': '002921',
                      'trans_price': '24.37'},
           '128036': {'bond_name': '金农转债', 'stock_name': '金新农R', 'bond_code': '128036', 'stock_code': '002548',
                      'trans_price': '7.39'},
           '123033': {'bond_name': '金力转债', 'stock_name': '金力永磁R', 'bond_code': '123033', 'stock_code': '300748',
                      'trans_price': '41.09'},
           '128053': {'bond_name': '尚荣转债', 'stock_name': '尚荣医疗', 'bond_code': '128053', 'stock_code': '002551',
                      'trans_price': '4.89'},
           '127020': {'bond_name': '中金转债', 'stock_name': '中金岭南R', 'bond_code': '127020', 'stock_code': '000060',
                      'trans_price': '4.71'},
           '110061': {'bond_name': '川投转债', 'stock_name': '川投能源R', 'bond_code': '110061', 'stock_code': '600674',
                      'trans_price': '9.58'},
           '110063': {'bond_name': '鹰19转债', 'stock_name': '山鹰纸业R', 'bond_code': '110063', 'stock_code': '600567',
                      'trans_price': '3.30'},
           '128034': {'bond_name': '江银转债', 'stock_name': '江阴银行', 'bond_code': '128034', 'stock_code': '002807',
                      'trans_price': '4.50'},
           '110048': {'bond_name': '福能转债', 'stock_name': '福能股份R', 'bond_code': '110048', 'stock_code': '600483',
                      'trans_price': '8.12'},
           '128113': {'bond_name': '比音转债', 'stock_name': '比音勒芬', 'bond_code': '128113', 'stock_code': '002832',
                      'trans_price': '14.90'},
           '113579': {'bond_name': '健友转债', 'stock_name': '健友股份R', 'bond_code': '113579', 'stock_code': '603707',
                      'trans_price': '42.05'},
           '128116': {'bond_name': '瑞达转债', 'stock_name': '瑞达期货', 'bond_code': '128116', 'stock_code': '002961',
                      'trans_price': '29.82'},
           '123007': {'bond_name': '道氏转债', 'stock_name': '道氏技术', 'bond_code': '123007', 'stock_code': '300409',
                      'trans_price': '14.95'},
           '110073': {'bond_name': '国投转债', 'stock_name': '国投资本R', 'bond_code': '110073', 'stock_code': '600061',
                      'trans_price': '15.25'},
           '128118': {'bond_name': '瀛通转债', 'stock_name': '瀛通通讯', 'bond_code': '128118', 'stock_code': '002861',
                      'trans_price': '27.53'},
           '113559': {'bond_name': '永创转债', 'stock_name': '永创智能', 'bond_code': '113559', 'stock_code': '603901',
                      'trans_price': '10.32'},
           '110043': {'bond_name': '无锡转债', 'stock_name': '无锡银行', 'bond_code': '110043', 'stock_code': '600908',
                      'trans_price': '5.79'},
           '110052': {'bond_name': '贵广转债', 'stock_name': '贵广网络R', 'bond_code': '110052', 'stock_code': '600996',
                      'trans_price': '7.94'},
           '113025': {'bond_name': '明泰转债', 'stock_name': '明泰铝业', 'bond_code': '113025', 'stock_code': '601677',
                      'trans_price': '11.20'},
           '113030': {'bond_name': '东风转债', 'stock_name': '东风股份R', 'bond_code': '113030', 'stock_code': '601515',
                      'trans_price': '6.75'},
           '113588': {'bond_name': '润达转债', 'stock_name': '润达医疗R', 'bond_code': '113588', 'stock_code': '603108',
                      'trans_price': '13.36'},
           '123024': {'bond_name': '岱勒转债', 'stock_name': '岱勒新材', 'bond_code': '123024', 'stock_code': '300700',
                      'trans_price': '24.90'},
           '113011': {'bond_name': '光大转债', 'stock_name': '光大银行R', 'bond_code': '113011', 'stock_code': '601818',
                      'trans_price': '3.76'},
           '110064': {'bond_name': '建工转债', 'stock_name': '重庆建工', 'bond_code': '110064', 'stock_code': '600939',
                      'trans_price': '4.57'},
           '128093': {'bond_name': '百川转债', 'stock_name': '百川股份', 'bond_code': '128093', 'stock_code': '002455',
                      'trans_price': '5.87'},
           '128040': {'bond_name': '华通转债', 'stock_name': '华通医药', 'bond_code': '128040', 'stock_code': '002758',
                      'trans_price': '11.29'},
           '128070': {'bond_name': '智能转债', 'stock_name': '智能自控', 'bond_code': '128070', 'stock_code': '002877',
                      'trans_price': '9.51'},
           '110047': {'bond_name': '山鹰转债', 'stock_name': '山鹰纸业R', 'bond_code': '110047', 'stock_code': '600567',
                      'trans_price': '3.34'},
           '128076': {'bond_name': '金轮转债', 'stock_name': '金轮股份', 'bond_code': '128076', 'stock_code': '002722',
                      'trans_price': '14.76'},
           '113563': {'bond_name': '柳药转债', 'stock_name': '柳药股份R', 'bond_code': '113563', 'stock_code': '603368',
                      'trans_price': '24.47'},
           '123036': {'bond_name': '先导转债', 'stock_name': '先导智能R', 'bond_code': '123036', 'stock_code': '300450',
                      'trans_price': '38.99'},
           '113526': {'bond_name': '联泰转债 ', 'stock_name': '联泰环保', 'bond_code': '113526', 'stock_code': '603797',
                      'trans_price': '6.11'},
           '132005': {'bond_name': '15国资EB', 'stock_name': '中国太保R', 'bond_code': '132005', 'stock_code': '601601',
                      'trans_price': '33.90'},
           '110070': {'bond_name': '凌钢转债', 'stock_name': '凌钢股份R', 'bond_code': '110070', 'stock_code': '600231',
                      'trans_price': '2.75'},
           '113519': {'bond_name': '长久转债', 'stock_name': '长久物流', 'bond_code': '113519', 'stock_code': '603569',
                      'trans_price': '11.15'},
           '127013': {'bond_name': '创维转债', 'stock_name': '创维数字R', 'bond_code': '127013', 'stock_code': '000810',
                      'trans_price': '11.39'},
           '123060': {'bond_name': '苏试转债', 'stock_name': '苏试试验', 'bond_code': '123060', 'stock_code': '300416',
                      'trans_price': '23.86'},
           '113037': {'bond_name': '紫银转债', 'stock_name': '紫金银行R', 'bond_code': '113037', 'stock_code': '601860',
                      'trans_price': '4.75'},
           '113534': {'bond_name': '鼎胜转债', 'stock_name': '鼎胜新材', 'bond_code': '113534', 'stock_code': '603876',
                      'trans_price': '15.18'},
           '128123': {'bond_name': '国光转债', 'stock_name': '国光股份', 'bond_code': '128123', 'stock_code': '002749',
                      'trans_price': '13.70'},
           '123031': {'bond_name': '晶瑞转债 ', 'stock_name': '晶瑞股份', 'bond_code': '123031', 'stock_code': '300655',
                      'trans_price': '18.53'},
           '113013': {'bond_name': '国君转债', 'stock_name': '国泰君安R', 'bond_code': '113013', 'stock_code': '601211',
                      'trans_price': '19.01'},
           '113532': {'bond_name': '海环转债', 'stock_name': '海峡环保', 'bond_code': '113532', 'stock_code': '603817',
                      'trans_price': '7.69'},
           '128081': {'bond_name': '海亮转债', 'stock_name': '海亮股份R', 'bond_code': '128081', 'stock_code': '002203',
                      'trans_price': '9.76'},
           '113593': {'bond_name': '沪工转债', 'stock_name': '上海沪工', 'bond_code': '113593', 'stock_code': '603131',
                      'trans_price': '21.32'},
           '110067': {'bond_name': '华安转债', 'stock_name': '华安证券R', 'bond_code': '110067', 'stock_code': '600909',
                      'trans_price': '8.67'},
           '128063': {'bond_name': '未来转债', 'stock_name': '德尔未来R', 'bond_code': '128063', 'stock_code': '002631',
                      'trans_price': '8.61'},
           '110034': {'bond_name': '九州转债', 'stock_name': '九州通R', 'bond_code': '110034', 'stock_code': '600998',
                      'trans_price': '18.32'},
           '127016': {'bond_name': '鲁泰转债', 'stock_name': '鲁泰AR', 'bond_code': '127016', 'stock_code': '000726',
                      'trans_price': '8.91'},
           '113516': {'bond_name': '苏农转债', 'stock_name': '苏农银行R', 'bond_code': '113516', 'stock_code': '603323',
                      'trans_price': '5.52'},
           '128042': {'bond_name': '凯中转债', 'stock_name': '凯中精密', 'bond_code': '128042', 'stock_code': '002823',
                      'trans_price': '12.94'},
           '110053': {'bond_name': '苏银转债', 'stock_name': '江苏银行R', 'bond_code': '110053', 'stock_code': '600919',
                      'trans_price': '7.28'},
           '128091': {'bond_name': '新天转债', 'stock_name': '新天药业', 'bond_code': '128091', 'stock_code': '002873',
                      'trans_price': '16.39'},
           '128083': {'bond_name': '新北转债', 'stock_name': '新北洋R', 'bond_code': '128083', 'stock_code': '002376',
                      'trans_price': '11.70'},
           '127006': {'bond_name': '敖东转债', 'stock_name': '吉林敖东R', 'bond_code': '127006', 'stock_code': '000623',
                      'trans_price': '20.42'},
           '127014': {'bond_name': '北方转债', 'stock_name': '北方国际', 'bond_code': '127014', 'stock_code': '000065',
                      'trans_price': '8.75'},
           '123039': {'bond_name': '开润转债', 'stock_name': '开润股份', 'bond_code': '123039', 'stock_code': '300577',
                      'trans_price': '33.22'},
           '113528': {'bond_name': '长城转债', 'stock_name': '长城科技', 'bond_code': '113528', 'stock_code': '603897',
                      'trans_price': '23.75'},
           '128087': {'bond_name': '孚日转债', 'stock_name': '孚日股份', 'bond_code': '128087', 'stock_code': '002083',
                      'trans_price': '6.30'},
           '110062': {'bond_name': '烽火转债', 'stock_name': '烽火通信R', 'bond_code': '110062', 'stock_code': '600498',
                      'trans_price': '25.65'},
           '113594': {'bond_name': '淳中转债', 'stock_name': '淳中科技', 'bond_code': '113594', 'stock_code': '603516',
                      'trans_price': '39.37'},
           '113017': {'bond_name': '吉视转债', 'stock_name': '吉视传媒R', 'bond_code': '113017', 'stock_code': '601929',
                      'trans_price': '2.95'},
           '113505': {'bond_name': '杭电转债', 'stock_name': '杭电股份R', 'bond_code': '113505', 'stock_code': '603618',
                      'trans_price': '7.14'},
           '128121': {'bond_name': '宏川转债', 'stock_name': '宏川智慧', 'bond_code': '128121', 'stock_code': '002930',
                      'trans_price': '20.25'},
           '113524': {'bond_name': '奇精转债', 'stock_name': '奇精机械', 'bond_code': '113524', 'stock_code': '603677',
                      'trans_price': '14.28'},
           '128018': {'bond_name': '时达转债', 'stock_name': '新时达', 'bond_code': '128018', 'stock_code': '002527',
                      'trans_price': '7.42'}
           }

THS_iFinDLogin("jztz093", "165805")


def get_data():
    str_code = ""
    for i in my_dict.keys():
        stock_code = my_dict[i]["stock_code"]
        if i[:2] == "11":
            i += ".SH"
            stock_code += ".SH"
        if i[:2] == "12":
            i += ".SZ"
            stock_code += ".SZ"
        str_code += i + "," + stock_code + ","
    # 请求同花顺
    result = json.loads(THS_RealtimeQuotes(str_code, 'latest;changeRatio;', 'pricetype:2', True))["tables"]
    r = {}
    for i in range(len(result)):
        _code = result[i]["thscode"]
        _time = result[i]["time"][0]
        _latest = result[i]["table"]["latest"][0]
        _changeRatio = result[i]["table"]["changeRatio"][0]
        r[_code] = {"time": _time, "latest": _latest, "changeRatio": _changeRatio}
    return r


def get_premium_rt():
    r = get_data()
    result_list = []
    for k, v in r.items():
        tail = k.split(".")[1]
        if k.strip(".SH").strip(".SZ") not in my_dict.keys():
            continue
        else:
            bond_price = r[k]["latest"]
            stock_code = my_dict[k.strip(".SH").strip(".SZ")]["stock_code"]
            stock_price = r[stock_code + "." + tail]["latest"]
            stock_changeRatio = r[stock_code + "." + tail]["changeRatio"]
            bond_changeRatio = r[k]["changeRatio"]
            trans_price = my_dict[k.strip(".SH").strip(".SZ")]["trans_price"]
            bond_name = my_dict[k.strip(".SH").strip(".SZ")]["bond_name"]
            premium_rate = trans(stock_price, bond_price, trans_price)
            result_list.append(
                {"bond_price": bond_price, "bond_code": k, "bond_name": bond_name, "premium_rate": premium_rate,
                 "stock_changeRatio": stock_changeRatio, "bond_changeRatio": bond_changeRatio})
    return result_list


def trans(p1, p2, convertible_share_price):
    """
    :param p1: 股票价格
    :param p2: 可转债价格
    :param convertible_share_price: 转股价格
    :return:
    """
    return float(p2) / (100 / float(convertible_share_price) * float(p1)) - 1


class Window(tk.Tk):
    """窗口类"""

    def __init__(self, wait_time=1000, *args, **kw):
        super().__init__()
        self.wm_title('提醒')
        self.configure(background='white')
        self.wm_minsize(360, 260)  # 设置窗口最小化大小
        self.wm_maxsize(4880, 2600)  # 设置窗口最大化大小
        self.resizable(width=True, height=True)  # 设置窗口宽度不可变，高度可变
        self.var1 = tk.StringVar()  # 文本储存器
        self.var2 = tk.StringVar()  # 文本储存器
        self.var3 = tk.StringVar()  # 文本储存器
        self.var4 = tk.StringVar()  # 文本储存器

        self.l1 = MyLabel2(height=2, width=150)
        self.l2 = MyLabel2(height=2, width=150)
        self.l3 = MyLabel2(height=2, width=150)
        self.l4 = MyLabel2(height=2, width=150)
        self.l_list = [self.l1, self.l2, self.l3, self.l4]
        self.refresh_data(wait_time)
        self.mainloop()

    def refresh_data(self, wait_time=1000):
        # 需要刷新数据的操作
        # 代码...
        # {'113581.SH': {'bond_name': '龙蟠转债', 'premium_rate': -0.1172043085441542}, '123063.SZ': {'bond_name': '大禹转债', 'premium_rate': -0.08589065112212024}}
        data = get_premium_rt()
        data = sorted(data, key=lambda x: x["premium_rate"])
        self.after(wait_time, self.refresh_data)  # 这里的10000单位为毫秒
        for i in range(4):
            bond_code = data[i]["bond_code"]
            bond_name = data[i]["bond_name"]
            premium_rate = data[i]["premium_rate"]
            bond_changeRatio = data[i]["bond_changeRatio"]
            stock_changeRatio = data[i]["stock_changeRatio"]
            bond_price = data[i]["bond_price"]
            self.l_list[i].set(bond_code + bond_name + "溢价率:" + str(premium_rate)+"")
            self.l_list[i].set(bond_code+bond_name+"溢价率："+(str(100*premium_rate))[:6]+"%"+"转债涨跌："+(str(bond_changeRatio))[:4]+"%"+"正股涨跌："+(str(stock_changeRatio))[:4]+"%"+"转债价格："+str(bond_price)[:6])
            if premium_rate < -0.01:

                self.l_list[i].bg("red")
            else:
                self.l_list[i].bg("white")


if __name__ == '__main__':
    aa = Window()
    aa.refresh_data()