# 从1 到 10 的偶数的平方

alist = []
for i in range(1, 11):
    if(i % 2 == 0):
        alist.append( i*i )
print(alist)

blist = [i*i for i in range(1, 11) if(i % 2 == 0)]
print(blist)

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座'
               , u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座')
zn_dic = {}
for i in range(len(zodiac_name)):
    zn_dic[zodiac_name[i]] = 0
print(zn_dic)

zn_dic_v1 = {zodiac_name[i]:0 for i in range(len(zodiac_name))}
print(zn_dic_v1)