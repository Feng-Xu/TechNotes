import os

#获取绝对路径
print(os.path.abspath('.'))
# 判断文件是否存在
print(os.path.exists('/Users'))
# 判断是否文件
print(os.path.isdir('/Users'))

# 路径的拼接
print(os.path.join('/tmp/a', 'b'))

from pathlib import Path
p = Path('.')
print(p.absolute())
print(p.resolve())

# 创建目录
path1 = Path('/tmp/a/b/c')
Path.mkdir(path1, parents=True)