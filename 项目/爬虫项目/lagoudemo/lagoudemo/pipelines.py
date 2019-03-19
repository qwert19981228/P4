# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql


class LagoudemoPipeline(object):
    def __init__(self):
        self.f = open('job.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
        return item

    def close_spider(self,response,spider):
        self.f.close()

class MySQLPipeline(object):

    def __init__(self):
        try:
            self.db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", database='p4',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.db.cursor()
        except:
            print('连接失败')

    def process_item(self, item, spider):
        data = dict(item)
        sql = 'insert ignore into `lagou` (`pname`,`money`,`location`,`year`,`degree`,`ptype`,`tags`,`date_pub`,`advantage`,`jobdesc`,`jobaddr`,`company`,`startmoney`,`endmoney`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, (data['pname'], data['money'],data['location'],data['year'],data['degree'],data['ptype'],data['tags'],data['date_pub'],data['advantage'],data['jobdesc'],data['jobaddr'],data['company'],data['startmoney'],data['endmoney']))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.close()



