import scrapy
from datetime import datetime
from utils.email_send import Emailer

class DolarToScrapeSpider(scrapy.Spider):
    name = 'valordolarbot'

    def start_requests(self):
        urls = ["https://br.investing.com/currencies/exchange-rates-table"]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        for elemento in response.xpath("//table[@id='exchange_rates_1']"):
            yield {
                'dolar': elemento.xpath(".//td[@id='last_12_35']/text()").get(),
                'euro': elemento.xpath(".//td[@id='last_17_35']/text()").get(),
                'libra': elemento.xpath(".//td[@id='last_3_35']/text()").get(),
                'iene': elemento.xpath(".//td[@id='last_2_35']/text()").get()
            }
       
        email = Emailer('willdesenvolvedorweb@gmail.com', 'zbvevzyvabsikhdk' )
        lista_de_contatos = ['willsantos.edf@gmail.com']
        lista_de_arquivos = ['cotacao.csv']
        email.definir_conteudo('Cotações das moedas', 'willdesenvolvedorweb@gmail.com', lista_de_contatos,"Bom dia!\nSegue em anexo os valores atuais das cotações das moedas." )
        email.anexar_arquivos(lista_de_arquivos)
        email.enviar_email(30)