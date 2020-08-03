import scrapy

from ..items import VisaOmanItem

class Travelspider(scrapy.Spider) :
    name = 'omanspider'
    start_urls = ['https://www.rop.gov.om/old/english/dg_pr_visas_tourist.asp']
    index=0
    visalist=['dg_pr_visas_investor.asp','dg_pr_visas_student.asp','dg_pr_visas_employment.asp']
    item_data=['','','','','','']

    def parse(self, response):
        items = VisaOmanItem()
        country_name= 'Oman'
        Travelspider.item_data[0] = country_name
        if Travelspider.index == 0:
            visit_visa = response.xpath('//div[@id="item1"]').extract()
            Travelspider.item_data[1] = self.filter_data(visit_visa[0])
        if Travelspider.index == 1:
            business_visa = response.xpath('//div[@id="item1"]').extract()
            Travelspider.item_data[2] = self.filter_data(business_visa[0])
        if Travelspider.index == 2:
            study_visa = response.xpath('//div[@id="item1"]').extract()
            Travelspider.item_data[3] = self.filter_data(study_visa[0])
        if Travelspider.index == 3:
            emp_visa = response.xpath('//div[@id="item1"]').extract()
            Travelspider.item_data[4] = self.filter_data(emp_visa[0])
            items['name'] = Travelspider.item_data[0]
            items['visit_visa'] = Travelspider.item_data[1]
            items['business_visa'] = Travelspider.item_data[2]
            items['study_visa'] = Travelspider.item_data[3]
            items['employment_visa'] = Travelspider.item_data[4]
            yield items
        if Travelspider.index < 3:
            next_page = 'https://www.rop.gov.om/old/english/' + Travelspider.visalist[Travelspider.index]
            Travelspider.index += 1
            yield response.follow(next_page, callback=self.parse)

    def filter_data(self,data):
        data=data[0:data.find('<span class="sectionTitle">Other Visa Types')]
        data = data + '</div>'
        return data