import scrapy

from ..items import VisaEnglandItem

class Travelspider(scrapy.Spider) :
    name = 'englandspider'
    start_urls = ['https://www.gov.uk/tier-4-general-visa']
    index=0
    visalist=['standard-visitor-visa','tier-2-general','tier-1-investor']
    item_data = ['', '', '', '', '', '']

    def parse(self, response):
        items = VisaEnglandItem()
        country_name= 'England'
        Travelspider.item_data[0] = country_name
        if Travelspider.index == 1:
            visit_visa = response.xpath('//div[@class="govuk-grid-column-two-thirds"]')[2].extract()
            Travelspider.item_data[1] = visit_visa
        if Travelspider.index == 3:
            business_visa = response.xpath('//div[@class="govuk-grid-column-two-thirds"]')[2].extract()
            Travelspider.item_data[2] = business_visa
            items['name'] = Travelspider.item_data[0]
            items['visit_visa'] = Travelspider.item_data[1]
            items['business_visa'] = Travelspider.item_data[2]
            items['study_visa'] = Travelspider.item_data[3]
            items['employment_visa'] = Travelspider.item_data[4]
            yield items
        if Travelspider.index == 0:
            study_visa = response.xpath('//div[@class="govuk-grid-column-two-thirds"]')[2].extract()
            Travelspider.item_data[3] = study_visa
        if Travelspider.index == 2:
            emp_visa = response.xpath('//div[@class="govuk-grid-column-two-thirds"]')[2].extract()
            Travelspider.item_data[4] = emp_visa

        if Travelspider.index < 3:
            next_page = 'https://www.gov.uk/' + Travelspider.visalist[Travelspider.index]
            Travelspider.index += 1
            yield response.follow(next_page, callback=self.parse)
