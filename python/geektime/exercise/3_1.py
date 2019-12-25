# 练习一 变量的定义和使用
# 定义两个变量分别为美元和汇率
# 通过搜索引擎找到美元兑人民币汇率
# 使用Python计算100美元兑换的人民币数量并用print( )进行输出

# 美元
dollar = 100

# 汇率
exchange = 6.8846

print('{dol}美元兑换的人民币数量为{yuan}'.format(dol=dollar, yuan=dollar * exchange))