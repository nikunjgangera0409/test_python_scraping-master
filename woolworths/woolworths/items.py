# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WoolworthsItem(scrapy.Item):
    item_url = scrapy.Field()
    Name = scrapy.Field()
    Price = scrapy.Field()
    thumbnail_url = scrapy.Field()

    
    pass
