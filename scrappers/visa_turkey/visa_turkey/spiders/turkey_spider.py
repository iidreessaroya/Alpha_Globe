import scrapy

from ..items import VisaTurkeyItem


class Visa_Turkey(scrapy.Spider) :
    name = 'turkeyspider'
    start_urls = ['http://www.mfa.gov.tr/visa-information-for-foreigners.en.mfa']
    index = 0

    def parse(self, response):
        items = VisaTurkeyItem()
        country_name = 'Turkey'
        Data = response.xpath('//div[@class="info"]/div/text()')[0].extract()
        while Visa_Turkey.index <= 48:
            Data_1 = response.xpath('//div[@class="info"]/div/p/text()')[Visa_Turkey.index].extract()
            Data = Data + Data_1
            Visa_Turkey.index += 1
        items['name'] = country_name
        items['data'] = Data

        yield items
