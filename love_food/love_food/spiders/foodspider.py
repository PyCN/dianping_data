# -*- coding: utf-8 -*-
#author zhangr
#thanks to Living
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import request,Request
from scrapy.selector import Selector
from love_food.items import LoveFoodItem  #引入items中的类

class Food(CrawlSpider):
    name = "foodspider"
    redis_key = 'foodspider:start_urls'
    start_urls = ['http://www.dianping.com/search/category/418/10']

    url = 'http://www.dianping.com/search/category/418/10' #下一页拼接字符串
    def parse(self, response):
        item = LoveFoodItem() #所有的网页数据
        selector = Selector(response)
        Foods = selector.xpath('//*[@id="shop-all-list"]/ul/li')
        for eachFood in Foods:
            restaurant = eachFood.xpath('div[2]/div[1]/a/h4/text()').extract()
            star = eachFood.xpath('div[2]/div[2]/span/@title').extract()
            average_price = eachFood.xpath('div[2]/div[2]/a[2]/b/text()').extract()
            foodtype = eachFood.xpath('div[2]/div[3]/a[1]/span/text()').extract()
            addr = eachFood.xpath('div[2]/div[3]/a[2]/span/text()').extract()
            if restaurant:
                print restaurant[0]
                item['restaurant'] = restaurant[0]
            else:
                item['restaurant'] = None
            if star:
                print star[0]
                item['star'] = star[0]
            else:
                item['star'] = None
            if average_price:
                print average_price[0]
                item['average_price'] = average_price[0]
            else:
                item['average_price'] = None
            if foodtype:
                print foodtype[0]
                item['foodtype'] = foodtype[0]
            else:
                item['foodtype'] = None
            if addr:
                print addr[0]
                item['addr'] = addr[0]
            else:
                item['addr'] = None

            yield item
        nextpage = selector.xpath('//*[@id="top"]/div[6]/div[3]/div[1]/div[2]/a/@href').extract()[-1]
        # nextpage 的标签容易出现变动
        # //*[@id="top"]/div[6]/div[3]/div[1]/div[2]/a[11] page1
        # //*[@id="top"]/div[6]/div[3]/div[1]/div[2]/a[12] page2
        # //*[@id="top"]/div[6]/div[3]/div[1]/div[2]/a[12] page3
        if nextpage:
            print nextpage,  'this is a *************************next page'
            # 字符串切片 拼接
            nextpage = nextpage[23:]
            yield Request(self.url+nextpage, callback=self.parse)
