# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlprojectItem(scrapy.Item):
    # define the fields for your item here like:
    celebrity_name = scrapy.Field()
    celebrity_img = scrapy.Field()
    celebrity_per_traits = scrapy.Field()
