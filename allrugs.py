import scrapy
from scrapy.crawler import CrawlerProcess

class AllrugsSpider(scrapy.Spider):
    name = 'allrugs'
    allowed_domains = ['therugshopuk.co.uk']
    start_urls = [f'https://www.therugshopuk.co.uk/rugs-by-type/rugs.html?p={j}' for j in range (1,150)]

    def parse(self, response):
        for item in response.css('div.product-item-info'):
            yield {
                'title':item.css('img.product-image-photo.image::attr(alt)').get() ,
                'link':item.css('a.product-item-link::attr(href)').get() ,
                'price in Euro': item.css('span.price::text').get().replace('£','') 
            }
            
        # nextpage=response.css('a[title=Next]::attr(href)').get()
        # if nextpage is not None :
        #     yield response.follow(nextpage,callback=self.parse)
        

process = CrawlerProcess(
    settings = {
        'FEEDS':{
            'data.csv':{
                'format':'csv'
            }
        }
    }
)

process.crawl(AllrugsSpider)
process.start()