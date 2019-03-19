## python基础题目

```python
1.请写出三种方式,实现一个字符串反转的函数：（例如，输出：'hello python' 输出：'nohtyp olleh'）

答案:
    1.使用字符串切片
    def reverse1():
        s = input("please input a string: ")
        return s[::-1]

    print(reverse1())

    2.使用递归
    def reverse2(s):
        if s == "":
            return s
        else:
            return reverse2(s[1:]) + s[0]

    str = 'hello python'
    print(reverse2(str))


    3.使用列表的reverse
    def reverse3(s):
        l = list(s)
        l.reverse()
        print("".join(l))
    reverse3('hello python')
  
2.string = "{1},{0}";string = string.format('hello','python'),请问将string打印结果为：
	A：hello，python			
	B：{1}，{0}
	C：python，hello
	D: hello，hello
    答案：C
    
3.请使用python内置函数处理如下问题：
	1请判断一个字符串是否以er结尾；
    2请将‘#teacher#’两侧的#去除；
答案：
    1.res = str1.endswith('er')
    2.res = str1.strip('#')
    # 解析:字符串操作
    
4.现从一个需要登录的简单网站获取信息，请使用python简要的写出登录函数 的具体实现（登录信息只包含username,password）
    def login(username, password):
        url = "https:xxxxxx"
        data = {"uname":username, "pwd":password}
        response = requests.post(url,data=data)
        return response.content.decode()
    
5.介绍一下python下range()函数的用法？
    range(1,5)#代表从1到5（不包含5）
    range(1,5,2)#代表从1到5，间隔2（不包含5）
    range(5)#代表从0到5（不包含5）
    range(0, -10, -1) # 负数
	[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    range(0)   []
	range(1, 0)    []

```

