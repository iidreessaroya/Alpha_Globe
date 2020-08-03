import scrapy

from ..items import GermanVisasItem

class Travelspider(scrapy.Spider) :
    name = 'germanspider'
    start_urls = ['https://www.germany-visa.org/student-visa']
    index=0
    visalist=['schengen-visa','business-visa','work-employment-visa']
    item_data=['','','','','','']

    def parse(self, response):
        items = GermanVisasItem()
        country_name= 'Germany'
        Travelspider.item_data[0] = country_name
        if Travelspider.index == 0:
            study_visa = response.xpath('//div[@class="post-content"]').extract()
            Travelspider.item_data[1] = self.filter_data(study_visa[0])
        if Travelspider.index == 1:
            visit_visa = response.xpath('//div[@class="post-content"]').extract()
            Travelspider.item_data[2] = self.filter_data(visit_visa[0])
        if Travelspider.index == 2:
            business_visa = response.xpath('//div[@class="post-content"]').extract()
            Travelspider.item_data[3] = self.filter_data(business_visa[0])
        if Travelspider.index == 3:
            emp_visa = response.xpath('//div[@class="post-content"]').extract()
            Travelspider.item_data[4] = self.filter_data(emp_visa[0])
            items['name'] = Travelspider.item_data[0]
            items['study_visa'] = Travelspider.item_data[1]
            items['visit_visa'] = Travelspider.item_data[2]
            items['business_visa'] = Travelspider.item_data[3]
            items['employment_visa'] = Travelspider.item_data[4]
            yield items
        if Travelspider.index < 3:
            next_page = 'https://www.germany-visa.org/' + Travelspider.visalist[Travelspider.index]
            Travelspider.index += 1
            yield response.follow(next_page, callback=self.parse)

    def filter_data(self,data):
        data=data[data.find('>')+1:len(data)-6]
        return data





