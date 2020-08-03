import scrapy

from ..items import BasicinfoItem


class Travelspider(scrapy.Spider):
    name = 'basicinfo'
    start_urls = [
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Turkey.html']
    countries = ['Germany', 'Norway', 'UnitedKingdom', 'Spain', 'China', 'Japan', 'Italy', 'Oman',
                 'SaudiArabia','america']
    index = 0

    def parse(self, response):
        items = BasicinfoItem()
        index_p = 0
        country_name = Travelspider.countries[Travelspider.index]
        validity = response.xpath('//div[@class="tsg-rwd-qf-box-data"]/p/text()')[index_p].extract()
        index_p += 1
        if Travelspider.index == 3 or Travelspider.index == 7:
            validity_1 = response.xpath('//div[@class="tsg-rwd-qf-box-data"]/p/text()')[index_p].extract()
            if Travelspider.index == 3:
                validity = validity + 'duration of stay in United Kingdom' + validity_1
            index_p += 1
        blank_pages = response.xpath('//div[@class="tsg-rwd-qf-box-data"]/p/text()')[index_p].extract()
        index_p += 1
        visa_required = response.xpath('//div[@class="tsg-rwd-qf-box-data"]/p/text()')[index_p].extract()
        index_p += 1
        vaccination = response.xpath('//div[@class="tsg-rwd-qf-box-data"]/p/text()')[index_p].extract()
        index_p += 1
        amount_entry = response.xpath('//div[@class="tsg-rwd-qf-box-data"]/p/text()')[index_p].extract()
        index_p += 1
        amount_exit = response.xpath('//div[@class="tsg-rwd-qf-box-data"]/p/text()')[index_p].extract()

        items['name'] = country_name
        items['validity'] = validity
        items['blank_pages'] = blank_pages
        items['visa_required'] = visa_required
        items['vaccination'] = vaccination
        items['amount_entry'] = amount_entry
        items['amount_exit'] = amount_exit

        yield items

        next_page = 'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/' + \
                    Travelspider.countries[Travelspider.index] + '.html'
        if Travelspider.index < 10:
            Travelspider.index += 1
            yield response.follow(next_page, callback=self.parse)