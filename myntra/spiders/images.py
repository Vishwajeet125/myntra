# -*- coding: utf-8 -*-
from scrapy import Request, Spider

from os.path import abspath, dirname, join
from string import strip


class ImagesSpider(Spider):
    name = "images"
    allowed_domains = ["myntra.com"]

    def start_requests(self):
        base_url = 'http://www.myntra.com/search-service/searchservice/search/filteredSearch'
        # Read in styleid(s)
        with open(join(dirname(abspath(__file__)), 'ids.txt'), 'r') as f:
            style_ids = map(strip, f)
        # Raise NameError if `styleids` is not present
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
        pass
