# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RedfinInformationSearchingScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Redfin_Estimate = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()