# python基础知识

```python
1.补充缺失的代码
def print_direchory_contents(sPath):

		"""

		合格函数接受文件夹的名称作为输入参数，

		返回该文件夹中文件的路径，

		以及其包含文件夹中文件的路径。

		（注意区分不同平台）

		"""

补充代码:
import os
def print_directory_contents(sPath):
    """
        这个函数接受文件夹的名称作为输入参数，
        返回该文件夹中文件的路径，
        以及其包含文件夹中文件的路径。
    """
    # 遍历获取当前文件路径下的文件路径
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        print(sChildPath)
        # 判断文件下是否含有其他文件,如果有调用原函数继续执行
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
```



```python
2.以下三个输出结果分别是什么?
    def f(x, l=[]):
        for i in range(x):
            l.append(i * i)
        print(l)

    f(2)
    f(3, [3, 2, 1])
    f(3)

    输出结果:
    [0,1]
    [3,2,1,0,1,4]
    [0,1,0,1,4]
```

```python
3.python里面的search()和match()的区别:
答案：
    match（）函数只检测RE是不是在string的开始位置匹配， search()会扫描整个string查找匹配, 也就是说match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
    例如：
    print(re.match(‘super’, ‘superstition’).span())会返回(0, 5)
    而print(re.match(‘super’, ‘insuperable’))则返回None

    search()会扫描整个字符串并返回第一个成功的匹配
    例如：
    print(re.search(‘super’, ‘superstition’).span())返回(0, 5)
    print(re.search(‘super’, ‘insuperable’).span())返回(2, 7)
    match()比较挑剔
```

```python
4.python匹配HTML tag的时候，<.*>和<.*?>有什么区别？
答案：
    贪婪和非贪婪
    贪婪模式在整个表达式匹配成功的前提下，尽可能多的匹配，而非贪婪模式在整个表达式匹配成功的前提下，尽可能少的匹配。
```

```python
5.res = True and False
print(res)
结果为?
	答:False

res = True or False
print(res)
结果为?
	答:True
```

