# -*- coding: utf-8 -*-
import scrapy
import re
from nhk.items import VocabularyItem, VocabularyItems
from urlcounts import urlcounts

def genStartUrls():
    urls = []
    for i in range(1, 49):
        urls.append('https://www.nhk.or.jp/lesson/chinese/vocabulary/list/{}_01.html'.format(i))
    return urls

class VocabularySpider(scrapy.Spider):
    name = 'vocabulary'
    allowed_domains = ['nhk.or.jp']
    start_urls = genStartUrls() 

    def parse(self, response):
        items = VocabularyItems()
        result = re.findall('\d+_\d+', response.url)[0].split('_')
        items['seq'] = result[0]
        items['items'] = []

        jas = response.xpath('//div[@id="w-box"]/div/h2/text()')
        prons = response.xpath('//div[@id="w-box"]/div/h2/span/text()')
        hanzis = response.xpath('//div[@id="w-box"]/div/p/b/text()')

        item = VocabularyItem()
        item['ja'] = jas[0].extract().strip()
        item['pron'] = prons[0].extract().strip()
        item['hanzi'] = hanzis[0].extract().strip()

        items['items'].append(item)

        urls = []
        for i in range(2, urlcounts[int(result[0])]+1):
            urls.append('https://www.nhk.or.jp/lesson/chinese/vocabulary/list/{}_{:02d}.html'.format(result[0], i))

        url = urls.pop(0)
        request = scrapy.Request(url, callback=self.parseItem, meta={ 'items': items, 'urls': urls })
        yield request

    def parseItem(self, response):
        items = response.meta['items']
        urls = response.meta['urls']

        jas = response.xpath('//div[@id="w-box"]/div/h2/text()')
        prons = response.xpath('//div[@id="w-box"]/div/h2/span/text()')
        hanzis = response.xpath('//div[@id="w-box"]/div/p/b/text()')

        item = VocabularyItem()
        item['ja'] = jas[0].extract().strip()
        item['pron'] = prons[0].extract().strip()
        item['hanzi'] = hanzis[0].extract().strip()

        items['items'].append(item)
        if not urls:
            yield items
        else:
            url = urls.pop(0)
            yield scrapy.Request(url, callback=self.parseItem, meta={ 'items': items, "urls": urls })

