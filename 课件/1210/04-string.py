'''
    字符串方法
        对象.方法名()

        方法就是函数
        对象: 一切皆对象

        .upper()        全部转为大写
        .lower()        全部转为小写
        .capitalize()   首字母大写
        .title()        每个单词的首字母大写
        .isalnum()      只能有数字, 字母 , 中文
        .isalpha()      只能有字母, 中文
        .isdigit()      只能有数字
        .isupper()      检测是否为大写
        .islower()      检测是否为小写
'''

a = 'I Love You very much'
b = '123'
b = '123.4'
b = 'True'
b = '1+2j'

c = 'abc'
d = 'abc123'

print( a.upper() )
print( a.lower() )
print( a.capitalize() )
print( a.title() )
print( a.swapcase() )
print( b.isalnum() )
print( c.isalpha() )
print( d.isalnum() )

print( b.isdigit() )
print( c.isdigit() )
print( d.isdigit() )

print( c.islower() )
print( c.isupper() )
print( c.isnumeric() )
print( b.isnumeric() )


