from bs4 import BeautifulSoup

text = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title sister">1234<b>The Dormouse's story</b></p>
<div>
    <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link1">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>
</div>

<p class="story">...</p>
<div>欢迎收看</div>
<div class="item">
    <div class="inner1">
        <div class="inner1"></div>
    </div>
</div>
"""

html = BeautifulSoup(text,'lxml')

# print(html.prettify())

#  元素选择器 对象.标签名 只获取第一个标签
# print(html.p)
# print(html.p.name)

# 获取文本
# string  如果当前标签中只有字标签没有其他文本内容那么可以获取到子标签的内容
        # 如果当前标签有文本内容而且还有字标签 那么直接返回none
# obj.element.get_text()
# obj.element.text     结果相同 不管有没有字标签 获取当前标签和子标签的内容
# print(html.title.string)
# print(html.p.string)
# print(html.p.get_text())
# print(html.p.text)


# 获取属性 第一种只能获取指定属性的值 第二种获取标签所有的属性 字典类型
# print(html.a['href'])
# print(html.a.attrs)

# 筛选
# print(html.find(class_="sister"))
# els = html.find_all('p')
# els = html.find_all(class_='sister')
# print(els)
# for i in els:
#     print(i.text)

# 获取指定标签带有指定属性的值
# els = html.find_all('a',attrs={'id':'link1'})
# print(els)

# 指定标签同时满足多个条件
# els = html.find_all('a',attrs={'class':'sister','id':'link1'})
# print(els)

# 获取只要满足一个条件的
# els = html.find_all(['p','a'])
# print(els)

#选择器

# 获取class类名为title的p标签
# res = html.select('p.title')
# print(res)

# 获取类名为  类选择器
# res= html.select('.sister')
# print(res)

# id选择器
# 获取id为link1
# res = html.select('#link1')
# print(res)

# 获取div中的p标签 后代
# res = html.select('div p')
# print(res,type(res[0]))

# 获取.item下的所有的inner1
# res = html.select('.item .inner1')
# print(res)

#获取item下的 子元素
# res = html.select('.item > .inner1')
# print(res)

# 同时获取.item 和 p class="story"
# res = html.select('.item,p[class=story]')
# print(res)

# 获取类名以指定字符开头的元素
# res = html.select('p[class^=t]')
# print(res)

# 以指定字符结尾的
# res = html.select('p[class$=y]')
# print(res)

# 包含指定字符
res = html.select('p[class*=t]')
print(res[0].get('class'))