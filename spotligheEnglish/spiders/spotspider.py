import scrapy
import copy
import time
import os
from selenium.webdriver.chrome.options import Options
from spotligheEnglish.items import SpotligheenglishItem


class SpotspiderSpider(scrapy.Spider):
    name = 'spotspider'
    allowed_domains = ['spotlightenglish.com']
    start_urls = ['https://spotlightenglish.com/playlists/']

    def parse(self, response):

        categorys = response.xpath('/html/body/div[1]/div[4]/div/div/div/div/div')

        for category in categorys:
            item = SpotligheenglishItem()
            item['category_name'] = category.xpath('./div/div/div/div/h2/a/text()').extract()[0]
            item['category_url'] = category.xpath('./div/div/div/div/h2/a/@href').extract()[0]
            # print(item)
            # yield item
            yield scrapy.Request(
                url=item['category_url'],
                callback=self.category_parse,
                meta={'item': copy.deepcopy(item)}
            )

    def category_parse(self, response):

        item = response.meta['item']
        articles = response.xpath('/html/body/div[1]/div[3]/div[2]/div/div/div/div')

        for article in articles:

            item['article_url'] = article.xpath(
                './article/div[2]/div/div[1]/h2/a/@href').extract()[0]
            item['article_title'] = article.xpath(
                './article/div[2]/div/div[1]/h2/a/text()').extract()[0]
            item['article_pic'] = article.xpath(
                './article/div[1]/a/img/@src').extract()[0]
            # time.sleep(3)
            # print(item)

            yield scrapy.Request(
                url=item['article_url'],
                callback=self.article_parse,
                meta={'item': copy.deepcopy(item)}
            )

    def article_parse(self, response):

        print('###############################################')
        item = response.meta['item']
        # time.sleep(3)
        # print(response.xpath('//figure[@class="wp-block-audio"]/audio/@src'))


        item['mp3_download_api'] = response.xpath('//figure[@class="wp-block-audio"]/audio/@src').extract()[0]
        # print(item['mp3_download_api'])
        item['youtube_url'] = response.xpath('//iframe[contains(@loading,"lazy")]/@src').extract_first()
        item['text'] = response.xpath('/html/body/div[1]/div[4]/div/div/div/article/div[2]/p/text()').extract()
        text = ''
        for i in item['text']:
            text = text + i

        item['text'] = text

       
        yield item
        # print(item['text'])
