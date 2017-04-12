# -*- coding: utf-8 -*-
#author zhangr

import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import request, Request
from scrapy.selector import Selector
from anjuke.items import AnjukeItem  #引入items中的类

class Anjuke(CrawlSpider):
    name = "anjuke_spider"
    allowed_domains = ["sh.zu.anjuke.com"]
    start_urls = ['http://sh.zu.anjuke.com'] #安居客租房链接地址

    def parse(self, response):
        item = AnjukeItem() #所有数据
        selector = Selector(response)
        HouseData = selector.xpath('//*[@id="list-content"]/div')  #div[1],div[2]需要舍弃
        for eachhouse in HouseData[3:]:
            house_type = eachhouse.xpath('div[1]/p[1]/text()[1]').extract()
            rent_type = eachhouse.xpath('div[1]/p[1]/text()[2]').extract()
            renovation = eachhouse.xpath('div[1]/p[1]/text()[3]').extract()
            address = eachhouse.xpath('div[1]/address/text()').extract()
            owner = eachhouse.xpath('div[1]/p[2]/span/text()').extract()
            price = eachhouse.xpath('div[2]/p/strong/text()').extract() #不要写成/div[2]/p/...没看清坑了自己

            if house_type:
                item['house_type'] = house_type
            else:
                item['house_type'] = None
            if rent_type:
                item['rent_type'] = rent_type
            else:
                item['rent_type'] = None
            if renovation:
                item['renovation'] = renovation
            else:
                item['renovation'] = None
            if address:
                item['address'] = address
            else:
                item['address'] = None
            if owner:
                item['owner'] = owner
            else:
                item['owner'] = None
            if price:
                item['price'] = price
            else:
                item['price'] = None
            yield item

        nextpage = selector.xpath('//div[@class="multi-page"]/a/@href').extract()[-1] #取最后一个href，顺序无法取
        print nextpage
        if nextpage:
            yield Request(nextpage,callback=self.parse)


