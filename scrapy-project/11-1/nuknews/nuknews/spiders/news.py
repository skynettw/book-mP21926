# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.nuk.edu.tw']
    start_urls = ['https://www.nuk.edu.tw/p/403-1000-83-1.php?Lang=zh-tw']
    visited_pages = ['https://www.nuk.edu.tw/p/403-1000-83-1.php?Lang=zh-tw']

    def parse(self, response):
        try:
            max_page = int(response.css("#Dyn_2_3 > div > section > div.mpgbar > nav > span::text").extract_first()[1:-1])
        except:
            max_page = 1
        url_pattern = 'https://www.nuk.edu.tw/p/403-1000-83-{}.php?Lang=zh-tw'
        page_urls = [url_pattern.format(i) for i in range(2, max_page+1)]
        for page_url in page_urls:
            if page_url not in self.visited_pages:
                self.visited_pages.append(page_url)
                yield scrapy.Request(page_url, self.parse)

        links = response.css("#pageptlist > table > tbody > tr > td > div > div > a::attr(href)").extract()
        titles = response.css("#pageptlist > table > tbody > tr > td > div > div > a::text").extract()
        titles = [item.strip() for item in titles]
        post_dates = response.css("#pageptlist > table > tbody > tr > td:nth-child(3) > div::text").extract()
        post_dates = [item.strip() for item in post_dates]
        for link, title, post_date in zip(links, titles, post_dates):
            data = dict()
            data['link'] = link
            data['title'] = title
            data['post_date'] = post_date
            yield scrapy.Request(link, meta={"data": data}, callback=self.parse_article)

    def parse_article(self, response):
        data = response.meta["data"]
        res = response.css("#Dyn_2_3 > div.module.module-detail.md_style1 > div > section > div.mcont > div.mpgdetail::text").extract()
        res = [r.strip() for r in res]
        data['content'] = "".join(res)
        return data
