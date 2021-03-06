# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class TxzpPipeline(object):

    def __init__(self):
        self.f = open("tx_append.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.f.write(content + ",\n")

        return item

    def close_spider(self):
        self.f.close()
