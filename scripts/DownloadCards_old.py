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

    name = "yugioh5656"

    def start_requests(self):
        """
        Define initial pages that the crawler will begin to work through
        :return: An iterable of Requests which spider will crawl from.
        """
        card_urls = [
            'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&keyword=&stype=1&ctype=&starfr=&starto=&pscalefr=&pscaleto'
            '=&linkmarkerfr=&linkmarkerto=&link_m=2&atkfr=&atkto=&deffr=&defto=&othercon=2 '
        ]
        for url in card_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Method used to call handle response downloaded for each request made.
        In addition, it will find relevant content based on the method described within the function and use this to identify other urls for Requests.
        :param response: Instance that holds the content of the page and other methods to help crawler.
        """
        filename = 'yugioh_cards.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log("Saved body to file")

        """
        for card in response.css('dl'):
            yield {
                'card-type': card.css('span.box_card_attribute span').extract_first(),
                'card-name': card.css('span.card_status strong').extract_first(),
                'card-link': card.css('')
            }

            next_page = response.css('div.page_num a::attr("href")').extract_first()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
        """
    def createCardFile(self):
        """
        Method that creates a new file for the Yu-Gi-Oh card links downloaded
        :return: Returns a new file
        """
        pass

