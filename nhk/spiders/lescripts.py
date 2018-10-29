# -*- coding: utf-8 -*-
import scrapy
from nhk.items import ScriptItem

def genStartUrls():
  urls = []
  for i in range(1, 49):
    urls.append('https://www.nhk.or.jp/lesson/chinese/learn/list/' + str(i) +'.html')
  return urls

class LescriptsSpider(scrapy.Spider):
  name = 'lescripts'
  allowed_domains = ['nhk.or.jp']
  start_urls = genStartUrls()
  
  def parse(self, response):
      items = []
      jaItems = response.xpath('//table[@class="tabel-script"]//tr[@class="line-ja"]')
      yomiItems = response.xpath('//table[@class="tabel-script"]/tr[@class="line-yomi"]')
      for idx, ja in enumerate(jaItems):
        item = ScriptItem()
        item['seq'] = idx
        item['ja_1'] = ja.xpath('th/text()')[0].extract()
        item['ja_2'] = ja.xpath('td/text()')[0].extract()
        item['ja_3'] = ja.xpath('td/text()')[1].extract()
        item['yomi_1'] = yomiItems[idx].xpath('th/text()')[0].extract()
        item['yomi_2'] = yomiItems[idx].xpath('td/text()')[0].extract()
        items.append(item)
      yield {
        response.url: items
      }

