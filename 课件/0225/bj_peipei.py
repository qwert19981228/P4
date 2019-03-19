import requests,json,jsonpath
base_url='https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=filter_type%3Drealtimehot%26mi_cid%3D100103%26pos%3D0_0%26c_type%3D30%26display_time%3D1550799509&luicode=10000011&lfid=231583 HTTP/1.1'

headers={
    'Host':'m.weibo.cn',
    'Connection':'keep-alive',
    'Accept':'application/json, text/plain, */*',
    'MWeibo-Pwa':'1',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':'https://m.weibo.cn/p/index?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=filter_type%3Drealtimehot%26mi_cid%3D100103%26pos%3D0_0%26c_type%3D30%26display_time%3D1550799509&luicode=10000011&lfid=231583',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'MLOGIN=0; _T_WM=69999be95d5b942170d8db423eddba6a; WEIBOCN_FROM=1110003030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231583%26fid%3D106003type%253D25%2526t%253D3%2526disable_hot%253D1%2526filter_type%253Drealtimehot%26uicode%3D10000011',
}
response = requests.get(base_url,headers=headers)
res = response.text
dic = json.loads(res)
print(dic)
# hot = dic['data']['cards'][0]['card_group']
# for i in hot:
#     print(i['desc'])
jpath = jsonpath.jsonpath(dic,'$..desc')
jurl = jsonpath.jsonpath(dic,'$..cards..scheme')
print(jpath)
print(jurl)