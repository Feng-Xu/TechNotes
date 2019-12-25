# 练习二 循环语句的使用
# # 使用for语句输出1-100之间的所有偶数
# # 使用while语句输出1-100之间能够被3整除的数字

for i in range(1,101):
    if i % 2 == 0:
        print(i)

n = 1
while n <= 100:
    if n % 3 == 0:
        print(n)
    n = n + 1