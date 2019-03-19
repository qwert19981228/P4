from urllib import request
import re
base_url="https://tieba.baidu.com/p/4423804144"

# 发送请求
response = request.urlopen(base_url)

# 返回的数据
html = response.read().decode('utf-8')

with open('./meimei.html','w',encoding='utf-8') as f:
    f.write(html)

# 定义规则
pat = re.compile(r'<img class="BDE_Image" src="(.*?)".*?>')
res = pat.findall(html)

# 下载图片
for item in res:
    fname = item.split('/')[-1]

    request.urlretrieve(item,fname)