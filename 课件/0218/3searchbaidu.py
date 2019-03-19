from urllib import request,parse

base_url =  'http://www.baidu.com/s?'
wd = input('请输入搜索内容：')
data = {
    'wd':wd
}
# 对url参数进行转码
msg = parse.urlencode(data)
newurl = base_url +msg

# 发送请求
html = request.urlopen(newurl)

print(html.read().decode('utf-8'))
