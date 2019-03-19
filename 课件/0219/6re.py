import re
str = '<a href="www.baudi.com">百度</a>'
html = '''
    <ul>
        <li class="active" id="1">吃饭啦</li>
        <li>下课吧</li>
        <li>告辞</li>
    </ul>
    <div>
        <a href="www.baidu.com"
        >百度</a>
        <a href="www.xiaomi.com">小米</a>
    </div>
'''

# 制定规则
# reg = re.compile(r'<li.*>.*</li>')
reg = re.compile(r'<a href="(.*)">.*</a>',re.S)
# 检索匹配字符串
res = reg.findall(html)
print(res)