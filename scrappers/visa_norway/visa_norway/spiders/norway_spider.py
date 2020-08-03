import scrapy

from ..items import VisaNorwayItem

class Travelspider(scrapy.Spider) :
    name = 'norwayspider'
    start_urls = ['https://www.norway.no/en/pakistan/services-info/visitors-visa-res-permit/visitors-visa']
    index=0
    visalist=['https://www.norway.no/en/pakistan/services-info/business/','https://www.norway.no/en/pakistan/services-info/studying/','https://www.nav.no/en/home/work-and-stay-in-norway/work-in-norway']
    item_data=['','','','','','']

    def parse(self, response):
        items = VisaNorwayItem()
        country_name= 'norway'
        Travelspider.item_data[0] = country_name
        if Travelspider.index == 0:
            visit_visa = response.xpath('//section[@class="process padded"]').extract()
            Travelspider.item_data[1] = visit_visa[0]
        if Travelspider.index == 1:
            business_visa = response.xpath('//div[@class="container"]').extract()
            Travelspider.item_data[2] = self.filter_data(business_visa[0])
        if Travelspider.index == 2:
            study_visa = response.xpath('//div[@class="container"]').extract()
            Travelspider.item_data[3] = study_visa[0]
        if Travelspider.index == 3:
            emp_visa = response.xpath('//article[@class="full-article"]').extract()
            Travelspider.item_data[4] = emp_visa[0]
            items['name'] = Travelspider.item_data[0]
            items['visit_visa'] = Travelspider.item_data[1]
            items['business_visa'] = Travelspider.item_data[2]
            items['study_visa'] = Travelspider.item_data[3]
            items['employment_visa'] = Travelspider.item_data[4]
            yield items
        if Travelspider.index < 3:
            next_page = Travelspider.visalist[Travelspider.index]
            Travelspider.index += 1
            yield response.follow(next_page, callback=self.parse)

    def filter_data(self,data):
        data=data[0:data.find('<div class="panels service-panel">')]
        data = data + '</div>'
        return data
