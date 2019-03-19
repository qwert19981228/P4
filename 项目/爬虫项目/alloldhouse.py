import requests
from lxml import etree
import pymysql
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
    headers = [
        {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    ]
    # proxy = {
    #     'http': 'http://212.205.149.211:33355',
    #     'https': 'https://212.205.149.211:33355',
    # }

    base_url = 'https://%s.anjuke.com/sale/'
    #
    url_list = ['beijing','tianjin','dalian','sjz','heb','sy','ty','cc','weihai','weifang','huhehaote','baotou','qinhuangdao','yt','baoding','shanghai','hangzhou','suzhou','nanjing','wuxi','jinan','qd','ks','nb','nc','fz','hf','xuzhou','zibo','nantong','cz','huzhou','shenzheng','guangzhou','foshan','cs','sanya','huizhou','dg','haikou','zh','zs','xm','nanning','quanzhou','liuzhou','chengdu','chongqing','wuhan','zhengzhou','xa','km','gy','lanzhou','luoyang']
    for i in url_list:
        url = base_url % i
        print(url)

        for i in range(1,51):
            newurl = url+'p%s' % i
            print(newurl)
            response = requests.get(newurl,headers=random.choice(headers))#,proxies=proxy
            sleep(1)
            text = response.content.decode('utf-8')
            html = etree.HTML(text)

            res = html.xpath('//li[@class="list-item"]//div[@class="house-details"]//a/@href')
            sleep(1)
            for i in res:
                sleep(random.randint(0, 5))
                response = requests.get(i,headers=random.choice(headers))#,proxies=proxy
                text = response.content.decode('utf-8')
                html = etree.HTML(text)
                res = html.xpath('//div[@class="houseInfo-wrap"]/ul')
                sleep(2)
                for j in res:
                    datahouse = {}
                    # 标题
                    title = ''.join(j.xpath('//h3[@class="long-title"]/text()')[0]).replace('\t', '').replace('\n', '').replace(' ', '')
                    # 所属小区
                    village = ''.join(j.xpath('./li[1]//text()')[4]).replace('\t','').replace('\n','').replace(' ','')
                    # 房屋户型
                    housetype = ''.join(j.xpath('./li[2]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 房屋单价
                    houseprice = ''.join(j.xpath('./li[3]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 所在位置
                    position = ''.join(j.xpath('./li[4]//text()')[2:8]).replace('\t','').replace('\n','').replace(' ','')
                    # 建筑面积
                    housearea = ''.join(j.xpath('./li[5]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 参考首付
                    first_pay = ''.join(j.xpath('./li[6]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 建造年代
                    build_year = ''.join(j.xpath('./li[7]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 房屋朝向
                    house_direct = ''.join(j.xpath('./li[8]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 房屋类型
                    type = ''.join(j.xpath('./li[10]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 所在楼层
                    floor = ''.join(j.xpath('./li[11]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 装修程度
                    house_decorate = ''.join(j.xpath('./li[12]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 产权年限
                    property_right = ''.join(j.xpath('./li[13]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 配套电梯
                    elevator = ''.join(j.xpath('./li[14]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 房本年限
                    premises_permit = ''.join(j.xpath('./li[15]//text()')[3]).replace('\t','').replace('\n','').replace(' ','')
                    # 产权性质
                    nature = ''.join(j.xpath('./li[16]//text()')[2:6]).replace('\t','').replace('\n','').replace(' ','')
                    # 唯一住房
                    unique_housing = ''.join(j.xpath('./li[17]//text()')[2:6]).replace('\t','').replace('\n','').replace(' ','')
                    # 一手房源
                    first_housing = ''.join(j.xpath('./li[18]//text()')[2:6]).replace('\t','').replace('\n','').replace(' ','')
                    # 编码
                    code = ''.join(j.xpath('//*[@id="houseCode"]//text()')[0]).replace('\t','').replace('\n','').replace(' ','').replace('，','').replace('房屋编码：','')
                    # 发布时间
                    time = ''.join(j.xpath('//span[@class="house-encode"]/text()')).replace('\t','').replace('\n','').replace(' ','').replace('，','').replace('发布时间：','')



                    datahouse = {
                        'title':title,
                        'village':village,
                        'housetype':housetype,
                        'houseprice':houseprice,
                        'position':position,
                        'housearea':housearea,
                        'first_pay':first_pay,
                        'build_year':build_year,
                        'house_direct':house_direct,
                        'type':type,
                        'floor':floor,
                        'house_decorate':house_decorate,
                        'property_right':property_right,
                        'elevator':elevator,
                        'premises_permit':premises_permit,
                        'nature':nature,
                        'unique_housing':unique_housing,
                        'first_housing':first_housing,
                        'code':code,
                        'time':time,
                    }
                    field = ''
                    values = ''
                    for k,v in datahouse.items():
                        field += '`%s`,' % k
                        values += '"%s",' % v
                    print(datahouse)

                    field = field.strip(',')
                    values = values.strip(',')
                    sql = 'INSERT ignore INTO `oldhouse` (%s) VALUES (%s)' % (field,values)
                    db.ping(reconnect=True)
                    cursor.execute(sql)
                    db.commit()
                    db.close()