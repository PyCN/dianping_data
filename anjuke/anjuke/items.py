# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_type = scrapy.Field()  #房子格局
    rent_type = scrapy.Field()   #出租类型：整租、合租
    renovation = scrapy.Field()  #装修情况
    address = scrapy.Field()     #地址
    owner = scrapy.Field()       #联系人
    price = scrapy.Field()       #出租价格
