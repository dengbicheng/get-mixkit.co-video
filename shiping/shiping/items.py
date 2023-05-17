# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShipingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #视频下载链接
    sp = scrapy.Field()
    #视频地址链接
    link = scrapy.Field()
    #视频名字
    name = scrapy.Field()
