# 列表内容可以变更，元组不可以变更

# 定义元组
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座'
               , u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# filter(lambda x: x < b, a)  从中找出比b小的值

(month, day) = (2, 15)

zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)

#print(len(list(zodiac_day)))

zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_len)
print(zodiac_name[zodiac_len])


# filter()函数的返回类型叫迭代器
# filter函数返回的内容类似一根长长的管子，里面按顺序依次存好要输出的元素，
# 使用list()函数可以一次性将管子里的数据都取出来，第二次再去取管子中自然是空的了。
# 当然也可以使用__next__()函数每次只取一个元素，根据业务的需要来编写。
a = [1, 2, 3, 4, 5]
b = iter(a)
print(type(a))
print(a)
print(type(b))
print(b)
# 将迭代器b中内容全部取出
print(list(b))
# 再次查看迭代器b中内容
print(list(b))

# 也可以使用__next__()函数每次取一个元素
c = iter(a)
print(c.__next__())
print(c.__next__())


# 列表
a_list = ['abc', 'xyz']
a_list.append('X')
print(a_list)
a_list.remove('xyz')
print(a_list)