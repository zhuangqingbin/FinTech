# coding = utf-8
# /usr/bin/env python

# Author: Jimmy
# Date: 2020-05-08 10:20

import os

#### 自动化邮件系统
# 设置服务器
MAIL_HOST = "smtp.qq.com"
# 用户名
MAIL_USER = "360650538@qq.com"
# 授权码


MAIL_TOKEN = 'ksymhxmiyrdxbhgc'
SENDER = '360650538@qq.com'
# RECEVIERS = ['360650538@qq.com','ccczexin@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
RECEVIERS = ['360650538@qq.com']

# 发件人名字（昵称）
SENDER_NAME = '量化机器人'
# 收件人名字（昵称）
RECEVIER_NAME = '终端用户'



# 监控股票
# STOCKS = ['603078','000021','600745','300346','300655','603005','600183',
#           '002463','002156','000636','002185','002241','600703','002456']
STOCKS = ['603078','000021']

# 行业龙头
NO1_dict = {
    '002415': '海康威视：连续7年蝉联全球视频监控设备市场第一名',
    '002475': 'AirPods全球组装供应商第一名',
    '000725': '京东方：LCD屏全球第一名',
    '603160': '汇顶科技：指纹芯片出货量全球第一名',
    '600745': '闻泰科技：全球最大的手机ODM公司',
    '000661': '长春高新：长效生长激素全球第一名',
    '002241': '歌尔股份：微型麦克风、游戏手柄业务、中高端虚拟现实业务全球第一名',
    '300628': '亿联网络：SIP出货量全球第一名',
    '300207': '欣旺达：智能手机电池全球第一名',
    '002019': '亿帆医药：泛酸钙全球第一名 国内第一名',
    '600276': '恒瑞医药：国内药品研发综合实力第一名',
    '300760': '迈瑞医疗：国内医疗器械公司第一名',
    '000063': '中兴通讯：通信电源市场国内第一名',
    '601360': '三六零：杀毒软件国内第一名',
    '300122': '智飞生物：二类疫苗销售国内第一名',
    '600588': '用友网络：公有云SaaS国内第一名',
    '600703': '三安光电：LED芯片国内第一名',
    '002230': '科大讯飞：智能语音国内第一名',
    '300454': '深信服：虚拟专用网络（Virtual Private Network）领域连续11年蝉联国内第一名；下一代防火墙在UTM领域国内第一名',
    '002371': '北方华创：IC设备品类国内第一名，除光刻机以外几乎涵盖所有的IC制造设备',
    '300014': '亿纬锂能：锂亚硫酰氯电池国内第一名',
    '002916': '深南电路：PCB国内第一名',
    '002841': '视源股份：交互智能平板国内第一名',
    '002007': '华兰生物：国内拥有产品品种最多、规格最全的血液制品生产企业',
    '002410': '广联达：建筑信息化国内第一名',
    '002456': '欧菲光：光学器件国内第一名',
    '603659': '璞泰来：人造石墨类负极材料国内第一名',
    '600845': '宝信软件：国内钢铁制造信息化、自动化第一品牌',
    '002008': '大族激光：国内最大的激光设备企业',
    '300136': '信维通信：手机天线国内第一名 中科曙光：超算Top100份额国内第一名',
    '002153': '石基信息：酒店信息管理系统国内第一名',
    '002463': '沪电股份：多层印制电路板国内第一名',
    '002439': '启明星辰：堡垒机国内第一名',
    '000050': '深天马：车载屏幕出货量国内第一名',
    '002405': '四维图新：车载前装导航国内第一名',
    '300271': '华宇软件：连续11年法院、检察院信息化领域国内第一名',
    '002152': '广电运通：连续11年银行设备国内第一名',
    '002396': '星网锐捷：连续16年瘦客户机国内第一名',
    '300017': '网宿科技：CDN业务国内第一名',
    '002281': '光迅科技：光通信器件国内第一名',
    '000997': '新大陆：POS机国内第一名',
    '002583': '海能达：专网通信终端国内第一名',
}

NO1_A_dict = {
    '300782': '卓胜微：射频芯片龙头',
    '600745': '闻泰科技：半导体标准器件龙头，收购安世半导体',
    '002475': '立讯精密：连接器龙头，TWS中军',
    '300136': '信维通信：手机天线龙头，开启趋势',
    '300750': '宁德时代：锂电池龙头',
    '000977': '浪潮信息：服务器龙头',
    '002938': '鹏鼎控股：消费电子PCB龙头',
    '603501': '韦尔股份：电源管理IC龙头',
    '603160': '汇顶科技：指纹识别芯片龙头',
    '002600': '领益智造：电子元器件龙头',
    '002456': '欧菲光：摄像头龙头',
    '300661': '圣邦股份：模拟芯片龙头',
    '600703': '三安光电：全球LED龙头',
    '002241': '歌尔股份：电声行业龙头',
    '688111': '金山办公：办公软件龙头',
    '300433': '蓝思科技：手机屏幕龙头',
    '002916': '深南电路：通信PCB龙头',
    '603986': '兆易创新：存储器龙头',
    '600183': '生益科技：覆铜板龙头',
    '300628': '亿联网络：通信终端龙头',
    '300383': '光环新网：IDC龙头',
    '002049': '紫光国微：国产芯片龙头',
    '600536': '中国软件：国产操作系统龙头',
    '002008': '大族激光：激光设备龙头',
    '601231': '环旭电子：消费电子用电池龙头',
    '002371': '北方华创：半导体设备龙头',
    '600584': '长电科技：半导体封测龙头',
    '300308': '中际旭创：光模块龙头',
    '600276': '恒瑞医药：创新药龙头',
    '300015': '爱尔眼科：眼科医疗龙头',
    '300760': '迈瑞医疗：医疗器械的大龙头',
    '603259': '药明康德：医药RCO龙头',
    '000661': '长春高新：创新药分支生长激素龙头',
    '600436': '片仔癀：中药龙头',
    '002044': '美年健康：体检医疗服务龙头',
    '000538': '云南白药：传统中医药龙头',
    '600196': '复星医药：创新药投入第二的龙头',
    '600332': '白云山：中药，西药双龙头',
    '300003': '乐普医疗：心脏支架系统龙头',
    '002001': '新和成：维生素龙头',
    '002007': '华兰生物：血液制品龙头',
    '300122': '智飞生物：疫苗代理销售龙头',
    '300347': '泰格医药：临床试验与咨询龙头',
    '600763': '通策医疗：口腔医疗龙头',
    '603939': '益丰药房：零售实体药店龙头',
    '000999': '华润三九：皮肤用药龙头',
    '002422': '科伦药业：输液药龙头',
    '300601': '康泰生物：自主疫苗龙头',
    '300357': '我武生物：脱敏药龙头',
    '002223': '鱼跃医疗：最全面的家用医疗器械行业的龙头',
    '002398': '丽珠集团：专科制剂领域老牌龙头',
    '300529': '健帆生物：一次性使用血液灌流器械龙头',
    '603707': '健友股份：肝素原料药龙头',
    '002821': '凯莱英：国际RCO龙头',
    '603882': '金域医学：诊断医学服务龙头',
    '300676': '华大基因：基因检测龙头',
    '300146': '汤臣倍健：保健品龙头',
    '600529': '山东药玻：医用包装瓶龙头',
    '300595': '欧普康视：医用光学器具龙头',
    '002603': '以岭药业：心血管药龙头',
    '002287': '奇正藏药：藏药龙头',
    '603858': '步长制药：专一的心脑血管药龙头',
    '002382': '蓝帆医疗：心脏介入器械龙头',
    '002030': '达安基因：荧光PCR检测龙头',
    '002737': '葵花药业：儿科药龙头',
    '002424': '贵州百灵：苗药龙头',
    '600422': '昆药集团：进军大麻的心血管药龙头',
    '300298': '三诺生物：血糖监测仪龙头',
    '600285': '羚锐制药：膏药龙头',
    '688029': '南微医学：微创手术器械龙头',
    '600789': '鲁抗医药：抗生素龙头',
    '300204': '舒泰神：注射用鼠神经生长因子龙头',
    '300147': '香雪制药：抗病毒口服液龙头',
    '600479': '千金药业：妇科药龙头',
    '002901': '大博医疗：骨科龙头',
    '300642': '透景生命：体外试剂诊断龙头',
    '600332': '白云山：中药，西药双龙头',
    '300003': '乐普医疗：心脏支架系统龙头',
    '002001': '新和成：维生素龙头',
    '002007': '华兰生物：血液制品龙头',
    '300122': '智飞生物：疫苗代理销售龙头',
    '002223': '鱼跃医疗：最全面的家用医疗器械行业的龙头',
    '002287': '奇正藏药：藏药龙头',
    '300015': '爱尔眼科：民营眼科医院连锁企业',
    '300070': '碧 水 源： 国内污水处理领先企业',
    '600563': '法拉电子：薄膜电容器制造龙头',
    '002572': '索 菲 亚：定制家具龙头',
    '002450': '康 得 新：国内预涂膜行业领先者',
    '002027': '分众传媒：新媒体营销龙头公司',
    '601888': '中国国旅 ：旅游龙头和免税业唯一的A股上市公司',
    '000895': '双汇发展：肉制品行业的绝对龙头',
    '603078': '江 化 微：湿电子化学品的行业龙头',
    '300648': '星云股份：锂电池检测系统的行业龙头',
    '300691': '联合光电：高端光学镜头的行业龙头',
    '300699': '光威复材：碳纤维 行业龙头',
    '002876': '三 利 谱：偏光片行业龙头',
    '300700': '岱勒新材：金刚石线的行业龙头',
    '000823': '超声电子：汽车电字PCB龙头',
    '603595': '东尼电子：超微细合金线材 的行业龙头',
    '603896': '寿 仙 谷：灵芝行业龙头',
    '002901': '大博医疗：骨科植入类医用耗材领域的龙头企业',
    '300603': '立昂技术：新疆地区的安防 龙头',
    '300620': '光库科技：光纤器件的行业龙头',
    '300689': '澄天伟业：智能卡的行业龙头',
    '300653': '正海生物：再生医学领域行业龙头',
    '603938': '三孚股份：三氯氢硅的行业龙头',
    '002004': '华邦制药：国内皮肤病领域龙头企业',
    '002010': '传化股份：国内纺织印染助剂龙头企业',
    '002022': '科华生物：国内体外临床诊断行业龙头企业',
    '002028': '思源电气：国内最大电力保护设备消弧线圈生产商',
    '002030': '达安基因：国内核酸诊断试剂领域领先者',
    '002031': '巨轮股份：国内汽车子午线轮胎活络模具龙头企业',
    '002036': '联创电子：国内最大中高档服装用衬生产商',
    '002041': '登海种业：国内玉米种子繁育推广一体化龙头企业',
    '002045': '广州国光：国内音响行业龙头企业',
    '002046': '轴研科技：国内航天特种轴承行业龙头企业',
    '002048': '宁波华翔：国内汽车内饰件龙头企业',
    '002056': '横店东磁：全球最大的磁体生产企业之一',
    '002063': '远光软件：国内电力财务软件龙头企业',
    '002071': '江苏宏宝：国内工具五金行业龙头企业',
    '002073': '软控股份：国内轮胎橡胶行业软件龙头企业',
    '002080': '中材科技：国内特种纤维复合材料行业龙头企业',
    '002090': '金智科技：国内电气自动化设备行业龙头企业',
    '002091': '江苏国泰：国内锂离子电池电解液行业龙头企业',
    '002094': '青岛金王：国内最大蜡烛制造商',
    '002098': '浔兴股份：国内拉链行业龙头企业',
    '002101': '广东鸿图：国内压铸行业龙头企业',
    '002103': '广博股份：国内纸制品文具行业龙头企业',
    '002104': '恒宝股份：国内智能卡行业龙头企业',
    '002105': '信隆实业：国内自行车零配件龙头企业',
    '002106': '莱宝高科：国内彩色滤光片行业龙头企业',
    '002111': '威海广泰：国内航空地面设备行业龙头企业',
    '002117': '东港股份：国内规模最大商业票据印刷企业',
    '002119': '康强电子：国内最大塑封引线框架生产基地',
    '002120': '新海股份：世界第四大塑料打火机制造商',
    '002121': '科陆电子：国内用电采集系统领域龙头企业',
    '002125': '湘潭电化：国内最大电解二氧化锰生产商',
    '002126': '银轮股份：国内最大机油冷却器生产商',
    '002130': '沃尔核材：国内热缩材料行业龙头企业',
    '002131': '利欧股份：国内最大的微型小型水泵制造商',
    '002138': '顺络电子：国内最大片式压敏电阻生产商',
    '002139': '拓邦股份：国内最大微波炉控制板生产商',
    '002140': '东华科技：国内煤化工细分行业龙头企业',
    '002141': '蓉胜超微：国内最大微细漆包线生产商',
    '002144': '宏达高科：国内汽车顶棚面料龙头企业',
    '002149': '西部材料：国内最大稀有金属复合材料生产商',
    '002150': '江苏通润：国内工具箱柜行业龙头企业',
    '002158': '汉钟精机：国内螺杆式压缩机龙头企业',
    '002161': '远 望 谷：国内铁路RFID市场垄断地位',
    '002160': '常铝股份：国内最大空调箔生产商',
    '002164': '东力传动：国内冶金齿轮箱领先企业',
    '002171': '精诚铜业：国内最大的铜带生产企业',
    '002175': '广陆数测：国内数显量具行业龙头企业',
    '002176': '江特电机：国内最大起重冶金电机生产商',
    '002179': '中航光电：国内最大军用连接器制造企业',
    '002182': '云海金属：国内最大专业化镁合金生产商',
    '002183': '怡 亚 通：国内领先的供应链服务商',
    '002188': '新 嘉 联：国内受话器行业龙头企业',
    '002190': '成飞集成：国内汽车模具行业龙头企业',
    '002196': '方正电机：全球最大家用缝纫机电机生产基地',
    '002197': '证通电子：国内金融支付信息安全产品领先企业',
    '002201': '九鼎新材：国内最大的纺织型玻纤制品生产商',
    '002202': '金风科技：国内领先的风机制造商',
    '002206': '海 利 得：国内涤纶工业长丝行业龙头企业',
    '002209': '达 意 隆：国内饮料包装机械行业龙头企业',
    '002211': '宏达新材：国内高温混炼胶行业龙头企业',
    '002213': '特 尔 佳：国内汽车电涡缓速器龙头企业',
    '002218': '拓日新能：国内非晶硅太阳能电池芯片龙头企业',
    '002223': '鱼跃医疗：国内基础医疗器械龙头企业',
    '002224': '三 力 士：国内传动带行业龙头企业',
    '002225': '濮耐股份：国内钢铁耐火材料的领先者',
    '002232': '启明信息：国内汽车业IT行业龙头企业',
    '002243': '通产丽星：国内化妆品塑料包装行业龙头企业',
    '002246': '北化股份：全球最大的硝化棉生产企业',
    '002254': '烟台氨纶：国内氨纶行业龙头企业',
    '002258': '利尔化学：国内氯代吡啶类除草剂系列农药龙头业',
    '002265': '西仪股份：国内最大汽车发动机连杆专业生产企业',
    '002270': '法因数控：国内专用数控成套加工设备龙头企业',
    '002282': '博深工具：国内最大金刚石工具厂商',
    '002283': '天润曲轴：国内重型发动机曲轴龙头企业',
    '002284': '亚太股份：国内汽车制动系统专业龙头企业',
    '002309': '中利科技：国内阻燃耐火软电缆龙头企业',
    '002314': '雅致股份：国内集成房屋的龙头企业',
    '002335': '科华恒盛：国内最大UPS供应商',
    '002337': '赛象科技：国内橡胶机械制造业的龙头企业',
    '002341': '新纶科技：国内防静电/洁净室行业龙头企业',
    '002343': '禾欣股份：国内PU合成革行业龙头企业',
    '002346': '柘中建设：国内PHC管桩行业龙头企业',
    '002347': '泰尔股份：国内冶金行业用联轴器领域龙头企业',
    '002348': '高乐股份：国内玩具行业龙头企业',
    '002373': '联信永益：国内党政通信公司市场占有率第一',
    '002389': '南洋科技：国内高端聚丙烯电子薄膜行业龙头',
    '002402': '和 而 泰：国内智能控制器行业龙头企业',
    '002403': '爱 仕 达：国内炊具行业龙头企业',
    '002406': '远东传动：国内最大的非等速传动轴生产企业',
    '002407': '多 氟 多：全球氟化盐龙头企业',
    '002408': '齐翔腾达：国内规模最大的甲乙酮生产企业',
    '002409': '雅克科技：国内最大的有机磷系阻燃剂生产商',
    '002410': '广 联 达：国内最大的工程造价软件企业',
    '002411': '延安必康：国内医药中间体龙头企业',
    '002414': '高德红外：国内规模最大的红外热像仪生产厂商',
    '002423': '中原特钢：国内大型特殊钢精锻件龙头企业',
    '002428': '云南锗业：国内锗产品龙头企业',
    '002430': '杭氧股份：国内最大空分设备和石化设备生产商',
    '002436': '兴森科技：国内最大专业印制电路板样板生产商',
    '002438': '江苏神通：国内冶金特种阀门与核电阀门龙头企业',
    '002444': '巨星科技：国内手工具行业龙头企业',
    '002445': '中南重工：国内最大工业金属管件制造商',
    '002446': '盛路通信：国内通信天线领域领先企业',
    '002448': '中原内配：亚洲最大气缸套生产企业',
    '002449': '国星光电：国内LED封装龙头企业',
    '002453': '天马精化：国内专用化学品细分领域龙头',
    '002454': '松芝股份：国内领先的汽车空调制造商',
    '002455': '百川股份：国内醋酸丁酯，偏苯三酸酐的龙头企业',
    '300001': '特 锐 德：国内铁路电力远动箱式变电站龙头',
    '300004': '南风股份：国内核电HVAC市场龙头企业',
    '300007': '汉威电子：国内气体传感器领先企业',
    '300011': '鼎汉技术：国内轨道交通电源系统龙头企业',
    '300012': '华测检测：国内民营第三方检测的龙头企业',
    '300016': '北陆药业：国内医药对比剂行业领跑者',
    '300018': '中元华电：国内电力二次设备子行业领先者',
    '300019': '硅宝科技：国内有机硅新材料下游龙头企业',
    '300022': '吉峰农机：国内农机连锁销售龙头企业',
    '300024': '机 器 人：国内工业机器人产业先驱',
    '300026': '红日药业：血必净注射液等产品垄断细分市场',
    '300027': '华谊兄弟：国内电影行业龙头企业',
    '300030': '阳普医疗：国内真空采血系统行业龙头企业',
    '300031': '宝通带业：国内耐高温输送带市场领导者',
    '300032': '金龙机电：国内最大的超小型微特电机生产商',
    '300037': '新 宙 邦：国内电子化学品生产龙头企业',
    '300041': '回天胶业：国内工程胶粘剂行业龙头企业',
    '300043': '星辉车模：国内车模行业龙头企业',
    '300045': '华力创通：国内计算机仿真行业领先企业',
    '300046': '台基股份：国内大功率半导体龙头企业',
    '300049': '福瑞股份：国内肝病诊治领域龙头企业',
    '300053': '欧 比 特：国内航天航空及军工领域龙头企业',
    '300054': '鼎龙股份：国内电子成像显像专用信息化学品龙',
    '002400': '省广股份：国内为企业提供品牌管理服务行业龙头',
    '300062': '中能电气：国内中压预制式电缆附件龙头企业',
    '300063': '天龙集团：国内超电子膜行业龙头',
    '300065': '海 兰 信：国内最大的VDR制造企业',
    '300067': '安 诺 其：国内高端燃料行业领跑者',
    '300070': '碧 水 源：国内污水处理领先企业',
    '300072': '三聚环保：国内能源净化行业龙头企业',
    '300073': '当升科技：国内锂电正极材料龙头企业',
    '300074': '华平股份：国内领先的多媒体通信系统提供商',
    '300075': '数字政通：国内数字化城市管理领域龙头',
    '300076': '宁波GQY：国内领先的专业视讯产品制造商',
    '300077': '国民技术：国内USBKEY领域龙头企业',
    '300078': '中瑞思创：国内电子防盗卷标行业龙头企业',
    '300080': '新大新材：国内晶硅片切割刃料领域龙头企业',
    '300082': '奥克股份：国内环氧乙烷精细化工行业龙头',
    '300084': '海默科技：国内油田多相计量领域领先企业',
    '300085': '银 之 杰：国内银行影像应用软件领域领先企业',
    '000569': '长城集团：国内艺术陶瓷行业龙头',
    '300091': '金 通 灵：国内最大的离心风机产品制造商',
    '300093': '金刚玻璃：国内安防玻璃领域龙头企业',
    '300095': '华伍股份：国内工业制动器行业龙头',
    '300097': '智云股份：国内领先的成套自动化装备方案解决商',
    '300099': '尤 洛 卡：国内煤矿顶板灾害防治设备龙头企业',
    '300101': '国腾电子：国内最大的北斗终端供应商',
    '300137': '先河环保：空气质量连续监测系统市场占有率第一',
    '002891': '中宠股份：宠物食品的行业龙头',
    '300672': '国 科 微：广播电视系列芯片和智能监控系列芯片行业龙头',
    '002352': '鼎泰新材：国内稀土合金镀层防腐新材料领域领导者',
    '002152': '北斗星通：国内最大港口集装箱机械导航系统提供商',
    '300066': '三川股份：国内最大节水型机械表和智能水表生产商',
    '002413': '常发股份：国内最大冰箱、空调用蒸发器和冷凝器生产商',
    '002459': '天业通联：国内最大铁路桥梁施工起重运输设备供应商',
    '002420': '毅昌股份：国内规模最大的电视机外观结构件供应商',
    '002443': '金洲管道：国内最大镀锌钢管、螺旋焊管和钢塑复合管供应商',
    '603978': '深圳新星：铝钛硼晶粒细化剂行业龙头，公司是行业内唯一一家拥有完整产业链的铝晶粒细化剂专业制造商'
}


if __name__ == '__main__':
    import os
    print(os.path.dirname(os.path.abspath(__file__)))