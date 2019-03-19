from urllib import request
import re,json
base_url = 'https://www.xicidaili.com/nn/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}

# 构建请求头
req = request.Request(url=base_url,headers=headers)

response = request.urlopen(req)

html = response.read().decode('utf-8')

# 制定规则
tr_pat = re.compile(r'<tr.*?>.*?</tr>',re.S)

# 检索
tr_list = tr_pat.findall(html)
# 便利拿到的tr
res = []
for item in tr_list[1:]:
    newdic = {}
    td_pat = re.compile(r'<td>(.*?)</td>',re.S)
    td_list = td_pat.findall(item)
    newdic['ip']=td_list[0]
    newdic['port']=td_list[1]
    newdic['httptype']=td_list[3]

    # 将字典插入到res
    res.append(newdic)

# 存到本地
with open('./diaoli.json','w',encoding='utf-8') as f:
    f.write(json.dumps(res,indent=4))


# 将速度大于1秒的排除  活跃天数小于一天的也排除
