import re
# 变量1 = re.compile(正则表达式)
# 变量2 = 变量1.match(要匹配的字符串)

# .: 匹配单个任意字符
# ^: 表示从开头开始搜索
# $: 表示末尾匹配
# *: 匹配前面的字符，0次或者多次
# +: 前面的字符，出现1次或者多次
# ?: 前面的字符，出现0次或者1次
# {}: 前面的字符，出现指定的次数   ca{4}t    ca{4,6}t
# []: 括号中任意字符匹配成功，均能匹配    c[bcd]t
# \d: 匹配内容是一个数字
# \D: 匹配不包含数字的
# \s: 匹配任意空白符    制表符\t 换行符\n 等
# \S: 匹配非空白符
# (): 进行分组
# ^$: 表示匹配空行
# .*?: 不适用贪婪模式



p = re.compile(r'(\d+)-(\d+)-(\d+)')
# 取出年份
# match是完全匹配，然后进行分组，相当于自带了^
print(p.match('2019-05-27').group(1))
print(p.match('2019-05-27').groups())
year, month, day = p.match('2019-05-27').groups()


# search() 不要求原字符和正则完全匹配，用于搜索字符串
print(p.search('aa2019-05-27'))

phone = '123-4567-7890 # 这是电话号码'
p2 = re.sub(r'#.*$', '', phone)
print(p2)
p3 = re.sub(r'\D', '', p2)
print(p3)

#match  search方法只能匹配第一个，不能搜索所有的

# 只能匹配第一个'-'
p0 = re.compile(r'\D')
print(p0.search('2019-05-27'))
# findall() 匹配所有的
p4 = p0.findall('2019-05-27')
print(p4)
# <re.Match object; span=(4, 5), match='-'>
# ['-', '-']