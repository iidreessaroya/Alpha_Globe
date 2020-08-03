# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VisaNorwayItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    study_visa = scrapy.Field()
    visit_visa = scrapy.Field()
    business_visa = scrapy.Field()
    employment_visa = scrapy.Field()
