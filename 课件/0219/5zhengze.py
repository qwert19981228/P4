# 正则
    # 按照一定的规则检索匹配 字符串
    # 普通字符
    # 转义字符
        # \w  \d \s \W \D \S
    # 修饰符
        # * . + ? ^ $ () | [] {}

    # 制定匹配规则
    # reg = re.compile('规则')
    # res = reg.search('目标字符串') 如果匹配到了就返回类对象(返回第一个匹配到的对象)  没有就返回None
    # res.group()   返回检索到的字符
import re

# 字符串
str = '''qwe123@_ _w_w\\wA/A.b\ai456du.comA'''

# 制定规则
# reg = re.compile('y')
# reg = re.compile('\n')
# reg = re.compile('\w.+')
# reg = re.compile('A+')
# reg = re.compile('.+')
# reg = re.compile('\w*')
# reg = re.compile('\d+?')
# reg = re.compile('.*?')   # 禁止贪婪
# reg = re.compile(r'\\')
# reg = re.compile(r'\.')
# reg = re.compile('.*(\d).*')  # qwe1@_ _w_w\\wA/A.b\aidu.comA    -->1
# reg = re.compile('.*(\d)(\d).*') # qwe123@_ _w_w\\wA/A.b\ai456du.comA --->5
# reg = re.compile('.*?(\d)(\d).*') # qwe123@_ _w_w\\wA/A.b\ai456du.comA --->1
str = r'''zhanghuanyu@i\\txdl.+org'''
# reg = re.compile('.*\.(cn|com|org)')
# reg = re.compile('.{5,10}')
# reg = re.compile(r'\\\\')
# 在【】中的.*+\都是普通字符 没有特殊意义
reg = re.compile(r'[a-z@\\.+\w]+')

# 检索匹配
res = reg.search(str)

if res:
    print(res.group())

    # print(res.group(2))
else:
    print('没有匹配到数据')




