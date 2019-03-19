# html提交的数据, 都会传递给指定的 专门的HTTP服务器, 才能做下一步的验证等处理
# 目前常见服务器有Apache, Nginx 等. 
# 那么此时, 我们并没有安装HTTP服务器, 此操作复杂繁琐, 在后期的Django, Flask框架都有很好的web处理. 
# 所以, 目前采用python自带的 http.server 提供的 "乞丐版HTTP服务器", 来体验 html与Python 的交互
# 
# http.server : HTTP服务器和请求处理程序


# 加载 http.server 模块
from http.server import HTTPServer, CGIHTTPRequestHandler

# 设置 web端口, 可修改, 建议改成大点的千位数
port = 8000

# 配置 服务器
# 	http.server.HTTPServer( server_address, RequestHandlerClass )
# 	参数:
# 		1. server_address 服务器地址
# 			需要填写两个值, 常用元组形式写入, 例如 (服务器IP, 端口)
# 			分析: 
# 				服务器IP若为空, 则默认使用当前IP
# 				端口: 正常使用80, 但由于这里是测试, 建议调成1000以上的端口, 防止与原生端口冲突
# 			
# 		2. RequestHandlerClass   请求处理程序类
# 			常用类:
# 				CGIHTTPRequestHandler 	处理http请求
# 	
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('服务器已启动')
httpd.serve_forever() 	# 监听服务器端口, 该文件不能中断, 一旦中断, 服务器就不能正常使用了









