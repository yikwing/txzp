# -*- coding: utf-8 -*-

# next_page

import scrapy

from txzp.items import TxzpItem


class TxSpider(scrapy.Spider):
    name = 'tx_next'
    allowed_domains = ['tencent.com']

    baseUrl = "http://hr.tencent.com/position.php?start="
    offset = 0

    start_urls = [baseUrl + str(offset)]

    def parse(self, response):
        item = TxzpItem()

        nodeItems = response.xpath("//tr[@class= 'even'] | //tr[@class= 'odd']")

        for node in nodeItems:
            name = node.xpath("./td[1]/a/text()").extract()[0]
            link = "hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract()[0]
            # type = node.xpath("./td[2]/text()").extract()[0]

            if len(node.xpath("./td[2]/text()")) > 0:
                type = node.xpath("./td[2]/text()").extract()[0]
            else:
                type = ""

            num = node.xpath("./td[3]/text()").extract()[0]
            address = node.xpath("./td[4]/text()").extract()[0]
            time = node.xpath("./td[5]/text()").extract()[0]

            item["positionName"] = name
            item["positionLink"] = link
            item["positionType"] = type
            item["positionNum"] = num
            item["positionAddress"] = address
            item["positionTime"] = time

            yield item

        if not len(response.xpath("//a[@class = 'noactive' and @id = 'next']")):
            nextUrl = "http://hr.tencent.com/" + response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request(nextUrl, callback=self.parse)
