# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
class JsonPipeline(object):
    def __init__(self):
        self.f = open('./img.json','w',encoding='utf-8')
    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item)))
        return item
    def close_spider(self,spider):
        self.f.close()

class Day1602Pipeline(JsonPipeline):
    def __init__(self):
        self.f = open('./goods.json','w',encoding='utf-8')

