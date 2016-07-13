# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PathExtraction(object):
    def process_item(self, item, spider):
        path = list()
        for image in item['images']:
            path.append(image['path'])
        item['image_paths'] = ';'.join(path)
        return item
