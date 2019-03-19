from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    # allowed_domains = ['hao123.org']
    start_urls = ['http://www.hao123.com/']

    rules = [
        Rule(LinkExtractor(), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
            yield {
                'name': response.css('title::text').extract_first(),
            }
            print(response.css('title::text').extract_first())
