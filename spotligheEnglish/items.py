# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpotligheenglishItem(scrapy.Item):
    # define the fields for your item here like:
    category_url = scrapy.Field()   # 分类目录链接
    category_name = scrapy.Field()  # 分类目录name
    category_dir = scrapy.Field()  # 分类目录文件夹路径
    article_url = scrapy.Field()       # 分类下所有文章链接
    article_title = scrapy.Field()  # 分类下所有文章标题
    article_pic = scrapy.Field()  # 分类下所有文章封面
    article_dir = scrapy.Field()  # 文章文件夹路径
    audio_url = scrapy.Field()       # 文章音频链接
    mp3_download_api = scrapy.Field()   # 文章音频下载链接
    youtube_url = scrapy.Field()      # 文章视频链接
    text = scrapy.Field()  # 文章视频链接



    pass
