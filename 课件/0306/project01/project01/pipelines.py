# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


class Project01Pipeline(object):
    def __init__(self):
        self.f = open('./proxy.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
        return item

    def close_spider(self, spider):
        self.f.close()


class TenContItem(object):
    def __init__(self):
        self.f = open('./teng.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()


class MydbPipline(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123456",database='p4',charset='utf8')
            self.cursor = self.db.cursor()
        except:
            print('连接失败')

    def process_item(self,item,spider):
        data = dict(item)
        sql = 'insert ignore into `proxy` values(null,%s,%s)'
        self.cursor.execute(sql,(data['ip'],data['port']))
        self.db.commit()
        return item
    def close_spider(self,spider):
        self.db.close()



