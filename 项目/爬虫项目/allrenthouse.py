import requests
from lxml import etree
import pymysql
import time
import random
from time import sleep
while True:
    try:
        # 连接数据库
        db = pymysql.connect(host="127.0.0.1", user="root", database='p4', password="123456", port=3306, charset="utf8",cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        cursor = db.cursor()
    except:
        print('连接失败')
    headers = [
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','cookie': 'aQQ_ajkguid=72AA2E39-D673-A99E-93D2-5FD9ABFCB8DC; _ga=GA1.2.1852825511.1551876704; 58tj_uuid=b50e4a9c-cdf2-4899-a302-75d8ca523dbc; wmda_uuid=f8bb4190ae5e83250adc9e8fdab902c6; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; als=0; search_words=%E9%87%91%E5%B1%B1%E4%B8%96%E7%BA%AA%E5%9F%8E; __xsptplus8=8.4.1551880689.1551880706.4%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23jqNVDkGObuOHMO1VLPD3dgtwDQVbGjt3%23; _gid=GA1.2.1114021403.1552350780; isp=true; browse_comm_ids=569172%7C877110%7C6405%7C6402%7C569173; propertys=lao67s-poa9up_; lp_lt_ut=440e93ff85095c5d2895ceaf12a8ffbc; aQQ_brokerguid=8D118BD8-6748-B6B1-1A81-1C505A93FB3D; ajk_member_id=155324276; ajk_member_name=U15524843398337; ajk_member_key=e32e1a60d964ca73c3eb7f383058d8e5; ajk_member_time=1584020280; aQQ_ajkauthinfos=1LX5XGFWZU1ZArFVnzld%2FS36ZJdKAJFSuTiyx6xNpMNudwxOsodcTQgotZZkU%2FjPlO%2FAD9eeo633HD8PbH38AUovx1o; lui=155324276%3A1; sessid=4E127D1E-06D7-692D-5D25-846D07E03480; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%26ck%3D1954.2.71.150.186.466.366.128%26shh%3Dwww.baidu.com%26sht%3D99249017_hao_pg%26wd%3D%26eqid%3De3095cbe0001b528000000035c89ba9d; twe=2; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%2526ck%253D1954.2.71.150.186.466.366.128%2526shh%253Dwww.baidu.com%2526sht%253D99249017_hao_pg%2526wd%253D%2526eqid%253De3095cbe0001b528000000035c89ba9d; new_uv=17; ctid=11; new_session=0; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1552476326,1552484406,1552522099,1552530085; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1552530085; wmda_session_id_6289197098934=1552531677416-0e21d10b-6652-26a9; _gat=1'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
         'Cookie': 'aQQ_ajkguid=72AA2E39-D673-A99E-93D2-5FD9ABFCB8DC; _ga=GA1.2.1852825511.1551876704; 58tj_uuid=b50e4a9c-cdf2-4899-a302-75d8ca523dbc; wmda_uuid=f8bb4190ae5e83250adc9e8fdab902c6; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; als=0; search_words=%E9%87%91%E5%B1%B1%E4%B8%96%E7%BA%AA%E5%9F%8E; __xsptplus8=8.4.1551880689.1551880706.4%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23jqNVDkGObuOHMO1VLPD3dgtwDQVbGjt3%23; _gid=GA1.2.1114021403.1552350780; isp=true; browse_comm_ids=569172%7C877110%7C6405%7C6402%7C569173; propertys=lao67s-poa9up_; lp_lt_ut=440e93ff85095c5d2895ceaf12a8ffbc; aQQ_brokerguid=8D118BD8-6748-B6B1-1A81-1C505A93FB3D; ajk_member_id=155324276; ajk_member_name=U15524843398337; ajk_member_key=e32e1a60d964ca73c3eb7f383058d8e5; ajk_member_time=1584020280; aQQ_ajkauthinfos=1LX5XGFWZU1ZArFVnzld%2FS36ZJdKAJFSuTiyx6xNpMNudwxOsodcTQgotZZkU%2FjPlO%2FAD9eeo633HD8PbH38AUovx1o; lui=155324276%3A1; sessid=4E127D1E-06D7-692D-5D25-846D07E03480; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%26ck%3D1954.2.71.150.186.466.366.128%26shh%3Dwww.baidu.com%26sht%3D99249017_hao_pg%26wd%3D%26eqid%3De3095cbe0001b528000000035c89ba9d; twe=2; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%2526ck%253D1954.2.71.150.186.466.366.128%2526shh%253Dwww.baidu.com%2526sht%253D99249017_hao_pg%2526wd%253D%2526eqid%253De3095cbe0001b528000000035c89ba9d; new_uv=17; ctid=11; new_session=0; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1552476326,1552484406,1552522099,1552530085; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1552530085; wmda_session_id_6289197098934=1552531677416-0e21d10b-6652-26a9; _gat=1'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','cookie': 'aQQ_ajkguid=72AA2E39-D673-A99E-93D2-5FD9ABFCB8DC; _ga=GA1.2.1852825511.1551876704; 58tj_uuid=b50e4a9c-cdf2-4899-a302-75d8ca523dbc; wmda_uuid=f8bb4190ae5e83250adc9e8fdab902c6; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; als=0; search_words=%E9%87%91%E5%B1%B1%E4%B8%96%E7%BA%AA%E5%9F%8E; __xsptplus8=8.4.1551880689.1551880706.4%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23jqNVDkGObuOHMO1VLPD3dgtwDQVbGjt3%23; _gid=GA1.2.1114021403.1552350780; isp=true; browse_comm_ids=569172%7C877110%7C6405%7C6402%7C569173; propertys=lao67s-poa9up_; lp_lt_ut=440e93ff85095c5d2895ceaf12a8ffbc; aQQ_brokerguid=8D118BD8-6748-B6B1-1A81-1C505A93FB3D; ajk_member_id=155324276; ajk_member_name=U15524843398337; ajk_member_key=e32e1a60d964ca73c3eb7f383058d8e5; ajk_member_time=1584020280; aQQ_ajkauthinfos=1LX5XGFWZU1ZArFVnzld%2FS36ZJdKAJFSuTiyx6xNpMNudwxOsodcTQgotZZkU%2FjPlO%2FAD9eeo633HD8PbH38AUovx1o; lui=155324276%3A1; sessid=4E127D1E-06D7-692D-5D25-846D07E03480; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%26ck%3D1954.2.71.150.186.466.366.128%26shh%3Dwww.baidu.com%26sht%3D99249017_hao_pg%26wd%3D%26eqid%3De3095cbe0001b528000000035c89ba9d; twe=2; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%2526ck%253D1954.2.71.150.186.466.366.128%2526shh%253Dwww.baidu.com%2526sht%253D99249017_hao_pg%2526wd%253D%2526eqid%253De3095cbe0001b528000000035c89ba9d; new_uv=17; ctid=11; new_session=0; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1552476326,1552484406,1552522099,1552530085; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1552530085; wmda_session_id_6289197098934=1552531677416-0e21d10b-6652-26a9; _gat=1'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0','cookie': 'aQQ_ajkguid=72AA2E39-D673-A99E-93D2-5FD9ABFCB8DC; _ga=GA1.2.1852825511.1551876704; 58tj_uuid=b50e4a9c-cdf2-4899-a302-75d8ca523dbc; wmda_uuid=f8bb4190ae5e83250adc9e8fdab902c6; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; als=0; search_words=%E9%87%91%E5%B1%B1%E4%B8%96%E7%BA%AA%E5%9F%8E; __xsptplus8=8.4.1551880689.1551880706.4%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23jqNVDkGObuOHMO1VLPD3dgtwDQVbGjt3%23; _gid=GA1.2.1114021403.1552350780; isp=true; browse_comm_ids=569172%7C877110%7C6405%7C6402%7C569173; propertys=lao67s-poa9up_; lp_lt_ut=440e93ff85095c5d2895ceaf12a8ffbc; aQQ_brokerguid=8D118BD8-6748-B6B1-1A81-1C505A93FB3D; ajk_member_id=155324276; ajk_member_name=U15524843398337; ajk_member_key=e32e1a60d964ca73c3eb7f383058d8e5; ajk_member_time=1584020280; aQQ_ajkauthinfos=1LX5XGFWZU1ZArFVnzld%2FS36ZJdKAJFSuTiyx6xNpMNudwxOsodcTQgotZZkU%2FjPlO%2FAD9eeo633HD8PbH38AUovx1o; lui=155324276%3A1; sessid=4E127D1E-06D7-692D-5D25-846D07E03480; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%26ck%3D1954.2.71.150.186.466.366.128%26shh%3Dwww.baidu.com%26sht%3D99249017_hao_pg%26wd%3D%26eqid%3De3095cbe0001b528000000035c89ba9d; twe=2; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%2526ck%253D1954.2.71.150.186.466.366.128%2526shh%253Dwww.baidu.com%2526sht%253D99249017_hao_pg%2526wd%253D%2526eqid%253De3095cbe0001b528000000035c89ba9d; new_uv=17; ctid=11; new_session=0; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1552476326,1552484406,1552522099,1552530085; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1552530085; wmda_session_id_6289197098934=1552531677416-0e21d10b-6652-26a9; _gat=1'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','cookie': 'aQQ_ajkguid=72AA2E39-D673-A99E-93D2-5FD9ABFCB8DC; _ga=GA1.2.1852825511.1551876704; 58tj_uuid=b50e4a9c-cdf2-4899-a302-75d8ca523dbc; wmda_uuid=f8bb4190ae5e83250adc9e8fdab902c6; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; als=0; search_words=%E9%87%91%E5%B1%B1%E4%B8%96%E7%BA%AA%E5%9F%8E; __xsptplus8=8.4.1551880689.1551880706.4%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23jqNVDkGObuOHMO1VLPD3dgtwDQVbGjt3%23; _gid=GA1.2.1114021403.1552350780; isp=true; browse_comm_ids=569172%7C877110%7C6405%7C6402%7C569173; propertys=lao67s-poa9up_; lp_lt_ut=440e93ff85095c5d2895ceaf12a8ffbc; aQQ_brokerguid=8D118BD8-6748-B6B1-1A81-1C505A93FB3D; ajk_member_id=155324276; ajk_member_name=U15524843398337; ajk_member_key=e32e1a60d964ca73c3eb7f383058d8e5; ajk_member_time=1584020280; aQQ_ajkauthinfos=1LX5XGFWZU1ZArFVnzld%2FS36ZJdKAJFSuTiyx6xNpMNudwxOsodcTQgotZZkU%2FjPlO%2FAD9eeo633HD8PbH38AUovx1o; lui=155324276%3A1; sessid=4E127D1E-06D7-692D-5D25-846D07E03480; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%26ck%3D1954.2.71.150.186.466.366.128%26shh%3Dwww.baidu.com%26sht%3D99249017_hao_pg%26wd%3D%26eqid%3De3095cbe0001b528000000035c89ba9d; twe=2; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%2526ck%253D1954.2.71.150.186.466.366.128%2526shh%253Dwww.baidu.com%2526sht%253D99249017_hao_pg%2526wd%253D%2526eqid%253De3095cbe0001b528000000035c89ba9d; new_uv=17; ctid=11; new_session=0; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1552476326,1552484406,1552522099,1552530085; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1552530085; wmda_session_id_6289197098934=1552531677416-0e21d10b-6652-26a9; _gat=1'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','cookie': 'aQQ_ajkguid=72AA2E39-D673-A99E-93D2-5FD9ABFCB8DC; _ga=GA1.2.1852825511.1551876704; 58tj_uuid=b50e4a9c-cdf2-4899-a302-75d8ca523dbc; wmda_uuid=f8bb4190ae5e83250adc9e8fdab902c6; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; als=0; search_words=%E9%87%91%E5%B1%B1%E4%B8%96%E7%BA%AA%E5%9F%8E; __xsptplus8=8.4.1551880689.1551880706.4%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23jqNVDkGObuOHMO1VLPD3dgtwDQVbGjt3%23; _gid=GA1.2.1114021403.1552350780; isp=true; browse_comm_ids=569172%7C877110%7C6405%7C6402%7C569173; propertys=lao67s-poa9up_; lp_lt_ut=440e93ff85095c5d2895ceaf12a8ffbc; aQQ_brokerguid=8D118BD8-6748-B6B1-1A81-1C505A93FB3D; ajk_member_id=155324276; ajk_member_name=U15524843398337; ajk_member_key=e32e1a60d964ca73c3eb7f383058d8e5; ajk_member_time=1584020280; aQQ_ajkauthinfos=1LX5XGFWZU1ZArFVnzld%2FS36ZJdKAJFSuTiyx6xNpMNudwxOsodcTQgotZZkU%2FjPlO%2FAD9eeo633HD8PbH38AUovx1o; lui=155324276%3A1; sessid=4E127D1E-06D7-692D-5D25-846D07E03480; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%26ck%3D1954.2.71.150.186.466.366.128%26shh%3Dwww.baidu.com%26sht%3D99249017_hao_pg%26wd%3D%26eqid%3De3095cbe0001b528000000035c89ba9d; twe=2; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253Dl-3LX1r6uBCV3auM-JX6h5LpnufDG2wgkJh8JP0zlFS22Yr5zmWzhBPUXcmkDjK-%2526ck%253D1954.2.71.150.186.466.366.128%2526shh%253Dwww.baidu.com%2526sht%253D99249017_hao_pg%2526wd%253D%2526eqid%253De3095cbe0001b528000000035c89ba9d; new_uv=17; ctid=11; new_session=0; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1552476326,1552484406,1552522099,1552530085; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1552530085; wmda_session_id_6289197098934=1552531677416-0e21d10b-6652-26a9; _gat=1'},
    ]
    # proxy = {
    #     'https': 'https://218.60.8.83:3129',
    #     'http': 'http://218.60.8.83:3129',
    # }

    base_url = 'https://%s.zu.anjuke.com/fangyuan/'
    #
    url_list = ['bj','tj','dl','sjz','heb','sy','ty','cc','wei','wf','hhht','bt','sh','hz','su','nj','wx','jn','qd','ks','nb','nc','fz','hf','xz','zb','sz','gz','fs','cs','san','hui','dg','hk','zh','zs','xm','nn','qz','lzh','cd','cq','wh','zz','xa','km','gy','lz','ly']
    for i in url_list:
        url = base_url % i
        print(url)
        for i in range(1,51):
            newurl = url+'p%s/' % i
            print(newurl)
            sleep(random.randint(0,5))
            response = requests.get(newurl,headers=random.choice(headers))#,proxies=proxy
            sleep(1)
            text = response.content.decode('utf-8')
            html = etree.HTML(text)
            res = html.xpath('//h3/a/@href')
            sleep(1)
            for i in res:
                sleep(random.randint(0,5))
                response = requests.get(i,headers=random.choice(headers))#,proxies=proxy
                text = response.content.decode('utf-8')
                html = etree.HTML(text)
                res = html.xpath('//div[@class="wrapper"]')
                sleep(2)
                for j in res:
                    datahouse = {}
                    # 标题
                    title = ''.join(j.xpath('//h3[@class="house-title"]/text()')).replace('\t', '').replace('\n', '').replace(' ', '')
                    title = str(title)
                    # 编码
                    code = ''.join(j.xpath('//*[@id="houseCode"]//text()')[0]).replace('\t','').replace('\n','').replace(' ','').replace('，','').replace('房屋编码：','')
                    code = str(code)
                    # 发布时间
                    time = ''.join(j.xpath('//div[@class="right-info"]/text()')).replace('\t','').replace('\n','').replace(' ','').replace('，','').replace('发布时间：','')
                    # 租金
                    price = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[1]/span[@class="price"]//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 支付类型
                    type = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[1]/span[@class="type"]//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 房屋户型
                    house_type = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[2]/span[@class="info"]//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 房屋面积
                    house_area = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[3]/span[@class="info"]//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 房屋朝向
                    house_direct = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[4]/span[@class="info"]//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 楼层
                    floor = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[5]/span[@class="info"]//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 装修
                    house_decorate = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[6]/span[@class="info"]//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 房屋类型
                    house_typeto = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[7]/span[@class="info"]//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 小区
                    village = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[8]/a//text()')).replace('\t','').replace('\n','').replace(' ','')
                    # 要求
                    require = ''.join(j.xpath('//ul[@class="house-info-zufang cf"]/li[9]/span[@class="info"]//text()')).replace('\t','').replace('\n','').replace(' ','')

                    datahouse = {
                        'title':title,
                        'code': code,
                        'time': time,
                        'price':price,
                        'type': type,
                        'house_type':house_type,
                        'house_area':house_area,
                        'house_direct': house_direct,
                        'floor':floor,
                        'house_decorate':house_decorate,
                        'house_typeto':house_typeto,
                        'village':village,
                        'require':require,
                    }


                    field = ''
                    values = ''
                    for k,v in datahouse.items():
                        field += '`%s`,' % k
                        values += '"%s",' % v
                    print(datahouse)

                    field = field.strip(',')
                    values = values.strip(',')
                    sql = 'INSERT ignore INTO `renthouse` (%s) VALUES (%s)' % (field,values)
                    db.ping(reconnect=True)
                    cursor.execute(sql)
                    db.commit()
                    db.close()