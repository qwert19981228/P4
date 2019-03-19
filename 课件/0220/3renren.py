from urllib import request,parse
from http import cookiejar

# 实例化cookie 管理器
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
# http_handler = request.HTTPHandler()
# https_handler = request.HTTPSHandler()
# request.urlopen()
# 创建自定义的请求方法
opener = request.build_opener(cookie_handler)
# 登录post提交 获取cookie
base_url = 'http://www.renren.com/PLogin.do'

data = {
    'email':'17731893183',
    'password':'qq6218346'
}
newdata = parse.urlencode(data)

req = request.Request(url=base_url,data=bytes(newdata,encoding='utf-8'))

# 发送请求 提交账号密码
response = opener.open(req)


# 向首页发送请求 （重定向）
home_index = 'http://www.renren.com/963734292'

home_response = opener.open(home_index)

print(home_response.read().decode('utf-8'))

