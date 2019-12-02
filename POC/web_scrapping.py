import scrapy
import re
from scrapy.crawler import CrawlerProcess
import json

class StackOverFlowRegionSpider(scrapy.Spider):
    name = "StackOverFlow_Region_Spider"
    
    def start_requests( self, str ):
        print(str)
        url = "https://data.stackexchange.com/stackoverflow/query/1160769?Location=Melbourne"
        yield scrapy.Request( url = url, callback = self.parse )

    def parse( self, response ):
        script_items = response.css('script')[8]
        data = script_items.extract()
        start = data.find('"resultSets": [')
        end = data.find("})")
        
        #json_data = json.load(data[start - 1:end + 1])
        content = data[start - 1:end + 1].replace("\r\n","")
        content = content.strip()
        content = "{" + content
        content = content.replace('\"','"')
        content = content.replace('  ',"")
        my_json = json.loads(content)
        
        print(len(my_json["resultSets"][0]["rows"]))
        print("\n\n\n")


process = CrawlerProcess()
process.crawl(StackOverFlowRegionSpider)
process.start("test")