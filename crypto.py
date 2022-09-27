import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd 
import fileinput

class CryptoSpider(scrapy.Spider):
    name = 'crypto'
    allowed_domains = ['www.coingecko.com']
    start_urls = [f'https://www.coingecko.com/?page={j}' for j in range(1,130)]

    def parse(self, response):
        # names =[]
        # for current in response.xpath("/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr/td[3]/div/div[2]/a/span[1]/text()"):
        #     names.append(current.get().replace('\n',''))
        # prices=[]
        # for price in response.xpath('/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr/td[4]/div/div[2]/span/text()'):
        #     prices.append(price.get().replace('$','').replace(',',''))
        
        # volume24hs=[]
        # for v in response.xpath('/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr/td[8]/span/text()'):
        #     volume24hs.append(v.replace('$','').replace(',',''))
        # marketcaps=[]
        # for mkt in response.xpath('/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr/td[9]/span/text()'):
        #     marketcaps.append(mkt.get().replace('$','').replace(',',''))
        # onehour=[]
        # for one in response.xpath('/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr/td[5]/span/text()'):
        #     onehour.append(one.get())
        # adayevo=[]
        # for day in response.xpath('/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr/td[6]/span/text()'):
        #     adayevo.append(day.get())
        # weekevo=[]
        # for week in response.xpath('/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr/td[7]/span/text()'):
        #     weekevo.append(week.get())
        
        
        for i in range(100):
            yield {
                'Coin':response.xpath(f"/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[{i+1}]/td[3]/div/div[2]/a/span[1]/text()").get().replace('\n',''),
                'Price':response.xpath(f'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[{i+1}]/td[4]/div/div[2]/span/text()').get().replace('$','').replace(',',''),
                '1h evolution':response.xpath(f'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[{i+1}]/td[5]/span/text()').get(),
                '24h evolution':response.xpath(f'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[{i+1}]/td[6]/span/text()').get(),
                '7d evolution':response.xpath(f'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[{i+1}]/td[7]/span/text()').get(),
                '24h Volume':response.xpath(f'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[{i+1}]/td[8]/span/text()').get().replace('$','').replace(',',''),
                'Market Cap':response.xpath(f'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[{i+1}]/td[9]/span/text()').get().replace('$','').replace(',','')
            }
            
            # for i in range(len(names)):
            #     yield {
            #         'Coin':names[i],
            #         'Price':prices[i],
            #         '1h evolution':onehour[i],
            #         '24h evolution':adayevo[i],
            #         '7d evolution':weekevo[i],
            #         '24h Volume':volume24hs[i],
            #         'Market Cap':marketcaps[i]
            #     }
            

    



process = CrawlerProcess(
    settings = {
        'FEEDS':{
            'cryptocurrencies.csv':{
                'format':'csv'
            }
        }
    }
)

process.crawl(CryptoSpider)
process.start()
# with open('cryptocurrencies.csv','r') as in_file, open('cryptocurrencies2.csv','w') as out_file:
  
#     seen = set() # set for fast O(1) amortized lookup
    
#     for line in in_file:
#         if line in seen: 
#           continue # skip duplicate

#         seen.add(line)
#         out_file.write(line)



seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput('cryptocurrencies.csv', inplace=1):
    if line not in seen:
        seen.add(line)
        print (line) # standard output is now redirected to the file 

