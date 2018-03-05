# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnDbpediacrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    entity1 = scrapy.Field()
    relation = scrapy.Field()
    entity2 = scrapy.Field()
