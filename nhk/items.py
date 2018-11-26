# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScriptItem(scrapy.Item):
  seq = scrapy.Field()
  ja_1 = scrapy.Field()
  ja_2 = scrapy.Field()
  ja_3 = scrapy.Field()
  yomi_1 = scrapy.Field()
  yomi_2 = scrapy.Field()

class VocabularyItem(scrapy.Item):
  ja = scrapy.Field()
  pron = scrapy.Field()
  hanzi = scrapy.Field()
  
class VocabularyItems(scrapy.Item):
  seq = scrapy.Field()
  items = scrapy.Field()
  
