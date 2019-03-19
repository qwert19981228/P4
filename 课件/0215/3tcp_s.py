# 导包
import socket
# 创建套接字对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定ip和端口号
sock.bind(('',8090))
# 监听 队列
sock.listen()
# 接收 sock对象，客户端地址
s,addr = sock.accept()
data = s.recv(1024)
print(data.decode('utf-8'))
s.send('约'.encode('utf-8'))
# 关闭套接字
sock.close()