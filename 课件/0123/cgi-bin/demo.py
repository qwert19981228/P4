# 引入 cgi模块
import cgi,cgitb

# 配置 请求头
print('Content-Type: text/html')
print()


# 通过cgi 接收请求的参数(get 或 post方式传递过来的值)
fs = cgi.FieldStorage()

# 输出参数
print('111112222333')

# 若以ajax 来访问py文件, 那么py 会以print 方式将数据 返回给ajax
