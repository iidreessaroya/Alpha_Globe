import scrapy

from ..items import VisaJapanItem

class Travelspider(scrapy.Spider) :
    name = 'japanspider'
    start_urls = ['https://www.montreal.ca.emb-japan.go.jp/en/consular/visa_tourist_en.html']
    index=0
    visalist=['visa_business_en.html','visa_coe_en.html']
    item_data = ['', '', '', '', '', '']

    def parse(self, response):
        items = VisaJapanItem()
        country_name= 'Japan'
        Travelspider.item_data[0] = country_name
        if Travelspider.index == 0:
            visit_visa = response.xpath('//div[@class="text_area"]').extract()
            Travelspider.item_data[1] = visit_visa[0]
        if Travelspider.index == 1:
            business_visa = response.xpath('//div[@class="text_area"]').extract()
            Travelspider.item_data[2] = business_visa[0]
        if Travelspider.index == 2:
            study_visa = response.xpath('//div[@class="text_area"]').extract()
            Travelspider.item_data[3] = study_visa[0]
        if Travelspider.index == 2:
            emp_visa = response.xpath('//div[@class="text_area"]').extract()
            Travelspider.item_data[4] = emp_visa[0]
            items['name'] = Travelspider.item_data[0]
            items['visit_visa'] = Travelspider.item_data[1]
            items['business_visa'] = Travelspider.item_data[2]
            items['study_visa'] = Travelspider.item_data[3]
            items['employment_visa'] = Travelspider.item_data[4]
            yield items

        if Travelspider.index < 2:
            next_page = 'https://www.montreal.ca.emb-japan.go.jp/en/consular/' + Travelspider.visalist[Travelspider.index]
            Travelspider.index += 1
            yield response.follow(next_page, callback=self.parse)
