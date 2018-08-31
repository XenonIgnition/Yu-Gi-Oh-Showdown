"""
Company: XenonT
Author: Adesina Bros
Date: 16/07/2018
Script: Rulesets.py


This module will house all the information pertaining to all the formats that will be available
for Yu-Gi-Oh Showdown.
"""

import numpy


class Rulesets:
    """
    Class that handles the rules for each of the card effects that a card may require
    """

    def __init__(self, gen, effect, index):
        """
        Constructor for ruleset class
        """
        self.gen = gen
        self.effect = effect
        self.index = index

    def __str__(self):
        """
        String representation
        :return: String rep of Rulesets class
        """

    def effect_rules(self):
        """
        Rules method to handle what happens when an effect occurs
        :return: Returns appropriate handler for the effect
        """

    def search_deck(self):
        """
        Rules method to handle what happens when an effect requiring a search in the deck is necessary
        Processes the deck using the index to generate a list of cards that can be acquired
        :return: Return search list
        """
        pass

    def search_graveyard(self):
        """
        Rules method to handle what happens when an effect requiring a search in the graveyard is necessary
        Processes the graveyard list using the index to generate a new list of cards that can be acquired
        :return: Return search list
        """
        pass

    def search_banish(self):
        """
        Rules method to handle what happens when an effect requiring a search in the banish zone is necessary
        Processes the banish list using the index to generate a new list of cards that can be acquired
        :return: Return search list
        """
        pass

    def search_extra(self):
        """
        Rules method to handle what happens when an effect requiring a search in the extra deck zone is necessary
        Processes the extra deck list using the index to generate a new list of cards that can be acquired
        :return: Return search list
        """
        pass

    def view_graveyard(self):
        """
        Rules method to handle what happens when the user wants to view the contents of the graveyard
        Processes graveyard list and and generates list of all cards in graveyard
        :return: Return view list
        """
        pass

    def view_banish(self):
        """
        Rules method to handle what happens when the user wants to view the contents of the banish zone
        Processes banish list and and generates list of all cards in graveyard
        :return: Return view list
        """
        pass

    def view_extra(self):
        """
        Rules method to handle what happens when the user wants to view the contents of the extra deck
        Processes extra list and and generates list of all cards in extra deck zone
        :return: Return view list
        """
        pass
