# 导包
import socket
# 创建套接字对象
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定ip和端口号
sock.bind(('',8080))
while True:
    # 等待接受消息
    data,addr = sock.recvfrom(1024)

    print('>>>:'+data.decode('utf-8'))
    if data.decode('utf-8') == '886':
        sock.sendto('对方已经离线'.encode('utf-8'), addr)
        break
    # 返回消息
    msg = input('<<<:')
    sock.sendto(msg.encode('utf-8'),addr)

# 关闭套接字
sock.close()