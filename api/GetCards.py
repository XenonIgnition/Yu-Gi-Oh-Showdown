"""
Author: Femi Adesina
Company: XenonTech

Script that will use an api request from yugioh hub to download all the cards
"""

import urllib3, requests, json, pickle
import api.GlobalMethods as glob
from bs4 import BeautifulSoup


class CardManager:
    """
    Class that will manage functions pertaining to the downloading of yugioh card information
    and creation of card objects
    """

    def __init__(self):
        """
        Constructor for Card Manager
        """
        self.cardList = []
        self.cardObjList = []

    #########################################################################
    # PROCESS CARD LOGIC DECLARATIONS
    #########################################################################

    ###############################
    # GET CARD LIST
    ###############################
    def getAllCardList(self):
        """
        Method to get a list of all the card names
        :return: Tuple of card names
        """
        # Define variable housing url to API
        cards_response = requests.get(glob.card_filename)

        # Code Frag: Ping API to see if it working
        try:
            if not cards_response.status_code == requests.codes.ok:
                print("Cannot access the website due to a bad code. Please fix and try again.")
        except ValueError:
            pass

        # Soup object holding json content of all cards fetched by the API
        soup = BeautifulSoup(cards_response.content, glob.bs4_parser)

        # Use Soup Object and convert json to a readable python object
        json_soup = json.loads(soup.get_text())

        # From python object, extract the card names and store them in a object variable
        self.cardList = json_soup['cards']
        # print(self.cardList)

        # Store the card list in a python pickle file for safekeeping
        with open(glob.raw_card_filename, 'wb') as fPickle:
            pickle.dump(self.cardList, fPickle, pickle=pickle.HIGHEST_PROTOCOL)

    ###############################
    # GET CARD INFORMATION
    ###############################
    def getCardInfo(self):
        """
        Method that will do repeated calls to the API in order to fetch information about specified card
        :return: Card Information
        """
        cards = self.cardList
        # Create a loop that will access names in the cardList and send them to the API.
        # Once fetched, the loop with callback the createCardObj using the information pulled to create a card object
        # This will be stored in the card_object object list variable
        for card in cards:
            info = glob.fetchCardAPI(card)
            print


    ###############################
    # CREATE PYTHON CARD OBJECTS
    ###############################
    def createCardObj(self, card_dict):
        """
        Method that will create a card object based on the info provided in dict
        :return: Return card information
        """
        # Change the config settings to say that the card list has been created
        glob.changeConfigSetting('createdCardList', 'T')

    #########################################################################
    # GETTERS/SETTERS
    #########################################################################

    def getCardList(self):
        """
        Getter for card list
        :return: Returns card list variable
        """
        return self.cardList


cards = CardManager()
cards.getAllCardList()
# print(cards.getCardList())
