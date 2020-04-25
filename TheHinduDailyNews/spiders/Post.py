import scrapy
from TheHinduDailyNews.items import ThehindudailynewsItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
import socket
import datetime



class PostSpider(scrapy.Spider):
    name = "Post"
    allowed_domains = ["thehindu.com"]
    start_urls = ['http://www.thehindu.com/todays-paper/']

    def parse(self, response):
    
        for href in response.xpath('//*[contains(@class, "archive-list")]/li/a/@href').extract():
            yield scrapy.Request((href), callback=self.parse_author)

    def parse_author(self, response):
        Items = ItemLoader(item=ThehindudailynewsItem(), response=response)
        Items.add_value('CATEGORY', "Front_Page")
        Items.add_xpath('TITLE', '/html/body/div[2]/section[1]/section/div/div/div/h1/text()', MapCompose(str.strip, str.title))
        Items.add_xpath('IMAGE', '//div[contains(@class,"img-container picture")]/img/@data-src-template')#, MapCompose(lambda i: urllib.parse.urljoin(response.url, i)))
        Items.add_xpath('SUBHEADING', '/html/body/div[2]/section[1]/section/div/div/div/h2/text()', MapCompose(str.strip, str.title))
        Items.add_xpath('CONTENT', '//div[contains(@id, "content-body")]//p//text()', MapCompose(str.strip), Join())
        Items.add_value('TIME', datetime.datetime.now())
        Items.add_value('URL', response.url)
        return Items.load_item()

        
    def parse_debug(self, response):
        d = ItemLoader(item=ThehindudailynewsItem(), response=response)
        d.add_value('url', response.url)
        d.add_value('project', self.settings.get('BOT_NAME'))
        d.add_value('spider', self.name)
        d.add_value('server', socket.gethostname())
        d.add_value('date', datetime.datetime.now())
