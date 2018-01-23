# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TxzpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 职位名
    positionName = scrapy.Field()
    # 职位链接
    positionLink = scrapy.Field()
    # 职位类别
    positionType = scrapy.Field()
    # 职位人数
    positionNum = scrapy.Field()
    # 工作地点
    positionAddress = scrapy.Field()
    # 职位发布时间
    positionTime = scrapy.Field()
