import scrapy
from ..items import CrawlprojectItem

class Crawl_Spider(scrapy.Spider):
    name = "celebrity"
    start_urls = [
        'https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1'
    ]
    def parse(self, response):
        items = CrawlprojectItem()
        all_div_crawl = response.css('div.mode-detail')
        for crawl in all_div_crawl:
            celebrity_name = crawl.css('.lister-item-header a::text').extract()
            celebrity_img = crawl.css('img').xpath('@src').extract()
            celebrity_per_traits = crawl.css('.text-small+ p::text').extract()
            items['celebrity_name'] = celebrity_name
            items['celebrity_img'] = celebrity_img
            items['celebrity_per_traits'] = celebrity_per_traits

            yield items
