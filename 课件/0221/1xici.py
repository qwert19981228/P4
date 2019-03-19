from urllib import request
import re,json
base_url = 'https://www.xicidaili.com/nt/2'

# 代理信息
proxy = {
    'http':'http://alice:123456@120.78.166.84:6666',
    'https': 'https://alice:123456@120.78.166.84:6666',
}
# 构建请求方法
proxies = request.ProxyHandler(proxy)
opener = request.build_opener(proxies)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}

# 构建请求头
req = request.Request(url=base_url,headers=headers)

# 发送请求
response = opener.open(req)

html = response.read().decode('utf-8')

# 制定规则 匹配tr
tr_pat = re.compile(r'<tr.*?>.*?</tr>',re.S)

# 检索
tr_list = tr_pat.findall(html)
# 便利拿到的tr
res = []
for item in tr_list[1:]:
    newdic = {}
    # 制定匹配td的规则
    td_pat = re.compile(r'<td.*?>(.*?)</td>',re.S)
    # td内的信息
    td_list = td_pat.findall(item)
    newdic['ip']=td_list[1]
    newdic['port']=td_list[2]
    newdic['httptype']=td_list[5]

    # 进行筛选速度
    speed_pat = re.compile(r'title="(.*?)"')
    speed_obj = speed_pat.search(td_list[6])
    print(td_list)
    print(speed_obj)
    # 判断匹配结果不为空
    if speed_obj:
        second = speed_obj.group(1)
        if float(second[:-1])>1:
            continue

    #时间筛选 如果不带天就跳出
    if '天' in td_list[8]:
        # 判断存活时间 如果小于3天也跳出
        if int(td_list[8][:-1]) < 3:
            continue
        else:
            newdic['day'] = td_list[8]
    else:
        continue
    # 将字典插入到res
    res.append(newdic)

# 存到本地
with open('./diaoli.json','w',encoding='utf-8') as f:
    f.write(json.dumps(res,indent=4,ensure_ascii=False))


# 将速度大于1秒的排除  活跃天数小于一天的也排除
