# ! /usr/bin/env python
import requests, time, jsonpath, json

# https://m.weibo.cn/search?containerid=231583

# uid: 1195242865
# luicode: 10000011
# lfid: 100103type=1&q=杨幂
# type: uid
# value: 1195242865
# containerid: 1005051195242865
# url = 'https://m.weibo.cn/api/container/getIndex?uid=1195242865&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%9D%A8%E5%B9%82&type=uid&value=1195242865&containerid=1005051195242865'

# 发送请求
url = 'https://m.weibo.cn/api/container/getIndex?uid=1195242865&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%9D%A8%E5%B9%82&type=uid&value=1195242865&containerid=1076031195242865'
headers = {
    # MWeibo-Pwa: 1
    'Referer': 'https://m.weibo.cn/u/1195242865?uid=1195242865&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%9D%A8%E5%B9%82',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest'
}
proxy = {
    'http': 'http://alice:123456@120.78.166.84:6666',
    'https': 'https://alice:123456@120.78.166.84:6666',
}
time.sleep(3)
response = requests.get(url, headers=headers, proxies=proxy)
jsoncontent = response.json()
print(jsoncontent)

# 获取到数据
scheme = jsonpath.jsonpath(jsoncontent, '$.data.cards[*].scheme') # 详情url
created_at = jsonpath.jsonpath(jsoncontent,'$.data.cards[*].mblog.created_at') # 时间
text = jsonpath.jsonpath(jsoncontent, '$.data.cards[*].mblog.text') # blog内容
reposts_count = jsonpath.jsonpath(jsoncontent, '$.data.cards[*].mblog.reposts_count') # 转发数
comments_count = jsonpath.jsonpath(jsoncontent, '$.data.cards[*].mblog.comments_count') # 评论数
attitudes_count = jsonpath.jsonpath(jsoncontent, '$.data.cards[*].mblog.attitudes_count') # 点赞数
total = jsonpath.jsonpath(jsoncontent, '$.data.cardlistInfo.total')[0] # 总博客数
# print(scheme)
# print(created_at)
# print(text)
# print(reposts_count)
# print(comments_count)
# print(attitudes_count)
print(total)

# 数据的结构处理
storelist = []
for a, b, c, d, e, f in zip(text, scheme, created_at, reposts_count, comments_count, attitudes_count):
    storedict = {
        'title': a,
        'scheme': b,
        'created_at': c,
        'reposts_count': d,
        'comments_count': e,
        'attitudes_count': f
    }
    storelist.append(storedict)

# 数据写入本地
with open('weibosearch.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(storelist, indent=4, ensure_ascii=False))





























