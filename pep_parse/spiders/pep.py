import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.css('section#numerical-index tbody tr')
        for pep_url in peps:
            pep = pep_url.css('td a::attr(href)').getall()[0]
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        h1 = response.css('h1.page-title::text').get().strip()
        number_of_pep = h1.partition(' – ')[0]
        data = {
            'number': number_of_pep.replace('PEP ', ''),
            'name': h1,
            'status': response.css('dt:contains("Status") + dd::text').get(),
        }
        yield PepParseItem(data)
