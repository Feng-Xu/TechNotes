# 记录十二生肖，根据年费判断生效

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

#print(chinese_zodiac[0:4])

#print(chinese_zodiac[-2])

year = 2018

print(year%12)

print(chinese_zodiac[year % 12])

print('狗' in chinese_zodiac)

print(chinese_zodiac + "heheheheh")
print(chinese_zodiac * 2)