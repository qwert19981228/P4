# 导包
import socket
# 创建套接字对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接
sock.connect(('192.168.1.15',8090))
# 发送信息
sock.send('约吗'.encode('utf-8'))
# 接收消息
data = sock.recv(1024)
print(data.decode('utf-8'))
# 关闭套接字
sock.close()