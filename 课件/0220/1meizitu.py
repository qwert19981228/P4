from urllib import request

base_url = 'https://i.meizitu.net/thumbs/2017/09/103952_26b31_236.jpg'

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1550623188,1550623272; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1550623337",
    "referer": "https://www.mzitu.com/japan/",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
}

req = request.Request(url = base_url,headers=headers)

# 发送请求
response = request.urlopen(req)
img = response.read()

with open('meizi.jpg','wb') as f:
    f.write(img)