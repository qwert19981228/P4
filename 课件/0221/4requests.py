import requests

base_url='https://www.xicidaili.com/'
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}
proxy={
    'http':'http://alice:123456@120.78.166.84:6666',
    'https':'https://alice:123456@120.78.166.84:6666'
}
response = requests.get(base_url,proxies=proxy,headers=headers)
print(response.headers)
print(response.text)