# 引入 cgi模块
import cgi,cgitb

# 配置 请求头
print('Content-Type: text/html')
print()


# 通过cgi 接收请求的参数(get 或 post方式传递过来的值)
data = cgi.FieldStorage()

# 输出参数

# print(data, type(data) );

# MiniFieldStorage('a', '5')
# 
# 单独获取 a, 通过 name 属性来获取
# 单独虎丘 5, 通过 value 属性来获取
# print(data['a'])
# print(data['a'].name )
# print(data['a'].value)

n1 = int(data['a'].value)
n2 = int(data['b'].value)
res = n1 + n2
print(res)


