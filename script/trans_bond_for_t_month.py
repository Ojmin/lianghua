import time

from EmQuantAPI import *
import datetime
import matplotlib.pyplot as plt
from matplotlib import ticker

c.start()

c.start()
data = {
    "113031": {'cd': '2020-8-5', 'name': '博威转债', "stock_id": "sh601137", "stock_nm": "博威合金"},
    '113550': {'cd': '2020-05-22', 'name': '常汽转债', 'stock_id': 'sh603035', 'stock_nm': '常熟汽饰'},
    "123041": {'cd': '2020-8-6', 'name': '东财转2', "stock_id": "sz300059", 'stock_nm': '东方财富'},
    '128043': {'cd': '2019-02-11', 'name': '东音转债', 'stock_id': 'sz002793', 'stock_nm': '罗欣药业'},
    "123020": {'cd': '2020-8-3', 'name': '富祥转债', "stock_id": "sz300497", 'stock_nm': '富祥药业'},
    "113518": {'cd': '2020-8-6', 'name': '顾家转债', "stock_id": "sh603816", "stock_nm": "顾家家居"},
    "128086": {'cd': '2020-8-6', 'name': '国轩转债', "stock_id": "sz002074", 'stock_nm': "国轩高科"},
    '113027': {'cd': '2019-12-20', 'name': '华钰转债', 'stock_id': 'sh601020', 'stock_nm': '华钰矿业'},
    "128045": {'cd': '2020-8-3', 'name': '机电转债', "stock_id": "sz002013", 'stock_nm': '中航机电'},  # 中航机电
    '123030': {'cd': '2020-02-27', 'name': '九洲转债', 'stock_id': 'sz300040', 'stock_nm': '九洲集团'},
    "113552": {'cd': '2020-8-4', 'name': '克来转债', "stock_id": "sh603960", 'stock_nm': '克来机电'},
    '123027': {'cd': '2019-12-17', 'name': '蓝晓转债', 'stock_id': 'sz300487', 'stock_nm': '蓝晓科技'},
    "123022": {'cd': '2020-8-3', 'name': '乐普转债', "stock_id": "sz300003", 'stock_nm': '乐普医疗'},
    "128089": {'cd': '2020-8-4', 'name': '麦米转债', "stock_id": "sz002851", 'stock_nm': '麦格米特'},
    '128084': {'cd': '2020-06-22', 'name': '木森转债', 'stock_id': 'sz002745', 'stock_nm': '木林森'},
    '113543': {'cd': '2020-02-24', 'name': '欧派转债', 'stock_id': 'sh603833', 'stock_nm': '欧派家居'},
    "113558": {'cd': '2020-8-3', 'name': '日月转债', "stock_id": "sh603218", 'stock_nm': '日月股份'},
    '113536': {'cd': '2019-12-06', 'name': '三星转债', 'stock_id': 'sh603578', 'stock_nm': '三星新材'},
    "128088": {"cd": "2020-8-3", 'name': '深南转债', "stock_id": "sz002916", "stock_nm": '深南电路'},
    "128059": {"cd": "2020-8-10", 'name': '视源转债', "stock_id": "sz002841", "stock_nm": '视源股份'},
    '128078': {'cd': '2020-04-27', 'name': '太极转债', 'stock_id': 'sz002368', 'stock_nm': '太极股份'},
    '128092': {'cd': '2020-07-06', 'name': '唐人转债', 'stock_id': 'sz002567', 'stock_nm': '唐人神'},
    '110060': {'cd': '2020-05-06', 'name': '天路转债', 'stock_id': 'sh600326', 'stock_nm': '西藏天路'},
    "113514": {"cd": "2020-8-3", 'name': '威帝转债', "stock_id": "sh603023", 'stock_nm': '威帝股份'},
    '113554': {'cd': '2020-06-22', 'name': '仙鹤转债', 'stock_id': 'sh603733', 'stock_nm': '仙鹤股份'},
    "113022": {"cd": "2020-8-5", 'name': '浙商转债', "stock_id": "sh601878", 'stock_nm': '浙商证券'},
    '113555': {'cd': '2020-06-29', 'name': '振德转债', 'stock_id': 'sh603301', 'stock_nm': '振德医疗'},
    '123026': {'cd': '2019-12-16', 'name': '中环转债', 'stock_id': 'sz300692', 'stock_nm': '中环环保'},
    
    # '128128': {'cd': '2021-02-26', 'name': '齐翔转2', 'stock_id': 'sz002408', 'stock_nm': '齐翔腾达'},
    #         '113581': {'cd': '2020-10-29', 'name': '龙蟠转债', 'stock_id': 'sh603906', 'stock_nm': '龙蟠科技'},
    #         '113575': {'cd': '2020-10-15', 'name': '东时转债', 'stock_id': 'sh603377', 'stock_nm': '东方时尚'},
    #         '128130': {'cd': '2021-03-04', 'name': '景兴转债', 'stock_id': 'sz002067', 'stock_nm': '景兴纸业'},
    #         '113580': {'cd': '2020-10-29', 'name': '康隆转债', 'stock_id': 'sh603665', 'stock_nm': '康隆达'},
    #         '113586': {'cd': '2020-12-15', 'name': '上机转债', 'stock_id': 'sh603185', 'stock_nm': '上机数控'},
    #         '113585': {'cd': '2020-12-15', 'name': '寿仙转债', 'stock_id': 'sh603896', 'stock_nm': '寿仙谷'},
    #         '123051': {'cd': '2020-12-10', 'name': '今天转债', 'stock_id': 'sz300532', 'stock_nm': '今天国际'},
    #         '113571': {'cd': '2020-09-18', 'name': '博特转债', 'stock_id': 'sh603916', 'stock_nm': '苏博特'},
    #         '123046': {'cd': '2020-09-25', 'name': '天铁转债', 'stock_id': 'sz300587', 'stock_nm': '天铁股份'},
    #         '113587': {'cd': '2020-12-21', 'name': '泛微转债', 'stock_id': 'sh603039', 'stock_nm': '泛微网络'},
    #         '128104': {'cd': '2020-10-13', 'name': '裕同转债', 'stock_id': 'sz002831', 'stock_nm': '裕同科技'},
    #         '128102': {'cd': '2020-09-25', 'name': '海大转债', 'stock_id': 'sz002311', 'stock_nm': '海大集团'},
    #         '128115': {'cd': '2021-01-04', 'name': '巨星转债', 'stock_id': 'sz002444', 'stock_nm': '巨星科技'},
    #         '113592': {'cd': '2021-01-14', 'name': '安20转债', 'stock_id': 'sh603345', 'stock_nm': '安井食品'},
    # '123037': {'cd': '2020-06-29', 'name': '新莱转债', 'stock_id': 'sz300260', 'stock_nm': '新莱应材'},
    #     '113572': {'cd': '2020-09-18', 'name': '三祥转债', 'stock_id': 'sh603663', 'stock_nm': '三祥新材'},
    #     '128108': {'cd': '2020-12-03', 'name': '蓝帆转债', 'stock_id': 'sz002382', 'stock_nm': '蓝帆医疗'},
    #     '113544': {'cd': '2020-03-26', 'name': '桃李转债', 'stock_id': 'sh603866', 'stock_nm': '桃李面包'},
    #     '123056': {'cd': '2021-01-04', 'name': '雪榕转债', 'stock_id': 'sz300511', 'stock_nm': '雪榕生物'},
    #     '110058': {'cd': '2019-10-22', 'name': '永鼎转债', 'stock_id': 'sh600105', 'stock_nm': '永鼎股份'},
    #     '128098': {'cd': '2020-09-11', 'name': '康弘转债', 'stock_id': 'sz002773', 'stock_nm': '康弘药业'},
    #     '113509': {'cd': '2018-12-10', 'name': '新泉转债', 'stock_id': 'sh603179', 'stock_nm': '新泉股份'},
    #         '128096': {'cd': '2020-08-17', 'name': '奥瑞转债', 'stock_id': 'sz002701', 'stock_nm': '奥瑞金'},
    #         '113547': {'cd': '2020-04-30', 'name': '索发转债', 'stock_id': 'sh603612', 'stock_nm': '索通发展'},
    #         '113035': {'cd': '2020-12-03', 'name': '福莱转债', 'stock_id': 'sh601865', 'stock_nm': '福莱特'},
    #         '113521': {'cd': '2019-05-22', 'name': '科森转债', 'stock_id': 'sh603626', 'stock_nm': '科森科技'},
    #         '113561': {'cd': '2020-07-07', 'name': '正裕转债', 'stock_id': 'sh603089', 'stock_nm': '正裕工业'},
    #         '113566': {'cd': '2020-09-07', 'name': '翔港转债', 'stock_id': 'sh603499', 'stock_nm': '翔港科技'},
    #         '113564': {'cd': '2020-09-07', 'name': '天目转债', 'stock_id': 'sh603136', 'stock_nm': '天目湖'},
    #         '128097': {'cd': '2020-09-02', 'name': '奥佳转债', 'stock_id': 'sz002614', 'stock_nm': '奥佳华'},
    #         '128067': {'cd': '2019-10-25', 'name': '一心转债', 'stock_id': 'sz002727', 'stock_nm': '一心堂'},
    #         '128017': {'cd': '2018-08-07', 'name': '金禾转债', 'stock_id': 'sz002597', 'stock_nm': '金禾实业'},
    #         '128112': {'cd': '2020-12-18', 'name': '歌尔转2', 'stock_id': 'sz002241', 'stock_nm': '歌尔股份'},
    #         '113601': {'cd': '2021-03-01', 'name': '塞力转债', 'stock_id': 'sh603716', 'stock_nm': '塞力斯'},
    #         '128071': {'cd': '2020-02-24', 'name': '合兴转债', 'stock_id': 'sz002228', 'stock_nm': '合兴包装'},
    #         '113028': {'cd': '2019-12-24', 'name': '环境转债', 'stock_id': 'sh601200', 'stock_nm': '上海环境'},
    #         '127015': {'cd': '2020-07-09', 'name': '希望转债', 'stock_id': 'sz000876', 'stock_nm': '新希望'},
    #         '113565': {'cd': '2020-09-03', 'name': '宏辉转债', 'stock_id': 'sh603336', 'stock_nm': '宏辉果蔬'},
    #         '123022': {'cd': '2019-09-23', 'name': '长信转债', 'stock_id': 'sz300088', 'stock_nm': '长信科技'},
    #         '113599': {'cd': '2021-02-18', 'name': '嘉友转债', 'stock_id': 'sh603871', 'stock_nm': '嘉友国际'},
    #         '123029': {'cd': '2020-02-24', 'name': '英科转债', 'stock_id': 'sz300677', 'stock_nm': '英科医疗'},
    #         '128029': {'cd': '2018-06-28', 'name': '太阳转债', 'stock_id': 'sz002078', 'stock_nm': '太阳纸业'},
    #         '113548': {'cd': '2020-05-06', 'name': '石英转债', 'stock_id': 'sh603688', 'stock_nm': '石英股份'},
    #         '110069': {'cd': '2020-10-13', 'name': '瀚蓝转债', 'stock_id': 'sh600323', 'stock_nm': '瀚蓝环境'},
    #         '128058': {'cd': '2019-09-16', 'name': '拓邦转债', 'stock_id': 'sz002139', 'stock_nm': '拓邦股份'},
    #         '123044': {'cd': '2020-09-18', 'name': '红相转债', 'stock_id': 'sz300427', 'stock_nm': '红相股份'},
    #         '123063': {'cd': '2021-02-03', 'name': '大禹转债', 'stock_id': 'sz300021', 'stock_nm': '大禹节水'},
    #         '110066': {'cd': '2020-09-07', 'name': '盛屯转债', 'stock_id': 'sh600711', 'stock_nm': '盛屯矿业'},
    #         '123052': {'cd': '2020-12-11', 'name': '飞鹿转债', 'stock_id': 'sz300665', 'stock_nm': '飞鹿股份'},
    #         '113537': {'cd': '2019-12-16', 'name': '文灿转债', 'stock_id': 'sh603348', 'stock_nm': '文灿股份'},
    #         '113583': {'cd': '2020-12-07', 'name': '益丰转债', 'stock_id': 'sh603939', 'stock_nm': '益丰药房'},
    #         '110074': {'cd': '2021-02-25', 'name': '精达转债', 'stock_id': 'sh600577', 'stock_nm': '精达股份'},
    #         '113582': {'cd': '2020-12-02', 'name': '火炬转债', 'stock_id': 'sh603678', 'stock_nm': '火炬电子'},
    #         '113504': {'cd': '2018-09-08', 'name': '艾华转债', 'stock_id': 'sh603989', 'stock_nm': '艾华集团'},
    #         '113577': {'cd': '2020-10-20', 'name': '春秋转债', 'stock_id': 'sh603890', 'stock_nm': '春秋电子'},
    #         '113525': {'cd': '2019-06-21', 'name': '台华转债', 'stock_id': 'sh603055', 'stock_nm': '台华新材'},
    #         '128075': {'cd': '2020-03-27', 'name': '远东转债', 'stock_id': 'sz002406', 'stock_nm': '远东传动'},
    #         '128056': {'cd': '2019-09-06', 'name': '今飞转债', 'stock_id': 'sz002863', 'stock_nm': '今飞凯达'},
    #         '113520': {'cd': '2019-05-14', 'name': '百合转债', 'stock_id': 'sh603313', 'stock_nm': '梦百合'},
    #         '113595': {'cd': '2021-01-27', 'name': '花王转债', 'stock_id': 'sh603007', 'stock_nm': '花王股份'},
    #         '123050': {'cd': '2020-10-20', 'name': '聚飞转债', 'stock_id': 'sz300303', 'stock_nm': '聚飞光电'},
    #         '113541': {'cd': '2020-02-03', 'name': '荣晟转债', 'stock_id': 'sh603165', 'stock_nm': '荣晟环保'},
    #         '127003': {'cd': '2016-12-16', 'name': '海印转债', 'stock_id': 'sz000861', 'stock_nm': '海印股份'},
    #         '113590': {'cd': '2021-01-04', 'name': '海容转债', 'stock_id': 'sh603187', 'stock_nm': '海容冷链'},
    #         '113553': {'cd': '2020-06-19', 'name': '金牌转债', 'stock_id': 'sh603180', 'stock_nm': '金牌厨柜'},
    #         '123002': {'cd': '2018-05-30', 'name': '国祯转债', 'stock_id': 'sz300388', 'stock_nm': '国祯环保'},
    #         '123062': {'cd': '2021-02-01', 'name': '三超转债', 'stock_id': 'sz300554', 'stock_nm': '三超新材'},
    #         '128049': {'cd': '2019-06-03', 'name': '华源转债', 'stock_id': 'sz002787', 'stock_nm': '华源控股'},
    #         '123038': {'cd': '2020-07-01', 'name': '联得转债', 'stock_id': 'sz300545', 'stock_nm': '联得装备'},
    #         '128064': {'cd': '2019-10-14', 'name': '司尔转债', 'stock_id': 'sz002538', 'stock_nm': '司尔特'},
    #         '127019': {'cd': '2021-01-21', 'name': '国城转债', 'stock_id': 'sz000688', 'stock_nm': '国城矿业'},
    #         '128057': {'cd': '2019-09-11', 'name': '博彦转债', 'stock_id': 'sz002649', 'stock_nm': '博彦科技'},
    #         '113578': {'cd': '2020-10-26', 'name': '全筑转债', 'stock_id': 'sh603030', 'stock_nm': '全筑股份'},
    #         '123045': {'cd': '2020-09-18', 'name': '雷迪转债', 'stock_id': 'sz300652', 'stock_nm': '雷迪克'},
    #         '120003': {'cd': '2021-08-26', 'name': '19华菱EB', 'stock_id': 'sz000932', 'stock_nm': '华菱钢铁'},
    #         '128050': {'cd': '2019-06-14', 'name': '钧达转债', 'stock_id': 'sz002865', 'stock_nm': '钧达股份'},
    #         '113602': {'cd': '2021-03-01', 'name': '景20转债', 'stock_id': 'sh603228', 'stock_nm': '景旺电子'},
    #         '123049': {'cd': '2020-10-19', 'name': '维尔转债', 'stock_id': 'sz300190', 'stock_nm': '维尔利'},
    #         '113598': {'cd': '2021-02-08', 'name': '法兰转债', 'stock_id': 'sh603966', 'stock_nm': '法兰泰克'},
    #         '113020': {'cd': '2019-05-23', 'name': '桐昆转债', 'stock_id': 'sh601233', 'stock_nm': '桐昆股份'},
    #         '128099': {'cd': '2020-09-17', 'name': '永高转债', 'stock_id': 'sz002641', 'stock_nm': '永高股份'},
    #         '123048': {'cd': '2020-10-16', 'name': '应急转债', 'stock_id': 'sz300527', 'stock_nm': '中船应急'},
    #         '128085': {'cd': '2020-06-22', 'name': '鸿达转债', 'stock_id': 'sz002002', 'stock_nm': '鸿达兴业'},
    #         '128066': {'cd': '2019-10-23', 'name': '亚泰转债', 'stock_id': 'sz002811', 'stock_nm': '郑中设计'},
    #         '113034': {'cd': '2020-10-16', 'name': '滨化转债', 'stock_id': 'sh601678', 'stock_nm': '滨化股份'},
    #         '128013': {'cd': '2017-02-06', 'name': '洪涛转债', 'stock_id': 'sz002325', 'stock_nm': '洪涛股份'},
    #         '128127': {'cd': '2021-03-01', 'name': '文科转债', 'stock_id': 'sz002775', 'stock_nm': '文科园林'},
    #         '128079': {'cd': '2020-04-27', 'name': '英联转债', 'stock_id': 'sz002846', 'stock_nm': '英联股份'},
    #         '113008': {'cd': '2015-08-03', 'name': '电气转债', 'stock_id': 'sh601727', 'stock_nm': '上海电气'},
    #         '123034': {'cd': '2020-05-08', 'name': '通光转债', 'stock_id': 'sz300265', 'stock_nm': '通光线缆'},
    #         '110072': {'cd': '2021-02-24', 'name': '广汇转债', 'stock_id': 'sh600297', 'stock_nm': '广汇汽车'},
    #         '123065': {'cd': '2021-03-11', 'name': '宝莱转债', 'stock_id': 'sz300246', 'stock_nm': '宝莱特'},
    #         '128021': {'cd': '2018-06-04', 'name': '兄弟转债', 'stock_id': 'sz002562', 'stock_nm': '兄弟科技'},
    #         '128073': {'cd': '2020-02-28', 'name': '哈尔转债', 'stock_id': 'sz002615', 'stock_nm': '哈尔斯'},
    #         '123047': {'cd': '2020-09-28', 'name': '久吾转债', 'stock_id': 'sz300631', 'stock_nm': '久吾高科'},
    #         '113556': {'cd': '2020-06-29', 'name': '至纯转债', 'stock_id': 'sh603690', 'stock_nm': '至纯科技'},
    #         '128019': {'cd': '2018-05-14', 'name': '久立转2', 'stock_id': 'sz002318', 'stock_nm': '久立特材'},
    #         '128039': {'cd': '2018-12-14', 'name': '三力转债', 'stock_id': 'sz002224', 'stock_nm': '三力士'},
    #         '128030': {'cd': '2018-06-28', 'name': '天康转债', 'stock_id': 'sz002100', 'stock_nm': '天康生物'},
    #         '123017': {'cd': '2019-05-27', 'name': '寒锐转债', 'stock_id': 'sz300618', 'stock_nm': '寒锐钴业'},
    #         '128105': {'cd': '2020-10-15', 'name': '长集转债', 'stock_id': 'sz002616', 'stock_nm': '长青集团'},
    #         '128103': {'cd': '2020-10-09', 'name': '同德转债', 'stock_id': 'sz002360', 'stock_nm': '同德化工'},
    #         '128051': {'cd': '2019-06-20', 'name': '光华转债', 'stock_id': 'sz002741', 'stock_nm': '光华科技'},
    #         '128094': {'cd': '2020-07-22', 'name': '星帅转债', 'stock_id': 'sz002860', 'stock_nm': '星帅尔'},
    #         '128022': {'cd': '2018-06-07', 'name': '众信转债', 'stock_id': 'sz002707', 'stock_nm': '众信旅游'},
    #         '128129': {'cd': '2021-03-01', 'name': '青农转债', 'stock_id': 'sz002958', 'stock_nm': '青农商行'},
    #         '128106': {'cd': '2020-10-16', 'name': '华统转债', 'stock_id': 'sz002840', 'stock_nm': '华统股份'},
    #         '123032': {'cd': '2020-04-17', 'name': '万里转债', 'stock_id': 'sz300591', 'stock_nm': '万里马'},
    #         '128095': {'cd': '2020-08-17', 'name': '恩捷转债', 'stock_id': 'sz002812', 'stock_nm': '恩捷股份'},
    #         '128107': {'cd': '2020-10-28', 'name': '交科转债', 'stock_id': 'sz002061', 'stock_nm': '浙江交科'},
    #         '110065': {'cd': '2020-06-29', 'name': '淮矿转债', 'stock_id': 'sh600985', 'stock_nm': '淮北矿业'},
    #         '123064': {'cd': '2021-03-08', 'name': '万孚转债', 'stock_id': 'sz300482', 'stock_nm': '万孚生物'},
    #         '132021': {'cd': '2020-11-30', 'name': '19中电EB', 'stock_id': 'sh600536', 'stock_nm': '中国软件'},
    #         '123055': {'cd': '2020-12-23', 'name': '晨光转债', 'stock_id': 'sz300138', 'stock_nm': '晨光生物'},
    #         '123054': {'cd': '2020-12-16', 'name': '思特转债', 'stock_id': 'sz300608', 'stock_nm': '思特奇'},
    #         '120004': {'cd': '2021-08-26', 'name': '20华菱EB', 'stock_id': 'sz000932', 'stock_nm': '华菱钢铁'},
    #         '128082': {'cd': '2020-06-10', 'name': '华锋转债', 'stock_id': 'sz002806', 'stock_nm': '华锋股份'},
    #         '113576': {'cd': '2020-10-16', 'name': '起步转债', 'stock_id': 'sh603557', 'stock_nm': '起步股份'},
    #         '123035': {'cd': '2020-05-20', 'name': '利德转债', 'stock_id': 'sz300296', 'stock_nm': '利亚德'},
    #         '113600': {'cd': '2021-02-19', 'name': '新星转债', 'stock_id': 'sh603978', 'stock_nm': '深圳新星'},
    #         '128074': {'cd': '2020-03-27', 'name': '游族转债', 'stock_id': 'sz002174', 'stock_nm': '游族网络'},
    #         '128046': {'cd': '2019-04-23', 'name': '利尔转债', 'stock_id': 'sz002258', 'stock_nm': '利尔化学'},
    #         '123061': {'cd': '2021-01-28', 'name': '航新转债', 'stock_id': 'sz300424', 'stock_nm': '航新科技'},
    #         '128090': {'cd': '2020-07-03', 'name': '汽模转2', 'stock_id': 'sz002510', 'stock_nm': '天汽模'},
    #         '113567': {'cd': '2020-09-10', 'name': '君禾转债', 'stock_id': 'sh603617', 'stock_nm': '君禾股份'},
    #         '113562': {'cd': '2020-07-08', 'name': '璞泰转债', 'stock_id': 'sh603659', 'stock_nm': '璞泰来'},
    #         '128114': {'cd': '2020-12-23', 'name': '正邦转债', 'stock_id': 'sz002157', 'stock_nm': '正邦科技'},
    #         '113545': {'cd': '2020-04-20', 'name': '金能转债', 'stock_id': 'sh603113', 'stock_nm': '金能科技'},
    #         '113029': {'cd': '2020-06-22', 'name': '明阳转债', 'stock_id': 'sh601615', 'stock_nm': '明阳智能'},
    #         '113039': {'cd': '2021-03-01', 'name': '嘉泽转债', 'stock_id': 'sh601619', 'stock_nm': '嘉泽新能'},
    #         '123059': {'cd': '2021-01-21', 'name': '银信转债', 'stock_id': 'sz300231', 'stock_nm': '银信科技'},
    #         '113570': {'cd': '2020-09-17', 'name': '百达转债', 'stock_id': 'sh603331', 'stock_nm': '百达精工'},
    #         '113033': {'cd': '2020-10-08', 'name': '利群转债', 'stock_id': 'sh601366', 'stock_nm': '利群股份'},
    #         '128100': {'cd': '2020-09-18', 'name': '搜特转债', 'stock_id': 'sz002503', 'stock_nm': '搜于特'},
    #         '123018': {'cd': '2019-06-26', 'name': '溢利转债', 'stock_id': 'sz300381', 'stock_nm': '溢多利'},
    #         '110055': {'cd': '2019-09-23', 'name': '伊力转债', 'stock_id': 'sh600197', 'stock_nm': '伊力特'},
    #         '123043': {'cd': '2020-09-11', 'name': '正元转债', 'stock_id': 'sz300645', 'stock_nm': '正元智慧'},
    #         '123012': {'cd': '2019-01-26', 'name': '万顺转债', 'stock_id': 'sz300057', 'stock_nm': '万顺新材'},
    #         '113568': {'cd': '2020-09-14', 'name': '新春转债', 'stock_id': 'sh603667', 'stock_nm': '五洲新春'},
    #         '113549': {'cd': '2020-05-21', 'name': '白电转债', 'stock_id': 'sh603861', 'stock_nm': '白云电器'},
    #         '113557': {'cd': '2020-06-29', 'name': '森特转债', 'stock_id': 'sh603098', 'stock_nm': '森特股份'},
    #         '110071': {'cd': '2021-01-18', 'name': '湖盐转债', 'stock_id': 'sh600929', 'stock_nm': '湖南盐业'},
    #         '123010': {'cd': '2019-01-11', 'name': '博世转债', 'stock_id': 'sz300422', 'stock_nm': '博世科'},
    #         '113036': {'cd': '2021-01-11', 'name': '宁建转债', 'stock_id': 'sh601789', 'stock_nm': '宁波建工'},
    #         '113038': {'cd': '2021-02-08', 'name': '隆20转债', 'stock_id': 'sh601012', 'stock_nm': '隆基股份'},
    #         '110051': {'cd': '2019-09-06', 'name': '中天转债', 'stock_id': 'sh600522', 'stock_nm': '中天科技'},
    #         '128048': {'cd': '2019-05-16', 'name': '张行转债', 'stock_id': 'sz002839', 'stock_nm': '张家港行'},
    #         '128119': {'cd': '2021-01-18', 'name': '龙大转债', 'stock_id': 'sz002726', 'stock_nm': '龙大肉食'},
    #         '123028': {'cd': '2019-12-25', 'name': '清水转债', 'stock_id': 'sz300437', 'stock_nm': '清水源'},
    #         '128110': {'cd': '2020-12-15', 'name': '永兴转债', 'stock_id': 'sz002756', 'stock_nm': '永兴材料'},
    #         '128131': {'cd': '2021-03-11', 'name': '崇达转2', 'stock_id': 'sz002815', 'stock_nm': '崇达技术'},
    #         '128028': {'cd': '2018-06-27', 'name': '赣锋转债', 'stock_id': 'sz002460', 'stock_nm': '赣锋锂业'},
    #         '110041': {'cd': '2018-06-28', 'name': '蒙电转债', 'stock_id': 'sh600863', 'stock_nm': '内蒙华电'},
    #         '110033': {'cd': '2016-07-05', 'name': '国贸转债', 'stock_id': 'sh600755', 'stock_nm': '厦门国贸'},
    #         '127005': {'cd': '2018-09-17', 'name': '长证转债', 'stock_id': 'sz000783', 'stock_nm': '长江证券'},
    #         '113546': {'cd': '2020-04-29', 'name': '迪贝转债', 'stock_id': 'sh603320', 'stock_nm': '迪贝电气'},
    #         '128111': {'cd': '2020-12-17', 'name': '中矿转债', 'stock_id': 'sz002738', 'stock_nm': '中矿资源'},
    #         '110064': {'cd': '2020-06-29', 'name': '建工转债', 'stock_id': 'sh600939', 'stock_nm': '重庆建工'},
    #         '127017': {'cd': '2020-12-09', 'name': '万青转债', 'stock_id': 'sz000789', 'stock_nm': '万年青'},
    #         '110043': {'cd': '2018-08-05', 'name': '无锡转债', 'stock_id': 'sh600908', 'stock_nm': '无锡银行'},
    #         '110057': {'cd': '2019-10-08', 'name': '现代转债', 'stock_id': 'sh600420', 'stock_nm': '现代制药'},
    #         '128025': {'cd': '2018-06-12', 'name': '特一转债', 'stock_id': 'sz002728', 'stock_nm': '特一药业'},
    #         '113542': {'cd': '2020-02-12', 'name': '好客转债', 'stock_id': 'sh603898', 'stock_nm': '好莱客'},
    #         '123057': {'cd': '2021-01-07', 'name': '美联转债', 'stock_id': 'sz300586', 'stock_nm': '美联新材'},
    #         '123058': {'cd': '2021-01-20', 'name': '欣旺转债', 'stock_id': 'sz300207', 'stock_nm': '欣旺达'},
    #         '110061': {'cd': '2020-05-15', 'name': '川投转债', 'stock_id': 'sh600674', 'stock_nm': '川投能源'},
    #         '123053': {'cd': '2020-12-11', 'name': '宝通转债', 'stock_id': 'sz300031', 'stock_nm': '宝通科技'},
    #         '128117': {'cd': '2021-01-08', 'name': '道恩转债', 'stock_id': 'sz002838', 'stock_nm': '道恩股份'},
    #         '128034': {'cd': '2018-08-01', 'name': '江银转债', 'stock_id': 'sz002807', 'stock_nm': '江阴银行'},
    #         '128069': {'cd': '2019-12-30', 'name': '华森转债', 'stock_id': 'sz002907', 'stock_nm': '华森制药'},
    #         '110038': {'cd': '2018-05-17', 'name': '济川转债', 'stock_id': 'sh600566', 'stock_nm': '济川药业'},
    #         '110063': {'cd': '2020-06-19', 'name': '鹰19转债', 'stock_id': 'sh600567', 'stock_nm': '山鹰纸业'},
    #         '127020': {'cd': '2021-01-25', 'name': '中金转债', 'stock_id': 'sz000060', 'stock_nm': '中金岭南'},
    #         '128053': {'cd': '2019-08-20', 'name': '尚荣转债', 'stock_id': 'sz002551', 'stock_nm': '尚荣医疗'},
    #         '113025': {'cd': '2019-10-16', 'name': '明泰转债', 'stock_id': 'sh601677', 'stock_nm': '明泰铝业'},
    #         '127007': {'cd': '2019-01-04', 'name': '湖广转债', 'stock_id': 'sz000665', 'stock_nm': '湖北广电'},
    #         '110056': {'cd': '2019-09-26', 'name': '亨通转债', 'stock_id': 'sh600487', 'stock_nm': '亨通光电'},
    #         '128040': {'cd': '2018-12-21', 'name': '华通转债', 'stock_id': 'sz002758', 'stock_nm': '华通医药'},
    #         '128116': {'cd': '2021-01-04', 'name': '瑞达转债', 'stock_id': 'sz002961', 'stock_nm': '瑞达期货'},
    #         '128125': {'cd': '2021-02-05', 'name': '华阳转债', 'stock_id': 'sz002949', 'stock_nm': '华阳国际'},
    #         '110048': {'cd': '2019-06-13', 'name': '福能转债', 'stock_id': 'sh600483', 'stock_nm': '福能股份'},
    #         '113032': {'cd': '2020-09-07', 'name': '桐20转债', 'stock_id': 'sh601233', 'stock_nm': '桐昆股份'},
    #         '110073': {'cd': '2021-02-01', 'name': '国投转债', 'stock_id': 'sh600061', 'stock_nm': '国投资本'},
    #         '113011': {'cd': '2017-09-18', 'name': '光大转债', 'stock_id': 'sh601818', 'stock_nm': '光大银行'},
    #         '110047': {'cd': '2019-05-27', 'name': '山鹰转债', 'stock_id': 'sh600567', 'stock_nm': '山鹰纸业'},
    #         '123014': {'cd': '2019-02-11', 'name': '凯发转债', 'stock_id': 'sz300407', 'stock_nm': '凯发电气'},
    #         '123025': {'cd': '2019-10-08', 'name': '精测转债', 'stock_id': 'sz300567', 'stock_nm': '精测电子'},
    #         '128036': {'cd': '2018-09-16', 'name': '金农转债', 'stock_id': 'sz002548', 'stock_nm': '金新农'},
    #         '113559': {'cd': '2020-06-29', 'name': '永创转债', 'stock_id': 'sh603901', 'stock_nm': '永创智能'},
    #         '128065': {'cd': '2019-10-22', 'name': '雅化转债', 'stock_id': 'sz002497', 'stock_nm': '雅化集团'},
    #         '128109': {'cd': '2020-12-10', 'name': '楚江转债', 'stock_id': 'sz002171', 'stock_nm': '楚江新材'},
    #         '128113': {'cd': '2020-12-21', 'name': '比音转债', 'stock_id': 'sz002832', 'stock_nm': '比音勒芬'},
    #         '113591': {'cd': '2021-01-08', 'name': '胜达转债', 'stock_id': 'sh603687', 'stock_nm': '大胜达'},
    #         '110070': {'cd': '2020-10-19', 'name': '凌钢转债', 'stock_id': 'sh600231', 'stock_nm': '凌钢股份'},
    #         '113030': {'cd': '2020-06-30', 'name': '东风转债', 'stock_id': 'sh601515', 'stock_nm': '东风股份'},
    #         '128076': {'cd': '2020-04-20', 'name': '金轮转债', 'stock_id': 'sz002722', 'stock_nm': '金轮股份'},
    #         '123042': {'cd': '2020-07-20', 'name': '银河转债', 'stock_id': 'sz300619', 'stock_nm': '金银河'},
    #         '113516': {'cd': '2019-02-11', 'name': '苏农转债', 'stock_id': 'sh603323', 'stock_nm': '苏农银行'},
    #         '113526': {'cd': '2019-07-29', 'name': '联泰转债', 'stock_id': 'sh603797', 'stock_nm': '联泰环保'},
    #         '110068': {'cd': '2020-09-30', 'name': '龙净转债', 'stock_id': 'sh600388', 'stock_nm': '龙净环保'},
    #         '110052': {'cd': '2019-09-11', 'name': '贵广转债', 'stock_id': 'sh600996', 'stock_nm': '贵广网络'},
    #         '128120': {'cd': '2021-01-25', 'name': '联诚转债', 'stock_id': 'sz002921', 'stock_nm': '联诚精密'},
    #         '113579': {'cd': '2020-10-29', 'name': '健友转债', 'stock_id': 'sh603707', 'stock_nm': '健友股份'},
    #         '113563': {'cd': '2020-07-22', 'name': '柳药转债', 'stock_id': 'sh603368', 'stock_nm': '柳药股份'},
    #         '127016': {'cd': '2020-10-15', 'name': '鲁泰转债', 'stock_id': 'sz000726', 'stock_nm': '鲁泰A'},
    #         '113037': {'cd': '2021-01-29', 'name': '紫银转债', 'stock_id': 'sh601860', 'stock_nm': '紫金银行'},
    #         '128093': {'cd': '2020-07-09', 'name': '百川转债', 'stock_id': 'sz002455', 'stock_nm': '百川股份'},
    #         '113519': {'cd': '2019-05-13', 'name': '长久转债', 'stock_id': 'sh603569', 'stock_nm': '长久物流'},
    #         '113013': {'cd': '2018-01-08', 'name': '国君转债', 'stock_id': 'sh601211', 'stock_nm': '国泰君安'},
    #         '128070': {'cd': '2020-01-08', 'name': '智能转债', 'stock_id': 'sz002877', 'stock_nm': '智能自控'},
    #         '123036': {'cd': '2020-06-17', 'name': '先导转债', 'stock_id': 'sz300450', 'stock_nm': '先导智能'},
    #         '113588': {'cd': '2020-12-23', 'name': '润达转债', 'stock_id': 'sh603108', 'stock_nm': '润达医疗'},
    #         '123004': {'cd': '2018-06-22', 'name': '铁汉转债', 'stock_id': 'sz300197', 'stock_nm': '铁汉生态'},
    #         '123031': {'cd': '2020-03-05', 'name': '晶瑞转债', 'stock_id': 'sz300655', 'stock_nm': '晶瑞股份'},
    #         '128118': {'cd': '2021-01-08', 'name': '瀛通转债', 'stock_id': 'sz002861', 'stock_nm': '瀛通通讯'},
    #         '128081': {'cd': '2020-05-27', 'name': '海亮转债', 'stock_id': 'sz002203', 'stock_nm': '海亮股份'},
    #         '123060': {'cd': '2021-01-27', 'name': '苏试转债', 'stock_id': 'sz300416', 'stock_nm': '苏试试验'},
    #         '110053': {'cd': '2019-09-20', 'name': '苏银转债', 'stock_id': 'sh600919', 'stock_nm': '江苏银行'},
    #         '128087': {'cd': '2020-06-23', 'name': '孚日转债', 'stock_id': 'sz002083', 'stock_nm': '孚日股份'},
    #         '128063': {'cd': '2019-10-11', 'name': '未来转债', 'stock_id': 'sz002631', 'stock_nm': '德尔未来'},
    #         '113534': {'cd': '2019-10-16', 'name': '鼎胜转债', 'stock_id': 'sh603876', 'stock_nm': '鼎胜新材'},
    #         '110067': {'cd': '2020-09-18', 'name': '华安转债', 'stock_id': 'sh600909', 'stock_nm': '华安证券'},
    #         '128123': {'cd': '2021-02-01', 'name': '国光转债', 'stock_id': 'sz002749', 'stock_nm': '国光股份'},
    #         '113524': {'cd': '2019-06-20', 'name': '奇精转债', 'stock_id': 'sh603677', 'stock_nm': '奇精机械'},
    #         '123033': {'cd': '2020-05-07', 'name': '金力转债', 'stock_id': 'sz300748', 'stock_nm': '金力永磁'},
    #         '123039': {'cd': '2020-07-02', 'name': '开润转债', 'stock_id': 'sz300577', 'stock_nm': '开润股份'},
    #         '113584': {'cd': '2020-12-14', 'name': '家悦转债', 'stock_id': 'sh603708', 'stock_nm': '家家悦'},
    #         '113532': {'cd': '2019-10-09', 'name': '海环转债', 'stock_id': 'sh603817', 'stock_nm': '海峡环保'},
    #         '127006': {'cd': '2018-09-19', 'name': '敖东转债', 'stock_id': 'sz000623', 'stock_nm': '吉林敖东'},
    #         '110062': {'cd': '2020-06-08', 'name': '烽火转债', 'stock_id': 'sh600498', 'stock_nm': '烽火通信'},
    #         '127013': {'cd': '2019-10-21', 'name': '创维转债', 'stock_id': 'sz000810', 'stock_nm': '创维数字'},
    #         '110034': {'cd': '2016-07-21', 'name': '九州转债', 'stock_id': 'sh600998', 'stock_nm': '九州通'},
    #         '123011': {'cd': '2019-01-24', 'name': '德尔转债', 'stock_id': 'sz300473', 'stock_nm': '德尔股份'},
    #         '113017': {'cd': '2018-07-03', 'name': '吉视转债', 'stock_id': 'sh601929', 'stock_nm': '吉视传媒'},
    #         '127014': {'cd': '2020-04-30', 'name': '北方转债', 'stock_id': 'sz000065', 'stock_nm': '北方国际'},
    #         '127012': {'cd': '2019-09-30', 'name': '招路转债', 'stock_id': 'sz001965', 'stock_nm': '招商公路'},
    #         '113593': {'cd': '2021-01-25', 'name': '沪工转债', 'stock_id': 'sh603131', 'stock_nm': '上海沪工'},
    #         '128052': {'cd': '2019-06-27', 'name': '凯龙转债', 'stock_id': 'sz002783', 'stock_nm': '凯龙股份'},
    #         '128083': {'cd': '2020-06-18', 'name': '新北转债', 'stock_id': 'sz002376', 'stock_nm': '新北洋'},
    #         '128121': {'cd': '2021-01-25', 'name': '宏川转债', 'stock_id': 'sz002930', 'stock_nm': '宏川智慧'},
    #         '123007': {'cd': '2018-07-04', 'name': '道氏转债', 'stock_id': 'sz300409', 'stock_nm': '道氏技术'},
    #         '113594': {'cd': '2021-01-27', 'name': '淳中转债', 'stock_id': 'sh603516', 'stock_nm': '淳中科技'},
    #         '123023': {'cd': '2019-09-27', 'name': '迪森转债', 'stock_id': 'sz300335', 'stock_nm': '迪森股份'},
    #         '113505': {'cd': '2018-09-12', 'name': '杭电转债', 'stock_id': 'sh603618', 'stock_nm': '杭电股份'},
    #         '113527': {'cd': '2019-07-30', 'name': '维格转债', 'stock_id': 'sh603518', 'stock_nm': '锦泓集团'},
    #         '128042': {'cd': '2019-02-03', 'name': '凯中转债', 'stock_id': 'sz002823', 'stock_nm': '凯中精密'},
    #         '113528': {'cd': '2019-09-09', 'name': '长城转债', 'stock_id': 'sh603897', 'stock_nm': '长城科技'},
    #         '128018': {'cd': '2018-05-10', 'name': '时达转债', 'stock_id': 'sz002527', 'stock_nm': '新时达'},
    #         '128091': {'cd': '2020-07-06', 'name': '新天转债', 'stock_id': 'sz002873', 'stock_nm': '新天药业'},
    #         '113596': {'cd': '2021-02-03', 'name': '城地转债', 'stock_id': 'sh603887', 'stock_nm': '城地股份'},
    #         '113026': {'cd': '2019-10-21', 'name': '核能转债', 'stock_id': 'sh601985', 'stock_nm': '中国核电'},
    #         '128124': {'cd': '2021-02-03', 'name': '科华转债', 'stock_id': 'sz002022', 'stock_nm': '科华生物'},
    #         '127011': {'cd': '2019-09-16', 'name': '中鼎转2', 'stock_id': 'sz000887', 'stock_nm': '中鼎股份'},
    #         '128012': {'cd': '2016-10-28', 'name': '辉丰转债', 'stock_id': 'sz002496', 'stock_nm': '*ST辉丰'},
    #         '128026': {'cd': '2018-06-19', 'name': '众兴转债', 'stock_id': 'sz002772', 'stock_nm': '众兴菌业'},
    #         '113024': {'cd': '2019-10-14', 'name': '核建转债', 'stock_id': 'sh601611', 'stock_nm': '中国核建'},
    #         '123024': {'cd': '2019-09-27', 'name': '岱勒转债', 'stock_id': 'sz300700', 'stock_nm': '岱勒新材'},
    #         '113012': {'cd': '2017-10-09', 'name': '骆驼转债', 'stock_id': 'sh601311', 'stock_nm': '骆驼股份'},
    #         '127021': {'cd': '2021-02-15', 'name': '特发转2', 'stock_id': 'sz000070', 'stock_nm': '特发信息'},
    #         '113014': {'cd': '2018-05-03', 'name': '林洋转债', 'stock_id': 'sh601222', 'stock_nm': '林洋能源'},
    #         '113573': {'cd': '2020-10-23', 'name': '纵横转债', 'stock_id': 'sh603602', 'stock_nm': '纵横通信'},
    #         '110031': {'cd': '2015-12-14', 'name': '航信转债', 'stock_id': 'sh600271', 'stock_nm': '航天信息'},
    #         '113530': {'cd': '2019-10-08', 'name': '大丰转债', 'stock_id': 'sh603081', 'stock_nm': '大丰实业'},
    #         '127018': {'cd': '2021-01-04', 'name': '本钢转债', 'stock_id': 'sz000761', 'stock_nm': '本钢板材'},
    #         '113021': {'cd': '2019-09-09', 'name': '中信转债', 'stock_id': 'sh601998', 'stock_nm': '中信银行'},
    #         '113597': {'cd': '2021-02-05', 'name': '佳力转债', 'stock_id': 'sh603912', 'stock_nm': '佳力图'},
    #         '128122': {'cd': '2021-01-29', 'name': '兴森转债', 'stock_id': 'sz002436', 'stock_nm': '兴森科技'},
    #         '127008': {'cd': '2019-05-22', 'name': '特发转债', 'stock_id': 'sz000070', 'stock_nm': '特发信息'},
    #         '128033': {'cd': '2018-07-03', 'name': '迪龙转债', 'stock_id': 'sz002658', 'stock_nm': '雪迪龙'},
    #         '113574': {'cd': '2020-10-08', 'name': '华体转债', 'stock_id': 'sh603679', 'stock_nm': '华体科技'},
    #         '128044': {'cd': '2019-02-20', 'name': '岭南转债', 'stock_id': 'sz002717', 'stock_nm': '岭南股份'},
    #         '113535': {'cd': '2019-11-15', 'name': '大业转债', 'stock_id': 'sh603278', 'stock_nm': '大业股份'},
    #         '128014': {'cd': '2017-10-23', 'name': '永东转债', 'stock_id': 'sz002753', 'stock_nm': '永东股份'},
    #         '110059': {'cd': '2020-05-06', 'name': '浦发转债', 'stock_id': 'sh600000', 'stock_nm': '浦发银行'},
    #         '128126': {'cd': '2021-02-18', 'name': '赣锋转2', 'stock_id': 'sz002460', 'stock_nm': '赣锋锂业'},
    #         '113009': {'cd': '2016-07-22', 'name': '广汽转债', 'stock_id': 'sh601238', 'stock_nm': '广汽集团'},
    #         '128015': {'cd': '2017-12-15', 'name': '久其转债', 'stock_id': 'sz002279', 'stock_nm': '久其软件'},
    #         '113589': {'cd': '2021-01-04', 'name': '天创转债', 'stock_id': 'sh603608', 'stock_nm': '天创时尚'},
    #         '128072': {'cd': '2020-02-26', 'name': '翔鹭转债', 'stock_id': 'sz002842', 'stock_nm': '翔鹭钨业'},
    #         '128101': {'cd': '2020-09-21', 'name': '联创转债', 'stock_id': 'sz002036', 'stock_nm': '联创电子'},
    #         '128032': {'cd': '2018-06-29', 'name': '双环转债', 'stock_id': 'sz002472', 'stock_nm': '双环传动'},
    #         '113508': {'cd': '2018-11-05', 'name': '新凤转债', 'stock_id': 'sh603225', 'stock_nm': '新凤鸣'},
    #         '128041': {'cd': '2019-01-23', 'name': '盛路转债', 'stock_id': 'sz002446', 'stock_nm': '盛路通信'},
    #         '128035': {'cd': '2018-08-13', 'name': '大族转债', 'stock_id': 'sz002008', 'stock_nm': '大族激光'},
    #         '113569': {'cd': '2020-09-14', 'name': '科达转债', 'stock_id': 'sh603660', 'stock_nm': '苏州科达'},
    #         '110045': {'cd': '2019-01-19', 'name': '海澜转债', 'stock_id': 'sh600398', 'stock_nm': '海澜之家'},
    #         '113502': {'cd': '2018-05-17', 'name': '嘉澳转债', 'stock_id': 'sh603822', 'stock_nm': '嘉澳环保'},
    #         '127004': {'cd': '2017-12-08', 'name': '模塑转债', 'stock_id': 'sz000700', 'stock_nm': '模塑科技'},
    #         '113016': {'cd': '2018-05-11', 'name': '小康转债', 'stock_id': 'sh601127', 'stock_nm': '小康股份'},
    #         '128023': {'cd': '2018-06-08', 'name': '亚太转债', 'stock_id': 'sz002284', 'stock_nm': '亚太股份'},
    #         '123015': {'cd': '2019-02-18', 'name': '蓝盾转债', 'stock_id': 'sz300297', 'stock_nm': '蓝盾股份'},
    #         '128010': {'cd': '2016-07-29', 'name': '顺昌转债', 'stock_id': 'sz002245', 'stock_nm': '澳洋顺昌'},
    #         '128037': {'cd': '2018-09-21', 'name': '岩土转债', 'stock_id': 'sz002542', 'stock_nm': '中化岩土'},
    #         '110044': {'cd': '2019-01-03', 'name': '广电转债', 'stock_id': 'sh600831', 'stock_nm': '广电网络'},
    #         '128062': {'cd': '2019-10-09', 'name': '亚药转债', 'stock_id': 'sz002370', 'stock_nm': '亚太药业'},
    #         '123013': {'cd': '2019-02-01', 'name': '横河转债', 'stock_id': 'sz300539', 'stock_nm': '横河模具'}
}
for k, v in data.items():
    tail = v["stock_id"][:2].upper()
    cd = v["cd"]  # 2021-02-26
    cd_date = datetime.datetime.strptime(cd, "%Y-%m-%d")
    if cd_date >= datetime.datetime.today():
        continue
    back_day = (cd_date + datetime.timedelta(days=30)).strftime("%Y-%m-%d").replace("-", "")
    front_day = (cd_date + datetime.timedelta(days=-30)).strftime("%Y-%m-%d").replace("-", "")
    stock_data = c.csd(v["stock_id"][2:] + "." + tail, "PCTCHANGE", front_day, back_day,
                       options="Ispandas=1,RowIndex=2")
    zz500_date = c.csd("000905.SH", "PCTCHANGE", front_day, back_day, options="Ispandas=1,RowIndex=2")
    x = []
    y1 = []
    y2 = []
    for index, row in stock_data.iterrows():
        stock_change = row["PCTCHANGE"]
        zz500_change = zz500_date[zz500_date.index == index]["PCTCHANGE"]
        x.append(index)
        y1.append(stock_change)
        y2.append(zz500_change)
    plt.figure(num=1, figsize=(15, 8), dpi=80)
    plt.grid()  # 生成网格
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(2))  # 密度总坐标数除70
    plt.xticks(rotation=60, fontsize=3)  # 设置横坐标显示的角度，角度是逆时针，自己看
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(x, y1, label=v["stock_nm"])
    plt.plot(x, y2, label="中证500")
    plt.tick_params(labelsize=23)
    plt.legend(fontsize=15)
    
    plt.savefig('../picture_data/picture_zz500_bond_trans_T30/{}.png'.format(v["stock_id"]), dpi=300,
                bbox_inches='tight')
    plt.show()
# c.stop()