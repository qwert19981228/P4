# 导包
import socket
# 创建套接字对象
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定ip和端口号
sock.bind(('',8080))
# 等待接受消息
data,addr = sock.recvfrom(1024)

print(data.decode('utf-8'))

# 返回消息
sock.sendto('world'.encode('utf-8'),addr)

# 关闭套接字
sock.close()