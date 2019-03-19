import requests

# 地址
base_url = 'http://www.baidu.com/s?'
# base_url = 'http://www.xicidaili.com/s?'
data={
    'wd':'美女'
}

# 发送请求
response = requests.get(base_url,params=data)
print(response.status_code)
response.encoding='utf-8'
print(response.text)
# print(response.content.decode('utf-8'))