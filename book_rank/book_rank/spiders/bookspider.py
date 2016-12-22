# -*- coding: utf-8 -*-
#author zhangr

import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import request,Request
from scrapy.selector import Selector
import sys
import urllib
import urllib2
import cookielib
from book_rank.items import BookRankItem  #引入items中的类

class Book(CrawlSpider):
    name = "bookspider"
    start_urls = [
        "http://opac.zjgtsg.com/opac/ranking/bookLoanRank"
    ]
    ReadID = ''  # 登录系统的账号，这里是身份证号码
    ReadPasswd = '14e52634c81e53e0ef7f87b034eab171'  # 登录密码的密文，POST中得到的

    def login_url(self):
        self.loginUrl = 'http://opac.zjgtsg.com/opac/reader/space'
        self.cookies = cookielib.CookieJar()
        # 自行分析POST的数据，这个系统不需要验证码
        self.postdata = urllib.urlencode({
            'rdid': ReadID,
            'rdPasswd': ReadPasswd
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def parse(self, response):
        item = BookRankItem()
        selector = Selector(response)
        Books = selector.xpath('//*[@id="contentTable"]')  #获取页面所有图书信息

        for eachBook in Books:
            rank = eachBook.xpath('/tbody/tr[2]/td[1]/text()').extract()
            name = eachBook.xpath('/tbody/tr[2]/td[2]/a/text()').extract()
            author = eachBook.xpath('/tbody/tr[2]/td[3]/text()').extract()
            view_number = eachBook.xpath('/tbody/tr[2]/td[4]/text()').extract()

            item['rank'] = rank
            item['name'] = name
            item['author'] = author
            item['press'] = press
            item['publish_time'] = publish_time
            item['view_number'] = view_number

            yield item