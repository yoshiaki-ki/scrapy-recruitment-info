# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class MongoPipeline:
    def open_spider(self, spider):
       self.client = MongoClient('localhost', 27017)
       self.db = self.client['scraping_green_job']
       self.collection = self.db['green_jobs']

    def close_spider(self, spider):
        """
        spiderの終了時にMySQLサーバーへの接続を切断する
        """
        self.conn.close()

    def process_item(self, item, spider):
        dup_check = self.collection.find({'job_title': item['job_title']}).count()
        if dup_check == 0:
            self.collection.insert(dict(item))

        return item
