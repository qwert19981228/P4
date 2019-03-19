```pyuthon
1.给定两个list A/ B, 请用python找到A、B中相同的元素，A、B中不同的元素
答案：
	def handleValue(list1, list2):
		# 判断数据格式
		if isinstance(list1, list) and isinstance(list2, list):
			sameElementList = [ value1 for value1 in list1 if value1 in list2]
			differentElementList = [ value2 for value2 in set(list1+list2) if value2 not in sameElementList]
			print("the list of same element is %s" % sameElementList)
			print("the list of different element is %s" % differentElementList)
		else:
			print("Error value")
答案二:
    A = [1,2,3]
    B = [2,3,4,5,6]
    set1 = set(A)    # 去重
    set2 = set(B)    # 去重
    # 
    print(set1&set2)
    # 非重复值
    print(set1^set2)
```

```python
写出以下程序的输出
    2.1------------
        a = 'abc'
        print(a[1])
        a[1]='a'
        print(a[1])

        答案：
            'b'
            '报错' 
            第二个print(a[1])报错,TypeError,字符串是不可变对象，不能用下标赋值的方式去改变字符串。

    2.2------------
        class Parent(object):
            x = 1

        class Child1(Parent):
            pass

        class Child2(Parent):
            pass

        print(Parent.x,Child1.x, Child2.x)
        Child1.x = 3
        print(Parent.x,Child1.x, Child2.x)
        Parent.x = 'a'
        print(Parent.x,Child1.x, Child2.x)

        答案：  1 1 1
                1 3 1
                a 3 a

    2.3 ------------
        def count():
            fs = []
            for i in range(1, 4):
                def f():
                    return i * i

                fs.append(f)
            return fs

        for f in count():
            print(f())

        答案：
            9
            9
            9
        闭包函数，外函数 count() 再调用结束时会将在内部函数 f() 使用到的临时变量的最终结果值，也传给内部函数。所以此处的 i 都是 3 。
        for f in count(): 遍历是因为 count() 函数的返回值是 内部函数本身 。
```

