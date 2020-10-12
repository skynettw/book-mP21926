# -*- coding: utf-8 -*-
from pymongo import MongoClient

class MyprojPipeline:

	def __init__(self):
		self.conn = MongoClient()
		self.db = self.conn.quoteDB
		self.collection = self.db.quotes

	def process_item(self, item, spider):
		try:
			self.collection.insert_one(dict(item))
		except:
			pass
		return item
