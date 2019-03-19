import requests

base_url = 'http://www.renren.com/PLogin.do'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
}
data = {
    'email':'17731893183',
    'password':'qq6218346'
}

response = requests.post(base_url,data,headers=headers)

print(response.text)