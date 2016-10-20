# -*- coding: utf-8 -*-

# Scrapy settings for love_food project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'love_food'

SPIDER_MODULES = ['love_food.spiders']
NEWSPIDER_MODULE = 'love_food.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
COOKIES_ENABLED = False
DOWNLOAD_DELAY = 3
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

FEED_URI = u'file:///D:/food_data.csv'
FEED_FORMAT = 'CSV'
