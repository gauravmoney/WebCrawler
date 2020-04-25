import scrapy
from scrapy.item import Item, Field


class ThehindudailynewsItem(scrapy.Item):
    
    LINK = Field()
    TITLE = Field()
    SUBHEADING = Field()
    CONTENT = Field()
    CATEGORY = Field()
    IMAGE = Field()
    URL = Field()
    project = Field()
    spider = Field()
    server = Field()
    TIME = Field()
