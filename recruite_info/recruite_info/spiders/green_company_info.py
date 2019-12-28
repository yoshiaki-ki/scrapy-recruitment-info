# -*- coding: utf-8 -*-
import scrapy


class GreenCompanyInfoSpider(scrapy.Spider):
    name = 'green-company-info'
    allowed_domains = ['green-japan.com']
    start_urls = ['http://green-japan.com/']

    def parse(self, response):
        pass
