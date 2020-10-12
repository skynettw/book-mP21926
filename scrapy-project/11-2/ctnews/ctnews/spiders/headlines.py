# -*- coding: utf-8 -*-
import scrapy


class HeadlinesSpider(scrapy.Spider):
    name = 'headlines'
    allowed_domains = ['www.chinatimes.com']
    start_urls = ['https://www.chinatimes.com/politic/total?chdtv']
    visited_pages = list()
    def parse(self, response):
    	res = response.css("section > ul > li > div > div > div.col")
    	for item in res:
    		data = dict()
    		data['link'] = item.css("h3.title a::attr(href)").extract_first()
    		data['title'] = item.css("h3.title a::text").extract_first().strip()
    		data['datetime'] = item.css("div.meta-info time::attr(datetime)").extract_first().strip()
    		data['abstract'] = item.css("p.intro::text").extract_first().strip()
    		yield data
    	next_pages = response.css("section > nav > ul > li > a::attr(href)").extract()
    	for next_page in next_pages:
    		if next_page is not None and next_page not in self.visited_pages :
    			self.visited_pages.append(next_page)
    			yield response.follow(response.urljoin(next_page), callback=self.parse)
