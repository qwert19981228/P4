# 引入 cgi模块
import cgi,cgitb


# 配置 请求头
print('Content-Type: text/html')
print()

# 通过cgi 接收请求的参数
fs = cgi.FieldStorage()

# 输出参数
print(fs) 
