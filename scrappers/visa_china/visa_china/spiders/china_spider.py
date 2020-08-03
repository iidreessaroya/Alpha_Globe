import scrapy

from ..items import VisaChinaItem

class Travelspider(scrapy.Spider) :
    name = 'chinaspider'
    start_urls = ['http://pk.chineseembassy.org/eng/lsfw/va/t1573128.htm']
    def parse(self, response):
        items = VisaChinaItem()
        country_name= 'china'
        items['name'] = country_name
        visa = response.xpath('//div[@id="News_Body_Txt_A"]').extract()
        items['visa'] = visa[0]
        yield items