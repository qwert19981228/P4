from urllib import request
import json
base_url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

# 发送请求
response = request.urlopen(base_url)

jsonstr = response.read().decode('utf-8')
newjson = json.loads(jsonstr)

with open('./douban.json','a+',encoding='utf-8') as f:
    for item in newjson:
        f.write(json.dumps(item,ensure_ascii=False)+'\n')
