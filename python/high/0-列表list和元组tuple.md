## 列表list和元组tuple
### 列表和元组的基础
列表和元组都是一个可以**放置任意元素的有序集合**  
```python
>>> list1 = [1, 2, 'qwer', 'asdf']
>>> list1
[1, 2, 'qwer', 'asdf']
>>> tup1 = (1, 2, 'asd', '123df')
>>> tup1
(1, 2, 'asd', '123df')
```
* **列表是动态的**，长度不固定，可以随意增加、删减或者改变元素（mutable）
* **元组是静态的**，长度固定，不能增加、删减和改变（immutable）
```python
>>> list1[3] = 'python'
>>> list1
[1, 2, 'qwer', 'python']
>>> tup1[3] = 'python'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
如果想对已有的元组有改变，那只能重新创建一个元组，对原来的元组进行操作。
```python
>>> new_tup1 = tup1 + ('1111',)
>>> new_tup1
(1, 2, 'asd', '123df', '1111')
>>> list1.append('1111')
>>> list1
[1, 2, 'qwer', 'python', '1111']
```
**列表和元组都支持负数索引**  
**列表和元组都支持切片操作**  
**列表和元组都支持随意嵌套**  
**列表和元组都支持相互转换list() & tuple()**  
列表和元组的常用的内置函数：  
```python
>>> l = [3, 2, 3, 7, 8, 1]
>>> l.count(3)
2
>>> l.index(7)
3
>>> l.reverse()
>>> l
[1, 8, 7, 3, 2, 3]
>>> l.sort()
>>> l
[1, 2, 3, 3, 7, 8]
>>>
>>> tup = (3, 2, 3, 7, 8, 1)
>>> tup.count(3)
2
>>> tup.index(7)
3
>>> reversed(tup)
<reversed object at 0x10354a438>
>>> list(reversed(tup))
[1, 8, 7, 3, 2, 3]
>>> sorted(tup)
[1, 2, 3, 3, 7, 8]
```
以上这几个函数的含义：  
* count(item) 表示统计列表 / 元组中 item出现的次数。  
* index(item) 表示返回列表 / 元组中item 第一次出现的索引。
* List.reverse() 和 list.sort() 分别表示原地倒转列表和排序（注意，元组没有内置的这两个函数)。
* reversed() 和 sorted() 同样表示对列表 / 元组进行倒转和排序，但是会返回一个倒转后或者排好序的新的列表 / 元组。
### 列表和元组的不同
列表是动态的，可变的，元组是静态的，不可变的，这两的差异会引起两者存储方式的不同。具体下面：
```python
>>> l
[1, 2, 3, 3, 7, 8]
>>> tup
(3, 2, 3, 7, 8, 1)
>>> l.__sizeof__()
88
>>> tup.__sizeof__()
72
```
上面列表和元组中存储相同的元素，但是元组比列表的存储空间少16字节。事实上，由于列表是动态的，所以它需要**存储指针**，来指向对应的元素（上述例子中，对于int型，8字节。如果是其他数据类型那么字节数会有变化，不一定是16）。另外由于列表可变，所以需要额外存储已经分配的长度大小（8字节），这样才可以实时追踪列表空间的使用情况，当空间不足时，及时分配额外空间。
```python
l = []
l.__sizeof__() // 空列表的存储空间为 40 字节
40
l.append(1)
l.__sizeof__() 
72 // 加入了元素 1 之后，列表为其分配了可以存储 4 个元素的空间 (72 - 40)/8 = 4
l.append(2) 
l.__sizeof__()
72 // 由于之前分配了空间，所以加入元素 2，列表空间不变
l.append(3)
l.__sizeof__() 
72 // 同上
l.append(4)
l.__sizeof__() 
72 // 同上
l.append(5)
l.__sizeof__() 
104 // 加入元素 5 之后，列表的空间不足，所以又额外分配了可以存储 4 个元素的空间
```
上述的例子，大概描述了列表的空间分配的过程。从上述我们可以看到，为了减少每次增加/删减操作时空间分配的开销，python每次分配空间时都会额外多分配一些，这样的机制（over-allocating）保证了其操作的高效性：增加或者删除的时间复杂度为O(1)。
### 列表和元组的性能
从存储的角度来看，元组比列表要轻量，所以总体来说，元组的性能比列表要高。  
另外，python会在后台对静态资源做**资源缓存**。通常来说，由于垃圾回收机制存在，如果一些变量不被使用，python会回收他们内存，返回给操作系统。但是作为一些静态资源，比如元组，如果它不被使用且占用空间不大时，python会对暂时缓存这些内存，这样下次再创建同样大小的元组时，python就可以不再向操作系统发出请求，去寻找内存，而是可以直接分配之前的缓存的内存空间，这样就大大加快程序运行的速度。 
下面的例子，是计算初始化一个相同元素的列表和元组分别所需的时间，元组的初始化速度要明显快于列表
```python
xufeng@xufengdeMacBook-Air ~ python -m timeit 'x=(1,2,3,4,5,6)'
20000000 loops, best of 5: 14.5 nsec per loop
xufeng@xufengdeMacBook-Air ~ python -m timeit 'x=[1,2,3,4,5,6]'
2000000 loops, best of 5: 94.4 nsec per loop
``` 
但是如果索引操作的话，两者的速度差别很小：
```python
xufeng@xufengdeMacBook-Air ~ python -m timeit -s 'x=(1,2,3,4,5,6)' 'y=x[3]'
10000000 loops, best of 5: 35.4 nsec per loop
xufeng@xufengdeMacBook-Air ~ python -m timeit -s 'x=[1,2,3,4,5,6]' 'y=x[3]'
10000000 loops, best of 5: 35 nsec per loop
```
但是，增加和删除操作肯定是列表最优，因为元组需要新创建个元组来执行。  
### 列表和元组的使用场景
1. 如果存储的数据和数量不变，比如你有一个函数，需要返回一个地点的经纬度，直接给前端渲染，那么元组合适。  
2. 如果数据是可变的，比如社交平台上的一个日志功能，是统计一个用户在一周之内看了哪些帖子，那么用列表更合适
### 思考
下列哪种方式，性能更优
```python
# 创建空列表
# option A
empty_list = list()

# option B
empty_list = []
```
方式B性能更高：  
区别主要在于list()是一个function call，Python的function call会创建stack，并且进行一系列参数检查的操作，比较expensive，反观[]是一个内置的C函数，可以直接被调用，因此效率高。
内存分配，GC等等知识会在第二章进阶里面专门讲到。
```python
>>> dis.dis(lambda : dict())
  1 0 LOAD_GLOBAL 0 (dict)
              3 CALL_FUNCTION 0 (0 positional, 0 keyword pair)
              6 RETURN_VALUE

>>> dis.dis(lambda : {})
  1 0 BUILD_MAP 0
              3 RETURN_VALUE
```
可以看到dict()中多了CALL_FUNCTION过程，所以性能低
