# __init__方法的第一参数永远是self，表示创建的类实例本身，
# 在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器会自己把实例变量传进去


class Player():
    def __init__(self, name_wai, hp_wai, sex, num):
        self.name = name_wai
        self.hp = hp_wai
        # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线,私有变量（private）
        self.__sex = sex
        # 以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
        # 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
        self._num = num
        print(self)

    def print_role(self):
        print("name: %s, hp: %s" % (self.name, self.hp))

    def get_sex(self):
        print(self.__sex)


user1 = Player('tom', 88, 'man', 1)
user2 = Player('jerry', 90, 'man', 2)
# user3 = Player()

user1.print_role()
user2.print_role()

print(user1.name)
# AttributeError: 'Player' object has no attribute '__sex'
# print(user1.__sex)
user1.__sex = 'female'
user1.get_sex()
print(user1._num)

print('====================')


class Monster():
    def __init__(self, hp):
        self.hp = hp

    def run(self):
        print('移动到某位置')

    def whoami(self):
        print('我是Monster')


class Animals(Monster):
    def __init__(self):
        super().__init__(hp=10)


class Boss(Monster):
    def whoami(self):
        print('我是Boss')


a1 = Monster('100')
print(a1.hp)
a1.run()
a2 = Animals()
print(a2.hp)
a2.run()

a3 = Boss(900)
print(a3.hp)
a3.whoami()

print(type(a1))
print(type(a2))
print(type(a3))

# 判断是否Monster的子类
print(isinstance(a2, Monster))

print('=============')


class FatherA(object):
    def __init__(self):
        print("in FatherA")


class FatherB(object):
    def __init__(self):
        print("in FatherB")


class SonC(FatherB, FatherA):
    pass


# 如果多个父类有相同的方法，并且子类里面没有声明，它会从左至右搜索
songc = SonC()
