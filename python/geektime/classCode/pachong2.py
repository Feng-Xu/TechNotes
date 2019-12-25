import requests
import re

response = requests.get('http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F')
#print(response.text)


# image_str = '<a href="http://www.cnu.cc/works/318906" class="thumbnail" target="_blank">\
#                         <div class="title">\
#                             ”心内的一场雨”\
#                             </div>\
#                         <div class="author">\
#                             darling安老师\
# \
#                         </div>'

# print(image_str)
# # .*?为懒惰模式，匹配到第一个"就停止匹配，因为它懒惰
# pattern = re.compile(r'<a href="(.*?)".*title">(.*?)</div>')
# print(re.match(pattern, image_str).groups())

# .*?为懒惰模式，匹配到第一个"就停止匹配，因为它懒惰
# re.S叫做单行模式，简单来说，就是你用正则要匹配的内容在多行里，会增加你要匹配的难度，
# 这时候使用re.S把每行最后的换行符\n当做正常的一个字符串来进行匹配的一种小技巧
pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, response.text)
for result in results:
    url, name = result
    # 使用re.sub('\s') 将 空格和换行等字符替换掉
    print(url, re.sub('\s', '', name))
