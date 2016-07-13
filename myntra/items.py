# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MyntraItem(Item):
    image_urls = Field()
    images = Field()
    image_paths = Field()
    product = Field()
    dre_landing_page_url = Field()
    global_attr_article_type = Field()
    visual_tag = Field()
    global_attr_base_colour = Field()
    gender_from_cms = Field()
    styleid = Field()
    product_additional_info = Field()
    product_details = Field()
