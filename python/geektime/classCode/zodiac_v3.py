# 列表内容可以变更，元组不可以变更
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# 定义元组
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座'
               , u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
cz_dic = {}
for i in range(len(chinese_zodiac)):
    cz_dic[chinese_zodiac[i]] = 0

zd_dic = {}
for i in range(len(zodiac_name)):
    zd_dic[zodiac_name[i]] = 0
while True:
    int_year = int(input('请输入年:'))
    int_month = int(input('请输入月份:'))
    int_day = int(input('请输入日期:'))

    n = 0
    while zodiac_days[n] < (int_month, int_day):
        if int_month == 12 and int_day > 23:
            break
        n += 1
    # 输出星座和生肖
    print(zodiac_name[n])
    print('%d 年的生肖是 %s' % (int_year, chinese_zodiac[int_year % 12]))
    cz_dic[chinese_zodiac[int_year % 12]] += 1
    zd_dic[zodiac_name[n]] += 1
    # 输入统计信息
    for each in cz_dic.keys():
        print('%s 生肖有 %d 个' % (each, cz_dic[each]))
    for each in zd_dic.keys():
        print('%s 星座有 %d 个' % (each, zd_dic[each]))