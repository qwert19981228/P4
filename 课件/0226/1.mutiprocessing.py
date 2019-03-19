
# 唱歌
def sing():
    for i in range(3):
        print('我在唱第%s首歌。。。'%i)

# 跳舞
def dance():
    for i in range(3):
        print('我在第%s跳舞....'%i)

if __name__ == '__main__':
    sing()
    dance()

'''
问题：是没有同时进行
解决方法：使用多任务处理
'''