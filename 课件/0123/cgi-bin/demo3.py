# 引入 cgi模块
import cgi,cgitb

# 配置 请求头
print('Content-Type: text/html')
print()


# 通过cgi 接收请求的参数(get 或 post方式传递过来的值)
data = cgi.FieldStorage()

# 返回参数
# print(data);
n1 = int(data['a'].value)
n2 = int(data['b'].value)
ope = data['ope'].value


if ope == '+':
	print(n1+n2)
elif ope == '-':
	print(n1-n2)
elif ope == '*':
	print(n1*n2)
elif ope == '/':
	print(n1/n2)

