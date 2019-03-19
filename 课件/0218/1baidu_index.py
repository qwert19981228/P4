from urllib import request

# 确定url地址
base_url = 'http://www.baidu.com'

# 发送请求
response = request.urlopen(base_url)

# 处理响应信息
html = response.read().decode('utf-8')

with open('./baidu.html','w',encoding='utf-8') as f:
    f.write(html)