# -*- coding: utf-8 -*-
import scrapy
from recruite_info.items import GreenCompanyInfo


class GreenCompanyInfoSpider(scrapy.Spider):
    name = 'green-company-info'
    allowed_domains = ['green-japan.com']

    def start_requests(self):
        with open("green_company_urls.txt") as f:
            for q in f:
                yield scrapy.Request(q)

    def parse(self, response):
        company_info = GreenCompanyInfo()
        comapny_info_table = response.css("table.detail-content-table tr")

        for tr in comapny_info_table:
            cl_name = self.rmv_th_td(tr.css("th").get())
            if cl_name == "業界":
                indusry_list = tr.css("td a::text").extract()
                company_info["big_industry"] = list(set(indusry_list[0::2]))
                company_info["small_industry"] = indusry_list[1::2]
            elif cl_name == "企業の特徴":
                features_list = tr.css("li::text").extract()
                company_info["feature"] = features_list
            else:
                try:
                    key_name = self.get_key_name(cl_name)
                    company_info[key_name] = self.rmv_th_td(tr.css("td").get())
                except KeyError:
                    pass

        yield company_info

    def rmv_th_td(self, text):
        try:
            return text.replace("<td>", "").replace("</td>", "").replace("<th>", "").replace("</th>", "")
        except:
            return text

    def get_key_name(self, cl_name):
        key_table = {
            "会社名": "company",
            "業界": "big_industry",
            "企業の特徴": "feature",
            "資本金": "fund",
            "設立年月": "established_at",
            "代表者氏名": "CEO",
            "事業内容": "business_description",
            "株式公開（証券取引所）": "IPO",
            "主要株主": "shareholder",
            "主要取引先": "main_client",
            "従業員数": "num_of_employees",
            "平均年齢": "avg_age",
            "本社所在地": "address",
            "売上（3年分）": "sales_3years"
        }
        return key_table[cl_name]
