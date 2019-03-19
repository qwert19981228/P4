from urllib import request
import json,random
# 获取到代理
def getProxy(proxyfile):
    # 读取文件
    with open(proxyfile,'r',encoding='utf-8') as f:
        proxy_str=f.read()
    data = json.loads(proxy_str)
    proxies = []
    for item in data:
        proxy = {}
        # 'http':'http://ip:port'
        proxy['http'] = 'http://'+ item['ip']+':'+item['port']
        proxy['https'] = 'https://'+ item['ip']+':'+item['port']
        proxies.append(proxy)

    return proxies

# 构建opener
def getOpener(proxy):
    proxies=random.choice(proxy)
    pro_obj = request.ProxyHandler(proxies)
    opener = request.build_opener(pro_obj)

    return opener

# 发送请求 如果请求失败重新获取代理在次发送请求
def getdata(base_url,opener,proxs,num=3):
    try:
        response = opener.open(base_url,timeout=3)
        data = response.read()
        return data
    except Exception as e:
        print(e)
        # 如果失败 再次调用发送请求
        if num > 1:
            data = getdata(base_url,getOpener(proxs),proxs,num = num-1)
            return data
        return None



if __name__ == '__main__':
    proxies = getProxy('diaoli.json')
    base_url = 'http://www.baidu.com/s?wd=ip'
    opener= getOpener(proxies)
    html = getdata(base_url,opener,proxies)
    if html:
        print(html.decode('utf-8'))
    else:
        print(html)