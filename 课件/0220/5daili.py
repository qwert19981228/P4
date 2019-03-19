from urllib import request

base_url = 'http://www.baidu.com/s?wd=ip'

# 创建代理
proxy={
    'http':'http://180.164.24.165:53281',
    'https':'http://180.164.24.165:53281'
}
# 创建代理对象
proxy_handler = request.ProxyHandler(proxy)
# 自定义请求方法
opener = request.build_opener(proxy_handler)

# 发送请求
response = opener.open(base_url)
print(response.read().decode('utf-8'))
