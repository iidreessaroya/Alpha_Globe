# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BasicinfoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    validity = scrapy.Field()
    blank_pages = scrapy.Field()
    visa_required = scrapy.Field()
    vaccination = scrapy.Field()
    amount_entry = scrapy.Field()
    amount_exit = scrapy.Field()