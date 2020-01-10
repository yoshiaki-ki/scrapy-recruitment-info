# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Green(scrapy.Item):
    job_tag = scrapy.Field()
    job_title = scrapy.Field()
    job_url = scrapy.Field()
    max_salary = scrapy.Field()
    min_salary = scrapy.Field()
    locate = scrapy.Field()
    language = scrapy.Field()
    company = scrapy.Field()
    company_url = scrapy.Field()
    big_occupation = scrapy.Field()
    small_occupation = scrapy.Field()


class GreenCompanyInfo(scrapy.Item):
    company = scrapy.Field()
    company_url = scrapy.Field()
    big_industry = scrapy.Field()
    small_industry = scrapy.Field()
    feature = scrapy.Field()
    fund = scrapy.Field()
    established_at = scrapy.Field()
    CEO = scrapy.Field()
    business_description = scrapy.Field()
    IPO = scrapy.Field()
    shareholder = scrapy.Field()
    main_client = scrapy.Field()
    num_of_employees = scrapy.Field()
    avg_age = scrapy.Field()
    address = scrapy.Field()
    sales_3years = scrapy.Field()