# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.selector import Selector

from ..items import MyntraItem

from os.path import abspath, dirname, join
from urlparse import urljoin
from string import strip
import json


class ImagesSpider(Spider):
    name = "images"
    allowed_domains = ["myntra.com"]

    def start_requests(self):
        base_url = 'http://www.myntra.com/search-service/searchservice/search/filteredSearch'
        # Read in styleid(s)
        with open(join(dirname(abspath(__file__)), 'ids.txt'), 'r') as f:
            style_ids = map(strip, f)
        # Raise NameError if `style_ids` is not present
        if not style_ids:
            raise NameError('Make sure ids.txt exists and has valid entries!')

        for style_id in style_ids:
            payload = '[{"fq":["count_options_availbale:[1 TO *]"],' \
                      '"query":"styleid : %s AND  (count_options_availbale:[' \
                      '0 TO *])",' \
                      '"start":0,' \
                      '"rows":15,' \
                      '"return_docs":true,' \
                      '"facet":false,' \
                      '"sort":[]}]' % style_id
            yield Request(url=base_url, method='POST', body=payload)

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        item = MyntraItem()
        item['product'] = data['response1']['products'][0]['product']
        item['styleid'] = data['response1']['products'][0]['styleid']
        item['dre_landing_page_url'] = data['response1']['products'][0]['dre_landing_page_url']
        item['global_attr_article_type'] = data['response1']['products'][0]['global_attr_article_type']
        item['global_attr_base_colour'] = data['response1']['products'][0]['global_attr_base_colour']
        item['gender_from_cms'] = data['response1']['products'][0]['gender_from_cms']
        item['visual_tag'] = data['response1']['products'][0]['visual_tag']
        item['product_additional_info'] = data['response1']['products'][0]['product_additional_info']

        # Build the web page url
        web_page = urljoin('http://www.myntra.com/', item['dre_landing_page_url'])
        # Call the parse function for the web page
        yield Request(url=web_page,
                      callback=self.parse_web,
                      meta={'item': item})

    def parse_web(self, response):
        selector = Selector(response=response)
        item = response.meta['item']
        # Extract product details
        item['product_details'] = selector.xpath('//div[contains(@class, "description") and contains(@class, "stylenote")]/following-sibling::div[1]//text()[normalize-space()]').extract()[0]
        yield item
