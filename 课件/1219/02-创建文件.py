'''
    交互式 创建文件
'''

import os
def create_file(filename):
    # 1. 判断文件是否存在
    #   存在: 则提示已存在
    if os.path.exists(filename):
        return '该文件已存在'

    # 2. 判断文件名 是否含有 特殊字符
    #   含有: 则提示 文件名问题
    special = '/\\|<>?:"*'
    for i in filename:
        if i in special:
            return '输入的文件名不能包含 %s ' % special

    # 3. 创建文件
    # open(filename, 'w')
    # os.system('type null>%s' % filename)
    # print('11111111111')
    return '创建成功'

filename = input('请输入文件名: ')

print( create_file(filename) )





# 常见创建一个文件3个方法:
# 1. open
#       open(文件路径, 'w' 或 'a')       推荐

# 2. system
#       import os
#       os.system('type null>文件路径')

# 3. pathlib模块
#       import pathlib
#       pathlib.Path(文件路径).touch()


# import pathlib
# pathlib.Path('xx.txt').touch()





