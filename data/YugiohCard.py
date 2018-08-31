# -*- coding: utf-8 -*-
"""
Company: XenonT
Author: Adesina Bros
Date: 16/07/2018
Script: YugiohCard.py

This module will house the Yugioh Cards information and create an object that will then be used to
store in the database. Each Card will have a type depending on whether the card is a monster, spell
or card. If there are any extraneous cards (Traps that turn into monster cards), then they will be
dealt with using a special formula.

Example:
    Monster
        Name: Cyber Dragon
        Level: 5
        Effect: ...
        Atk: ...
        Def: ...
        Image: ...
        Code: ...
        Packs Obtained From:
        Generation:

Important attributes that will be used in the indexing and game option classes are the:
    Generation: Which Generation is that card counted towards (Will be determined by date of
                        release, pack)
    Pack: Which packs that the card appears in.


To-Do List:
- Card Structure
- Determine Card Type
- Constructor

"""


# Imports

class YuGiOhCard:
    """
    Class that will be used to store the Yu-Gi-Oh cards from DevPro's database
    """

    def __init__(self, type, card_info):
        """
        Constructor for Yu-Gi-Oh Card
        """
        self.type = type
        self.card_info = card_info
        if self.type is 'Monster':
            self.card = self.createMonsterCard()
        elif self.type is 'Spell':
            self.card = self.createSpellCard()
        else:
            self.card = self.createTrapCard()

    def createMonsterCard(self):
        """
        Method that creates a new dictionary containing relevant info of card
        :return: void
        """
        card_dict = {}
        card_dict['name'] = self.card_info['card']['name']
        card_dict['id'] = self.card_info['card']['number']
        card_dict['type'] = self.card_info['card']['type']
        card_dict['mon_type'] = self.card_info['card']['monster_types']
        card_dict['species'] = self.card_info['card']['species']
        card_dict['attr'] = self.card_info['card']['attribute']
        card_dict['level'] = self.card_info['card']['stars']
        card_dict['need_materials'] = self.card_info['card']['has_materials']
        card_dict['need_name'] = self.card_info['card']['has_name_condition']
        card_dict['desc'] = self.card_info['card']['text']
        card_dict['atk'] = self.card_info['card']['attack']
        card_dict['def'] = self.card_info['card']['defense']
        card_dict['desc'] = self.card_info['card']['text']
        card_dict['legality'] = self.card_info['card']['legality']
        card_dict['releases'] = self.card_info['card']['releases']
        card_dict['img'] = self.card_info['card']['image_path']
        card_dict['thumb'] = self.card['card']['thumbnail_path']
        # card_dict['is_extra_deck'] = self.card_info['card']['is_extra_deck']
        # card_dict['is_fusion'] = self.card_info['card']['is_fusion']
        # card_dict['pendulum'] = self.card_info['card']['is_illegal']
        # card_dict['is_link'] = self.card_info['card']['is_link']

        return card_dict

    def createSpellCard(self):
        """
        Method that creates a new dictionary containing relevant info of card
        :return: void
        """
        card_dict = {}
        card_dict['name'] = self.card_info['card']['name']
        card_dict['id'] = self.card_info['card']['number']
        card_dict['type'] = self.card_info['card']['type']
        card_dict['mon_type'] = self.card_info['card']['monster_types']
        card_dict['species'] = self.card_info['card']['species']
        card_dict['attr'] = self.card_info['card']['attribute']
        card_dict['level'] = self.card_info['card']['stars']
        card_dict['need_materials'] = self.card_info['card']['has_materials']
        card_dict['need_name'] = self.card_info['card']['has_name_condition']
        card_dict['desc'] = self.card_info['card']['text']
        card_dict['atk'] = self.card_info['card']['attack']
        card_dict['def'] = self.card_info['card']['defense']
        card_dict['desc'] = self.card_info['card']['text']
        card_dict['legality'] = self.card_info['card']['legality']
        card_dict['releases'] = self.card_info['card']['releases']
        card_dict['img'] = self.card_info['card']['image_path']
        card_dict['thumb'] = self.card['card']['thumbnail_path']
        # card_dict['is_extra_deck'] = self.card_info['card']['is_extra_deck']
        # card_dict['is_fusion'] = self.card_info['card']['is_fusion']
        # card_dict['pendulum'] = self.card_info['card']['is_illegal']
        # card_dict['is_link'] = self.card_info['card']['is_link']

        return card_dict

    def createTrapCard(self):
        """
        Method that creates a new dictionary containing relevant info of card
        :return: void
        """
        card_dict = {}
        card_dict['name'] = self.card_info['card']['name']
        card_dict['id'] = self.card_info['card']['number']
        card_dict['type'] = self.card_info['card']['type']
        card_dict['mon_type'] = self.card_info['card']['monster_types']
        card_dict['species'] = self.card_info['card']['species']
        card_dict['attr'] = self.card_info['card']['attribute']
        card_dict['level'] = self.card_info['card']['stars']
        card_dict['need_materials'] = self.card_info['card']['has_materials']
        card_dict['need_name'] = self.card_info['card']['has_name_condition']
        card_dict['desc'] = self.card_info['card']['text']
        card_dict['atk'] = self.card_info['card']['attack']
        card_dict['def'] = self.card_info['card']['defense']
        card_dict['desc'] = self.card_info['card']['text']
        card_dict['legality'] = self.card_info['card']['legality']
        card_dict['releases'] = self.card_info['card']['releases']
        card_dict['img'] = self.card_info['card']['image_path']
        card_dict['thumb'] = self.card['card']['thumbnail_path']
        # card_dict['is_extra_deck'] = self.card_info['card']['is_extra_deck']
        # card_dict['is_fusion'] = self.card_info['card']['is_fusion']
        # card_dict['pendulum'] = self.card_info['card']['is_illegal']
        # card_dict['is_link'] = self.card_info['card']['is_link']

        return card_dict
