# with 上下文管理器
# 上下文管理器最常用的是确保正确关闭文件
# 平时打开文件使用 try...except....finally，如果出现异常，会在finally中close文件
# 但是在with上下文管理器中，发生异常，会自动关闭文件。
with open('sanguo.txt') as f:
    for line in f:
        print(line)


# with基本用法
# with expression [as variable]:
# 　　　 with-block

# expression是一个上下文管理器，其实现了enter和exit两个函数。当我们调用一个with语句时， 依次执行一下步骤，
# 1.首先生成一个上下文管理器expression， 比如open('xx.txt').
# 2.执行expression.enter()。如果指定了[as variable]说明符，将enter()的返回值赋给variable.
# 3.执行with-block语句块.
# 4.执行expression.exit(),在exit()函数中可以进行资源清理工作.
# with语句不仅可以管理文件，还可以管理锁、连接等等
