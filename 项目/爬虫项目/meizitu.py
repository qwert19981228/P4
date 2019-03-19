import requests
from lxml import etree
import time,ssl,os
from urllib import request
import random
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Referer': 'https://www.mzitu.com/'
}
while True:

    try:
        base_url = 'https://www.mzitu.com/%s/'
        url_list = ['xinggan','japan','taiwan','mm']
        for i in url_list:
            url = base_url % i
            for i in range(1,141):
                newurl = url+'page/%s/' % i
                print(newurl)
                response = requests.get(newurl,headers=headers)
                # time.sleep(1)
                text = response.content.decode('utf-8')
                html = etree.HTML(text)
                res = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
                for i in res :
                    # time.sleep(1)
                    for j in range(1,66):
                        imgurl = i + '/%s' % j
                        print(imgurl)
                        # time.sleep(1)
                        response = requests.get(imgurl,headers=headers)
                        text = response.content.decode('utf-8')
                        html = etree.HTML(text)
                        res = html.xpath('//div[@class="main-image"]/p/a/img/@src')
                        res = ''.join(res)
                        targetPath = os.getcwd() + os.path.sep + 'mzitu' + os.path.sep
                        # 判断路径存不存在
                        if not os.path.exists(targetPath):
                            # 创建文件夹
                            os.makedirs(targetPath)
                        fname = res.split('/')[-1]
                        # request.urlretrieve(res,fname)
                        req = requests.get(res,headers=headers)
                        print(req.status_code)
                        img = req.content
                        with open('%s/%s' % (targetPath, fname), 'wb') as f:
                            f.write(img)
    except:
        pass
    continue