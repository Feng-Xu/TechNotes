from urllib import request

url = "http://www.baidu.com"
response = request.urlopen(url)
#print(response.read().decode('utf-8'))

# 如我们需要 字符串 转换成 字节，可以使用bytes()或encode()进行转换：
s='你好'
b1=s.encode('utf-8') # 使用utf8编码将字符串转换为字节
print(type(b1))
b2=bytes(s, encoding='utf-8') #和上面功能一样

# 那如果将字节转换回字符串呢？
c1 = b1.decode('utf-8')
print(type(c1))
str(b2, encoding='utf-8')
