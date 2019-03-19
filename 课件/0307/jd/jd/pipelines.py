# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class MysqlPipline(object):
    def __init__(self):
        try:
            self.db = pymysql.connect('127.0.0.1','root','123456','py17',charset='utf8')
            self.cursor = self.db.cursor()
        except:
            print('连接失败')
    def process_item(self,item,spider):
        pass
    def close_spider(self):
        self.db.close()

class JdPipeline(MysqlPipline):
    def process_item(self, item, spider):

        return item
