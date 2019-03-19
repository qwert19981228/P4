```python
1.python2和python3的区别
    #1.Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')
    #2.python2 range(1,10)返回列表，python3中返回迭代器，节约内存
    #3.python2中使用ascii编码，python中使用utf-8编码
    #4.python2中unicode表示字符串序列，str表示字节序列，python3中str表示字符串序列，byte表示字节序列
    #5.python2中为正常显示中文，引入coding声明，python3中不需要
    #6.python2中是raw_input()函数，python3中是input()函数
```

```python
2.请使用python内置函数处理如下问题：
	1.请判断一个字符串是否以er结尾；
	2.请将“#teacher#”两侧的“#”去除；
	3.请使用map函数将[1,2,3,4]处理成[1,0,1,0];
	4.请使用filter函数将[1,2,3,4]处理成[2,4];
	5.请使用reduce函数计算100的阶乘；
      #1.var1.endswith('er')	返回的是true

      #2.str.replace("#","")	返回的是teacher

      #3. #def square(x) :
          #if x%2 == 0:
              #print(0)
          #else:
              #print(1)
      #map(square, [1,2,3,4])

      #4.def is_odd(n):
          #return n % 2 == 0
      #tmplist = filter(is_odd, [1,2,3,4])
      #newlist = list(tmplist)
      #print(newlist)

      #5. #from functools import reduce
          #def prod(L):
              #def myCheng(x,y):
                  #return x*y
              #return reduce(myCheng,L)

          #varlist = []
          #for i in range(1,101):
              #varlist.append(i)
          #print(prod(varlist))
```

```python
3.定义A = [1,2,3,4] 使用列表生成式[i*i for i in A]生成列表为：
	A: [1,2,3,4]
	B: [1,4,9,16]
	C: [1,4,6,8]
	D: [1,4,9,12]
	答案：B
```

```python
4.定义A=("a","b","c","d"),执行del A[2]后的结果为：
	A：("a","b","d")
	B: ("a","b","c")
	C: ("a","c","d")
	D：异常
    答案：D
    解析：元组对象不支持项删除。
```

```python
5.输出结果是什么？
	list1 = ['a','b','c','d','e']
	print(list1[10:])
	答案：
		[]
```

