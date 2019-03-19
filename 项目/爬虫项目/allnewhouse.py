import requests
from lxml import etree
import pymysql,re
from time import sleep
import random

while True:
    try:
        # 连接数据库
        db = pymysql.connect(host="127.0.0.1", user="root", database='p4', password="123456", port=3306, charset="utf8",cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        cursor = db.cursor()
    except:
        print('连接失败')
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    # proxy = [
    #     {
    #         'http':'http://212.101.74.73:443',
    #      # 'https':'http://212.101.74.73:443',
    #      },
    #     {
    #         'http':'http://91.249.169.134:3128',
    #     # 'https':'http://91.249.169.134:3128',
    #     },
    #     {
    #         'http':'http://218.28.96.196:8060',
    #         # 'https':'http://218.28.96.196:8060'
    # },
    # ]
    # 'http':'http://183.82.32.153:56144',
    # 'http':'http://1.20.101.150:41904',
    # 'http':'http://223.19.141.26:8197',
    # 'http':'http://93.33.234.116:56793',
    # 'http':'http://36.67.226.17:37860',
    # 'http':'http://110.232.74.13:54306',
    # 'http':'http://36.89.211.146:40438',
    # 'http':'http://213.6.67.86:32586',
    # 'http':'http://82.207.43.131:47704',
    # 'http':'http://178.214.74.215:44445',
    # 'http':'http://5.40.175.182:8082',

    base_url = 'https://%s.fang.anjuke.com/loupan/all/'

    url_list = ['bj','tj','lf','sh','sjz','ty','bt','wf','yt','dl','heb','shen','cc','ks','hz','su','nj','wx','nb','hf','jn','qd','nt','yz','cz','tz','sz','gz','fs','sy','hui','fz','xm','dg','zh','zs','jm','nn','nc','hai','cd','cq','wh','zz','xa','cs','km','gy','ly','wlmq','lz','xc','yi']
    sleep(2)
    for i in url_list:
        url = base_url % i
        for i in range(1,29):
            newurl = url+'p%s/' % i
            print(newurl)
            response = requests.get(newurl,headers=headers)#,proxies=random.choice(proxy)
            text = response.content.decode('utf-8')
            html = etree.HTML(text)
            res = html.xpath('//div[@class="infos"]/a[@class="lp-name"]/@href')
            sleep(2)
            for i in res:
                response = requests.get(i,headers=headers)#,proxies=random.choice(proxy)
                text = response.content.decode('utf-8')
                html = etree.HTML(text)
                res = html.xpath('//div[@class="basic-details"]')
                reg = re.compile(r'https://.*.fang.anjuke.com/loupan/(.*?).html')
                code = reg.findall(i)[0]
                sleep(2)
                for j in res:
                    # 标题
                    title = ''.join(j.xpath('.//div[@class="basic-info"]/h1/text()')).replace('\t', '').replace('\n', '').replace(' ', '')
                    # 别名
                    name = ''.join(j.xpath('.//div[@class="basic-info"]/p/text()')).replace('\t', '').replace('\n', '').replace(' ', '').replace('别名：','')
                    # 标签
                    tags = ''.join(j.xpath('.//div[@class="tags"]/a/text()')).replace('\t', '').replace('\n', '').replace(' ', '').replace('\r','')
                    # 价格
                    price = ''.join(j.xpath('.//dl//dd[@class="price"]/p//text()')).replace('\t', '').replace('\n', '').replace(' ', '').replace('\r','').replace('\uebf4变价通知我','')
                    # 开盘
                    open = ''.join(j.xpath('.//dl/dd[2]/span/text()')).replace('\t', '').replace('\n', '').replace(' ', '').replace('\r','')
                    # 交房
                    close = ''.join(j.xpath('.//dl/dd[3]/span/text()')).replace('\t', '').replace('\n', '').replace(' ', '').replace('\r','')
                    # 户型
                    type = ''.join(j.xpath('.//dl/dd[4]//div[@class="house-item g-overflow"]//a/text()')).replace('\t', '').replace('\n', '').replace(' ', '').replace('\r','')
                    # 地址
                    place = ''.join(j.xpath('.//dl/dd[5]/a[1]/text()')).replace('\t', '').replace('\n', '').replace(' ', '').replace('\r','')

                    datahouse = {
                        'title':title,
                        'name':name,
                        'tags':tags,
                        'price':price,
                        'open':open,
                        'close':close,
                        'type':type,
                        'place':place,
                        'code':code
                    }
                    field = ''
                    values = ''
                    for k,v in datahouse.items():
                        field += '`%s`,' % k
                        values += '"%s",' % v
                    print(datahouse)

                    field = field.strip(',')
                    values = values.strip(',')
                    sql = 'INSERT ignore INTO `test4` (%s) VALUES (%s)' % (field,values)
                    db.ping(reconnect=True)
                    cursor.execute(sql)
                    db.commit()
                    db.close()