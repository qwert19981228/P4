# 加载 服务器相关模块
from http.server import HTTPServer, CGIHTTPRequestHandler

# 设置 web端口, 可修改, 建议改成大点的千位数
port = 8044

# 开启服务器
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('服务器已启动')
httpd.serve_forever() 	# 监听服务器端口, 该文件不能中断, 一旦中断, 服务器就不能正常使用了




