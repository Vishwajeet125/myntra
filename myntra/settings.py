# -*- coding: utf-8 -*-

# Scrapy settings for myntra project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

from os.path import abspath, dirname, join


BOT_NAME = 'myntra'

SPIDER_MODULES = ['myntra.spiders']
NEWSPIDER_MODULE = 'myntra.spiders'


# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}

# Configure item pipelines
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
#    'myntra.pipelines.SomePipeline': 300,
}

# Configure images pipeline
IMAGES_STORE = join(dirname(abspath(__file__)), '../../exports/myntra')

# Enable and configure HTTP caching (disabled by default)
HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
