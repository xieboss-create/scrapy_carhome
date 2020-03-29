# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CarhomePipeline(object):
    # item是parse方法返回值的元素  是一个字典
    def process_item(self, item, spider):
        with open('car.json', 'a', encoding='utf-8')as fp:
            fp.write(str(item))
        return item

