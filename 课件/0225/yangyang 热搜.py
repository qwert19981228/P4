# ! /usr/bin/env python
import json, jsonpath, time
import requests

url = 'https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=filter_type%3Drealtimehot%26mi_cid%3D100103%26pos%3D0_0%26c_type%3D30%26display_time%3D1551057682&luicode=10000011&lfid=231583'
headers = {
    # 'MWeibo-Pwa': 1,
    'Referer': 'https://m.weibo.cn/p/index?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=filter_type%3Drealtimehot%26mi_cid%3D100103%26pos%3D0_0%26c_type%3D30%26display_time%3D1551057682&luicode=10000011&lfid=231583',
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

title = jsonpath.jsonpath(jsoncontent, '$.data.cards[0].card_group[*].desc')
# print(len(title))
scheme = jsonpath.jsonpath(jsoncontent, '$.data.cards[0].card_group[*].scheme')
# print(len(scheme))

storelist = []
for i, j in zip(title, scheme):
    storedict = {
        'title': i,
        'scheme': j
    }
    storelist.append(storedict)

with open('3hotsearch_v1.1.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(storelist, indent=4, ensure_ascii=False))torelist, indent=4, ensure_ascii=False))