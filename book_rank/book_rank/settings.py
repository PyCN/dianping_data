# -*- coding: utf-8 -*-

# Scrapy settings for book_rank project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'book_rank'

SPIDER_MODULES = ['book_rank.spiders']
NEWSPIDER_MODULE = 'book_rank.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'book_rank (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

USER_AGENT = 'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
COOKIES_ENABLED = False
DOWNLOAD_DELAY = 3
# Obey robots.txt rules

# 以csv文件进行保存
FEED_URI = u'file:///E:/book_rank.csv'
FEED_FORMAT = 'CSV'
