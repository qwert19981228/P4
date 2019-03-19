from urllib import request,parse
import time,random,hashlib

msg = input('请输入要翻译的内容：')

base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

# "" + (new Date).getTime() + parseInt(10 * Math.random(), 10)
salt = ''+str(int(time.time()*1000)) + str(random.randint(0,9))
#  sign: n.md5("fanyideskweb" + fnayi + i + "p09@Bn{h02_BIEe]$P^nG")
def getMD5(new_temp):
    m = hashlib.md5()
    m.update(new_temp.encode('utf-8'))
    # 获取sign
    sign = m.hexdigest()
    return sign



data = {
    "i": msg,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    # "salt": "15506426842784",
    "salt":salt,
    "sign": getMD5("fanyideskweb"+msg+salt+"p09@Bn{h02_BIEe]$P^nG"),
    # "sign":"741366b0bfa79375ea3645bd80a41cb9",
    "ts":'1550642684278',
    # "ts": str(int(time.time()*1000)),
    "bv": "c2a59c50299d41ed6f790ebc60178237",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false",
}
data = parse.urlencode(data)
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": len(data),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": '_ga=GA1.2.350948535.1548817319; OUTFOX_SEARCH_USER_ID_NCOO=1810007035.5914545; OUTFOX_SEARCH_USER_ID="-1874561565@10.168.11.11"; JSESSIONID=aaa3ZVEBag7Qv_2DrGjKw; ___rl__test__cookies=1550642684276',
    # "Cookie": "_ga=GA1.2.350948535.1548817319; OUTFOX_SEARCH_USER_ID_NCOO=1810007035.5914545; OUTFOX_SEARCH_USER_ID='-1874561565@10.168.11.11'; JSESSIONID=aaaPJYGJ-mJs0exFj3iKw; ___rl__test__cookies=1550632061157",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

req = request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=headers)

# 发送请求
response = request.urlopen(req)

print(response.read().decode('utf-8'))