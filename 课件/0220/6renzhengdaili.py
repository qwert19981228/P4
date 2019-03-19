from urllib import request

base_url = 'http://www.baidu.com/s?wd=ip'

# 创建代理
proxy={
    'http':'http://alice:123456@120.78.166.84:6666',
    'https':'https://alice:123456@120.78.166.84:6666'
}
# 创建代理管理器
proxy_handler = request.ProxyHandler(proxy)
# 自定义请求方法
opener = request.build_opener(proxy_handler)

# 发送请求
response = opener.open(base_url)
print(response.read().decode('utf-8'))
