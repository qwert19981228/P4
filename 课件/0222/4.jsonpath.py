import requests,jsonpath,json

base_url="https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547433909; _ga=GA1.2.1714103551.1547433909; user_trace_token=20190114104509-681bea39-17a6-11e9-adcf-525400f775ce; LGUID=20190114104509-681bef9a-17a6-11e9-adcf-525400f775ce; JSESSIONID=ABAAABAAADEAAFIC4EDBC42FE7414CEA9504BBAACDDBC84",
    "Host": "www.lagou.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
}
response = requests.get(base_url,headers=headers)
response.encoding='utf-8'
str = response.text
# 所有城市的名字
# res = jsonpath.jsonpath(json.loads(str),'$..name')
# 获取data
# res = jsonpath.jsonpath(json.loads(str),'$..allCitySearchLabels')
#  获取包头的信息
# res = jsonpath.jsonpath(json.loads(str),'$..allCitySearchLabels.B[?(@.name=="包头")]')
# 获取isSelected为true
res = jsonpath.jsonpath(json.loads(str),'$..allCitySearchLabels..[?(@.isSelected==False)]')

print(res)
print(json.loads(str))