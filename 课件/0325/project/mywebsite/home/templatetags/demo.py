from django import template
register = template.Library()


# 自定义过滤器
@register.filter  #  告诉你 我是注册过滤器
def kong_upper(val):
    # print ('val from template:',val)
    return val.upper()

# 自定义标签
from django.utils.html import format_html
@register.simple_tag   #  告诉你 我是注册自定义标签
def jia(a,b):
    res = int(a) + int(b)
    return res

#课堂作业
#自定义标签
# 获取导航栏
# data = ['首页','女装','汉服','cosplay']
# # 直接return
@register.simple_tag
def getnav():
    data = ['首页','女装','汉服','cosplay']
    html = ''
    for i in data:
        html += '<li>'+i+'</li>'

    return format_html(html)
