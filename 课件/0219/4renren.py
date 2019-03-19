# cookie: 在浏览器中存储的信息 以 key=value
# session（会话）: 将数据存在服务无端  key=valye
#     当创建了一个session 会生成一个sessionid
#     将sessionid存入到本地浏览器当中的cookie
#     下次访问时就可以通过 提交的cookie 中的sessionid判断是否已经登录

# 编号     信息              干了什么事情
#  1        name age sex      。。。。。

from urllib import request

base_url = 'http://www.renren.com/969685801'

# 构建请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "Cookie": "anonymid=jsa34cxx9y0ncb; depovince=BJ; _r01_=1; JSESSIONID=abc74FWLs4Kgc-tNcydKw; ick_login=82b9055c-419a-48e5-9dd6-a2d44353faf5; jebecookies=1335a48c-719f-4c8a-ba75-1d60fda39235|||||; _de=F8ACC661CB0C81B0D50364A326E8DA93; p=b044a4463e7cb9e3d0bde7d898c8d5d61; first_login_flag=1; ln_uact=17611593298; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=f532568044c88ac4df35fb2f70bbf1c01; societyguester=f532568044c88ac4df35fb2f70bbf1c01; id=969685801; xnsid=fc8dd1af; ver=7.0; loginfrom=null; jebe_key=534eb42f-e54e-4243-80a3-f50614126293%7Cd9baafb2d9acfdd31adc4a02a63486c3%7C1550541015122%7C1%7C1550541016124; wp_fold=0"
}

# 发送请求
req = request.Request(url=base_url,headers=headers)
response = request.urlopen(req)
html = response.read().decode('utf-8')
print(html)