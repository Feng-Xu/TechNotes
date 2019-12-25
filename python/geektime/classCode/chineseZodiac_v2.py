# 记录十二生肖，根据年费判断生效

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

#print(chinese_zodiac[0:4])

#print(chinese_zodiac[-2])

# year = int(input('请输入年份：'))
# if chinese_zodiac[year % 12] == '狗' :
#     print('狗年很旺')


for cz in chinese_zodiac:
    print(cz)

for i in range(1, 13):
    print(i)

for year in range(2000, 2020):
    print('%s 年的生效是 %s' %(year, chinese_zodiac[year % 12]))

import time
num = 5
while True:
    num = num + 1

    if num == 10:
        continue

    print(num)
    time.sleep(1)