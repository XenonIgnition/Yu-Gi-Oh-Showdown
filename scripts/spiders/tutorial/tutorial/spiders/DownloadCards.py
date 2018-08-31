"""
Company: XenonT
Author: Adesina Bros
Date: 16/07/2018
Script: YugiohCard.py


This module will create a web crawler that will get the information necessary for all the Yu-Gi-Oh
cards from a database.
"""

# Imports

import scrapy

# Website Prefix
web_prefix = 'https://www.db.yugioh-card.com/'


class CardSpider(scrapy.Spider):
    """
    Crawler that will download the Yu-Gi-Oh cards
    """

    name = "yugioh"
    cards = []
    count = 0

    def start_requests(self):
        """
        Define initial pages that the crawler will begin to work through
        :return: An iterable of Requests which spider will crawl from.
        """
        card_urls = [
            'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&keyword=&stype=1&ctype=&starfr=&starto=&pscalefr=&pscaleto=&linkmarkerfr=&linkmarkerto=&link_m=2&atkfr=&atkto=&deffr=&defto=&othercon=2'
        ]
        for url in card_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Method used to call handle response downloaded for each request made.
        In addition, it will find relevant content based on the method described within the function and use this to identify other urls for Requests.
        :param response: Instance that holds the content of the page and other methods to help crawler.
        """
        self.count = self.count + 1
        filename = 'yugioh_cards.html'

        self.log("Saved links to to file")

        card_dets = {}

        self.log("Printing Current Card Details")

        LIST_SELECTOR = 'li'
        NAME_SELECTOR = 'strong::text'
        IF_SELECTOR = './/dl'
        LINK_SELECTOR = ''

        for card in response.css(LIST_SELECTOR):
            self.log("Card: {} ".format(len(card.xpath(IF_SELECTOR))))
            if len(card.xpath(IF_SELECTOR)) is not 0:
                yield {
                    'card-name': card.css(NAME_SELECTOR).extract_first(),
                    'card-link': card.css('input.link_value').xpath('@value').extract_first(),
                }

        page_num = response.xpath('//a[contains(text(), "»")]/@href').re(r'\d+')
        next_page = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=3&page={}'.format(page_num[0])
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

        """for card in response.css('dl'):
            yield {
                
            }

            card_dets['name'] = card.css('span.card_status strong::text').extract_first()
            card_dets['link'] = card.css('input.link_value').xpath('@value').extract_first()

            self.log("Printing Current Card Details")
            self.log(card_dets)

            page_num = response.xpath('//a[contains(text(), "»")]/@href').re(r'\d')
            next_page = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=3&page={}'.format(page_num)
            # next_page = response.css('div.page_num a::attr("href")').extract_first()
            if next_page is not None:
                yield response.follow(next_page, self.parse)"""
