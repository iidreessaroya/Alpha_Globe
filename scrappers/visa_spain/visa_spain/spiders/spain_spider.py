import scrapy

from ..items import VisaSpainItem

class Travelspider(scrapy.Spider) :
    name = 'spainspider'
    start_urls = ['https://www.schengenvisainfo.com/spain-visa/']
    def parse(self, response):
        items = VisaSpainItem()
        country_name= 'spain'
        items['name'] = country_name
        visa = response.xpath('//div[@class="content"]').extract()
        items['visa'] = visa[0]
        yield items