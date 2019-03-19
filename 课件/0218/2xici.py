from urllib import request
import ssl
# 确定url地址
base_url = 'https://www.xicidaili.com'
# 关闭ssl认证
ssl._create_default_https_context = ssl._create_unverified_context
# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}
req = request.Request(url=base_url,headers=headers)
# 发送请求
response = request.urlopen(req)

# 处理响应
html=response.read().decode('utf-8')

with open('./xici.html','w',encoding='utf-8') as f:
    f.write(html)