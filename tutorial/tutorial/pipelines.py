# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
import sets

class TutorialPipeline(object):
	def __init__(self):
		self.file = open('item.json', 'wb')
		self.container = sets.Set()

	def process_item(self, item, spider):
		if item['article'] in self.container:
			raise DropItem('existed!')
		line = json.dumps(dict(item)) + "\n"
		self.file.write(line)
		self.container.add(item['article'])
		return item
