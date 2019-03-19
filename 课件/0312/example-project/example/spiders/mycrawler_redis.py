from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    allowed_domains = ['lagou.com']
    redis_key = 'mycrawler:start_urls' # redis中的key

    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )



    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
