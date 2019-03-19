from lxml import etree
from time import sleep
import requests
import pymysql
import datetime
import re,random
import ssl
import urllib3
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Accept-Language':'zh-CN,zh;q=0.9'
           }

proxy = {
'http':'http://49.51.70.42:1080',
}

try:
    # 连接数据库
    db = pymysql.connect(host="127.0.0.1", user="root", database='p4', password="123456", port=3306, charset="utf8",cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = db.cursor()
except:
    print('连接失败')
while True:
    try:
        base_url = 'https://job.dajie.com/qz1-p%d/'
        for i in range(1,15491):
            print(i)
            new_url = base_url % i
            response = requests.get(new_url,headers=headers,verify=False)
            text = response.content.decode('utf-8')
            html = etree.HTML(text)
            url = html.xpath('//*[@id="content"]/div[1]/div[2]/div[3]/ul/li/@data-url')
            sleep(2)
            for i in url:

                sleep(2)
                response = requests.get(i,headers=headers,verify=False)

                text = response.content.decode('utf-8')
                html = etree.HTML(text)
                pat = re.compile(r'https://job.dajie.com/(.*?).html')
                code = pat.findall(i)[0]
                print(i)
                # 工作名
                jobname = html.xpath('//*[@id="jp-app-wrap"]/div[2]/div[2]/div[1]/div[1]/div/span[1]/text()')[0]
                # 待遇
                salary = html.xpath('//*[@id="jp-app-wrap"]/div[2]/div[2]/div[1]/div[1]/span[1]/text()')[0]
                # 经验
                experience = html.xpath('//*[@id="jp-app-wrap"]/div[2]/div[2]/div[1]/div[2]/ul/li[3]/span/text()')[0]
                # 学历
                degree = ''.join(html.xpath('//*[@id="jp-app-wrap"]/div[2]/div[2]/div[1]/div[2]/ul/li[4]/span/text()'))
                # 工作内容
                jobdesc = html.xpath('//*[@id="jp_maskit"]/pre[2]/text()')[0].replace('\'', '').replace('"', '').replace('\n','')
                # 工作地点
                jobposition = html.xpath('//*[@id="jp-app-wrap"]/div[2]/div[2]/div[6]/span/text()')[0]
                # 工作诱惑
                jobboon = html.xpath('//*[@id="jp-app-wrap"]/div[2]/div[2]/div[1]/div[3]//li/text()')[0]
                # 公司
                company = html.xpath('//*[@id="jp-app-wrap"]/div[2]/div[3]/div[1]/p/a[1]/text()')[0]
                # 发布时间
                time = datetime.datetime.now().strftime('%Y-%m-%d')
                data = {
                    'jobname': jobname,
                    'salary': salary,
                    'experience': experience,
                    'degree': degree,
                    'jobdesc': str(jobdesc),
                    'jobposition': jobposition,
                    'jobboon': jobboon,
                    'company': company,
                    'time': time,
                    'code': code,
                }
                field = ''
                values = ''
                for k, v in data.items():
                    field += '`%s`,' % k
                    values += '\'%s\',' % v
                print(data)

                field = field.strip(',')
                values = values.strip(',')

                sql = '''INSERT ignore INTO `dajie` (%s) VALUES (%s)''' % (field, values)
                db.ping(reconnect=True)
                cursor.execute(sql)
                db.commit()
                db.close()
    except:
        pass
    continue
    







































#
# # 请求地址
# # 请求地址
# browser.get('https://shanghai.anjuke.com/sale/p')
# # browser.find_element_by_class_name('houseListTitle')
# # url = browser.find_element_by_xpath('//li[@class="list-item"]//div[@class="house-details"]//a/@href')
# # browser.find_element_by_xpath('//ul/li[@class="houseInfo-detail-item"]/text()')
#
#
#

