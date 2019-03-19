# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):
        return item

class BlogPipeline(object):
    def __init__(self):
        self.f = open('./blog.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        # 存数据
        self.f.write(json.dumps(dict(item))+'\n')
        return item
    def spider_close(self):
        # 关闭文件操作
        self.f.close()