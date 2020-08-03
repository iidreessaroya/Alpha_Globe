import scrapy

from ..items import VisaAmericaItem

class Travelspider(scrapy.Spider) :
    name = 'americaspider'
    start_urls = ['https://www.ustraveldocs.com/pk/pk-niv-typej.asp']
    index=0
    visalist=['pk-niv-typeb1b2.asp','pk-niv-typefandm.asp','pk-niv-typework.asp']
    item_data=['','','','','','']

    def parse(self, response):
        items = VisaAmericaItem()
        country_name= 'America'
        Travelspider.item_data[0] = country_name
        if Travelspider.index == 0:
            visit_visa = response.xpath('//div[@class="editable"]').extract()
            Travelspider.item_data[1] = visit_visa[0]
        if Travelspider.index == 1:
            business_visa = response.xpath('//div[@class="editable"]').extract()
            Travelspider.item_data[2] = business_visa[0]
        if Travelspider.index == 2:
            study_visa = response.xpath('//div[@class="editable"]').extract()
            Travelspider.item_data[3] = study_visa[0]
        if Travelspider.index == 3:
            emp_visa = response.xpath('//div[@class="editable"]').extract()
            Travelspider.item_data[4] = emp_visa[0]
            items['name'] = Travelspider.item_data[0]
            items['visit_visa'] = Travelspider.item_data[1]
            items['business_visa'] = Travelspider.item_data[2]
            items['study_visa'] = Travelspider.item_data[3]
            items['employment_visa'] = Travelspider.item_data[4]
            yield items
        if Travelspider.index < 3:
            next_page = 'https://www.ustraveldocs.com/pk/' + Travelspider.visalist[Travelspider.index]
            Travelspider.index += 1
            yield response.follow(next_page, callback=self.parse)
