def true(): return True

print(true())


# lambda x: x<= (month, day)
# def func1(x):
#     return x <= (month, day)

func3 = lambda item: item[1]

def func2(item):
    return item[0]

adict = {'a':'aa', 'b':'bb'}

for i in  adict.items():
    print(i)
    print(func2(i))
    print(func3(i))