# python基础知识

```
1.优化一下下面的程序
	result = []
	for x in range(10):
		result.append(x ** 2)
	print(result)
答案:
result = [ (x ** 2) for x in range(10)]
print(result)
用列表推导式的方式优化了上面的程序
```

```python
2.说说dict的items()方法与iteritems()方法的不同

dict.items()返回的是一个完整的列表，而dict.iteritems()返回的是一个生成器(迭代器)。
dict.items()返回列表list的所有列表项，形如这样的二元组list：［(key,value),(key,value),...］
dict.iteritems()是generator, yield 2-tuple。相对来说，前者需要花费更多内存空间和时间，但访问某一项的时间较快(KEY)。后者花费很少的空间，通过next()不断取下一个值，但是将花费稍微多的时间来生成下一item。
```

```python
3.utf-8和unicode的区别是什么？
	Unicode 是「字符集」
    UTF-8 是「编码规则」
    字符集：为每一个「字符」分配一个唯一的 ID（学名为码位 / 码点 / Code Point）
    编码规则：将「码位」转换为字节序列的规则（编码/解码 可以理解为 加密/解密 的过程）
    广义的 Unicode 是一个标准，定义了一个字符集以及一系列的编码规则，即 Unicode 字符集和 UTF-8、UTF-		16、UTF-32 等等编码……
	Unicode 字符集为每一个字符分配一个码位，例如「知」的码位是 30693，记作 U+77E5（30693 的十六进制为 	   0x77E5）。
	UTF-8 顾名思义，是一套以 8 位为一个编码单位的可变长编码。会将一个码位编码为 1 到 4 个字节：
```

```python
4.复杂列表[{"k":1,"v":2},{"k":12,"v":22},{"k":13,"v"}]，请用内置方法写出按K的倒序排列的代码 
答案：	
li = [{"k":1,"v":2},{"k":12,"v":22},{"k":13,"v":32}]
li.sort(key=lambda dict:dict["k"],reverse=True)
print(li)
```

```python
5.字典d = {'k':1,'v':2},请写出d.items()的结果

答案：
		[('k', 1), ('v', 2)]
```

