import scrapy

from ..items import VisaItalyItem

class Travelspider(scrapy.Spider) :
    name = 'italyspider'
    start_urls = ['https://www.schengenvisainfo.com/italy-visa/']
    def parse(self, response):
        items = VisaItalyItem()
        country_name= 'italy'
        items['name'] = country_name
        visa = response.xpath('//div[@class="content"]').extract()
        items['visa'] = visa[0]
        yield items