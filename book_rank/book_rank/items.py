# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item,Field

class BookRankItem(scrapy.Item):
    # 定义需要爬取的内容
    # name = scrapy.Field()
    rank = Field()
    name = Field()
    author = Field()
    press = Field()
    publish_time = Field()
    view_number = Field()
