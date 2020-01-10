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
       # self.collection = self.db['green_jobs']  # Jobのクロールはこちら
       self.collection = self.db['green_companies']  # Companyのクロールはこちら

    def close_spider(self, spider):
        """
        spiderの終了時にDBサーバーへの接続を切断する
        """
        self.client.close()

    def process_item(self, item, spider):
        # dup_check = self.collection.find({'job_url': item['job_url']}).count()  # jobはこっち
        dup_check = self.collection.find({'company': item['company']}).count()   # companyはこっち

        if dup_check == 0:
            self.collection.insert(dict(item))

        return item
