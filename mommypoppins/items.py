# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item, Field

class MommypoppinsItem(Item):
    # define the fields for your item here like:
    event_name   = scrapy.Field()
    description  = scrapy.Field()
    age_group    = scrapy.Field()
    location     = scrapy.Field()
    price        = scrapy.Field()
    link		 = scrapy.Field()
    event_link   = scrapy.Field()
    date   = scrapy.Field()
