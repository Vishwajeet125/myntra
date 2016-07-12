# -*- coding: utf-8 -*-
import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["myntra.com"]
    start_urls = (
        'http://www.myntra.com/',
    )

    def parse(self, response):
        pass
