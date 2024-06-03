import scrapy


class TextItem(scrapy.Item):
    text = scrapy.Field()
