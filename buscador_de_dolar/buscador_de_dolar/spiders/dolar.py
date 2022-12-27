import scrapy

class DolarToScrapeSpider(scrapy.Spider):
    name = 'valordolarbot'

    def start_requests(self):
        urls = ["https://br.investing.com/currencies/exchange-rates-table"]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        for elemento in response.xpath("//table[@id='exchange_rates_1']"):
            yield {
                'Dolar': elemento.xpath(".//td[@id='last_12_35']/text()").get(),
                'Euro': elemento.xpath(".//td[@id='last_17_35']/text()").get(),  
            }
       
