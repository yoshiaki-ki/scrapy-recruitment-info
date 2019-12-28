# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urljoin

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recruite_info.items import Green



class GreenSpider(CrawlSpider):
    name = 'green'
    allowed_domains = ['green-japan.com']
    base_url = 'https://green-japan.com'
    start_urls = ['https://green-japan.com/search_key/01?key=2st6fzxsag8ckiplpi18&page=1']
    #start_urls = ['https://green-japan.com/search_key/01?key=2st6fzxsag8ckiplpi18&page={0}'.format(str(i)) for i in range(100)]

    allow_list = [r'/job/[0-9]+']# 'hoge.com/product'以下を正規表現でマッチング
    # restrict_list = ['//*[@id="srch-rslt"]']# スパイダーがスナイポするHTML要素

    rules = (
        Rule(LinkExtractor(
            allow=allow_list,
      #      restrict_xpaths=restrict_list,
            unique=True,
        ), callback='parse_item', follow=True),
    )

    # def start_requests(self):
    #     for i in range(1, 3):
    #         yield scrapy.Request('https://green-japan.com/search_key/01?key=2st6fzxsag8ckiplpi18&page=' + str(i))

    def parse_item(self, response):
        green = Green()
        green["job_tag"] = response.css('div.job-offer-icon::text').extract_first().strip()
        green["job_title"] = response.css('h2::text').extract_first().strip()
        green["job_url"] = response.url
        try:
            salary = response.css('ul.job-offer-meta-tags>li::text')[0].get().strip()
            min_max_salary = re.split('[~〜]', salary)
            green["min_salary"] = min_max_salary[0]
            green["max_salary"] = min_max_salary[1]
        except:
            green["min_salary"] = ""
            green["max_salary"] = ""
        try:
            green["locate"] = response.css('ul.job-offer-meta-tags>li::text')[1].get().strip()
        except:
            green["locate"] = ""
        try:
            green["language"] = response.css('ul.job-offer-meta-tags>li::text')[2].get().strip()
        except:
            green["language"] = ""
        try:
            green["company"] = response.css('div.company-info-box>section>h4::text').get().strip()
        except:
            green["company"] = ""
        try:
            company_url = response.css('div.company-info-box__btn-area>li:nth-child(2)>a::attr(href)').get().strip()
            company_url_mod = re.sub("\?.+", "", company_url)

            green["company_url"] = urljoin('https://green-japan.com', company_url_mod)

        except:
            green["company_url"] = ""
        try:
            green["big_occupation"] = response.css('div.std_box>div:nth-child(3)>p>a::text')[0].get()
        except:
            green["big_occupation"] = ""
        try:
            green["small_occupation"] = response.css('div.std_box>div:nth-child(3)>p>a::text')[1].get()
        except:
            green["small_occupation"] = ""

        yield green

