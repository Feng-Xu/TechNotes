import re


def find_item(hero):
    with open('sanguo.txt') as f:
        date = f.read().replace('\n', '')
        name_num = re.findall(hero, date)
    print("%s 出现 %d 次" % (name, len(name_num)))
    return len(name_num)


name_dict = {}
with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for name in names:
            name_dict[name] = find_item(name)
print(name_dict)
