'''
	模块
	1. 定义
	2. 格式
	3. 路径
	4. 属性
	5. 标准模块
'''

# 1. 定义
# 	模块是一个包含所有自定义的函数, 类 和 变量的文件
# 	当模块被别的程序引入时, 便可以使用该模块的任意函数 和 变量
# 	Python系统标准库, 也是这么引用的


# 2. 格式
# 	2.1 引用模块
# 	2.2 引用模块中的方法/变量


# 2.1 引用模块
#   import 模块名
# 	模块名.方法名()
# 	模块名.变量名
from 测试.media import demo

print(demo.name)
print(demo.money)
demo.skill()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 2.2 引用模块中的方法/变量
#  	
#  	from 模块名 import 方法名
#  	from 模块名 import 方法名1, 方法名2, ...
#  	from 模块名 import 变量名
#  	from 模块名 import 变量名1, 变量名2, ...

from 测试.media.demo import skill
skill()
# skill2()

from 测试.media.demo import skill, skill2
skill()
skill2()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

from 测试.media.demo import name
print(name)
# print(money)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

from 测试.media.demo import name, money
print(name)
print(money)

# 小结:
# 	单纯的import, 是引入整个模块文件
# 	from ... import ..., 只引用模块中的某些方法/变量
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')






# 3. 路径
# 	import 的模块都存在哪里, 从哪里引入的?

# 查看路径
import sys
print(sys.path)

# 可以看到有以下几个目录:
# 	有Python37-32\ 		安装的根目录
# 	有Python37-32\DLLs 
# 	有Python37-32\lib
# 	有Python37-32\lib\site-packages\
# 	当前目录下  			(该运行文件的目录下)


# 4. __name__ 属性
# 	作用: 自动获取当前模块/引用模块的名字
# 
# 	如果是自身文件被运行, __name__ 返回 __main__ 代表正在运行的是当前主程序
# 	如果是被别的模块引入, __name__返回 引入模块的名字

# import demo
# demo.skill3()

# 使用案例:
# 	模块A 被模块B 第一次引入时, 模块A的主程序将会主动执行
# 	现在想要模块A 被引入时, 模块A的部分不想运行



