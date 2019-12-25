import pysnooper


#@pysnooper.snoop()
def name():
    f = open('name.txt', 'r')
    data = f.read()
    print(data)
    data_split = data.split('|')
    c = f.read().split('|')
    print(data_split)
    f.close()

def weapon():
    f = open('weapon.txt', 'r')
    datas = f.readlines()
    i = 0
    for data in datas:
        if i % 2 == 0:
            print(data, end='')
        i = i + 1

def openfile(filename):
    f = open(filename, 'r')
    #data = f.read()
    for line in f:
        data = line
    f.close()
    return data


if __name__ == '__main__':
    #name()
    #weapon()
    # f = open('sanguo.txt')
    # print(f.read().replace('\n', ''))
    print(openfile('name.txt'))
