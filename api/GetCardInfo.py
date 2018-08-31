"""
Author: Femi Adesina
Company: XenonTech

Script that will use an api request from yugioh hub to get card info
"""

import urllib3, requests, json
from bs4 import BeautifulSoup

parser = 'html.parser'

# Define a function that will get the card name list from an external file and then load them into a file object variable
# Define a function that will loop through each card name in the list and then send API request to Yu-Gi-Oh Hub that will get the relevant information
# Define a function that will use the collected information to make Yu-Gi-Oh card objects
# Define a function that will...

def getCardFile(filename):
    """
    Function that will get the card list file from memory
    :param filename: File that houses the card list
    :return: List of Yu-Gi-Oh card objects
    """
