#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from redfin_information_searching_scrapy.redfin_information_searching_scrapy.items import \
    RedfinInformationSearchingScrapyItem
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('Analysis Template Automation test.xlsx', sheet_name='Data Base')
url = df['URL']
print(url)


class RedfinSpider(scrapy.Spider):
    name = 'redfin'
    allowed_domains = ['redfin.com']
    start_urls = url

    custom_settings = {
        "FEED_EXPORTERS": {'xlsx': 'scrapy_xlsx.XlsxItemExporter'},
        "FEED_FORMAT": 'xlsx',
        'FEED_URI': 'output.xlsx'
    }

    def parse(self, response):
        item = RedfinInformationSearchingScrapyItem()
        for redfin_estimate in response.css('.value.font-size-large::text').getall():
            item['Redfin_Estimate'] = redfin_estimate
        # there are a list of clickable span element in the website, so I need to see if there is a "Sold"
        # text in them
        for status in response.xpath('//*[@id="overview-scroll"]/div/div/div[2]/'
                                     'div[2]/span/span/span[2]/div/span/text()').getall():
            item['status'] = status
        item['url'] = response.url
        yield item


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(RedfinSpider)
process.start()
