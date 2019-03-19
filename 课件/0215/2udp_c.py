# 导包
import socket
# 创建套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定ip和端口
sock.bind(('',8000))
while True:
    # 发送消息
    msg = input('<<<:')
    sock.sendto(msg.encode('utf-8'),('192.168.1.15',8080))
    # 接受消息
    data,addr = sock.recvfrom(1024)
    print('>>>:'+data.decode('utf-8'))
# 关闭套接字
sock.close()