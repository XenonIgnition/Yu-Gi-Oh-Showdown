"""
Author: Femi Adesina
Company: XenonTech

Script that houses all of the global methods used within this project
"""

import numpy, os, json, requests, bs4

# Define global instance for configuration file
config_filename = "config.json"
config_filepath = "../data/config.json"
card_filename = 'https://www.ygohub.com/api/all_cards'
fetch_card_url = 'https://www.ygohub.com/api/card_info?name={}'
raw_card_filename = "../data/cards.pickle"
bs4_parser = 'html.parser'


# Define a method that pings a website and checks if it is successful
def pingSite(website):
    """
    Method that pings a website and determines if it can be accessed
    :param website: URL of website
    :return: T/F
    """
    # Define variable housing url to API
    response = requests.get(website)

    # Code Frag: Ping API to see if it working
    try:
        if not response.status_code == requests.codes.ok:
            print("Cannot access the website due to a bad code. Please fix and try again.")
            return False
        else:
            return True
    except ValueError:
        pass


# Define method that will request and return information using the parameterized name
def fetchCardAPI(name):
    """
    Method that will use the name passed to pull information and return to function caller
    :param name: String of Yu-Gi-Oh card name
    :return: Dictionary of the Yu-Gi-Oh card info
    """
    card_url = fetch_card_url.format(name)

    # Check URL accessibility
    if not pingSite(card_url):
        return "Could not access website"

    # Define variable housing url to API
    card_info_response = requests.get(card_url)

    # Soup object holding json content of all cards fetched by the API
    soup = bs4.BeautifulSoup(card_info_response.content, bs4_parser)

    # Use Soup Object and convert json to a readable python object
    json_soup = json.loads(soup.get_text())

    return json_soup

    # print(json.dumps(json_soup, indent=4, sort_keys=True))


# Define method that will check if the config file exists
def doesConfigExist():
    """
    Method to check if config file exists
    :return: Returns true if it does and creates a new one if it does not
    """
    if os.path.isfile(config_filepath):
        return True
    else:
        createConfigFile()


# Define method that will create the config file if the config file does not exist
def createConfigFile():
    """
    Method that will create the config file
    :return:
    """
    config_settings = {'createdCardList': 'F', 'updateCardRequired': 'F'}

    with open(config_filepath, 'w') as fJson:
        json.dump(config_settings, fJson, sort_keys=True, indent=4, ensure_ascii=False)


def openConfigFile():
    """
    Utility method to open config file
    :return: Returns the data in the config file
    """
    with open(config_filepath, 'r') as fJson:
        loaded_config = json.load(fJson)
    return loaded_config


def changeConfigSetting(setting_name, data):
    """
    Method that will change a setting in the config settings json file
    Does not check if data is OK so make sure that it is
    :param setting_name: Dictionary name of the variable to be changed
    :param data: Value that will be changed to
    :return: returns string showing if process worked
    """
    setting = openConfigFile()
    if setting_name in setting:
        setting[setting_name] = data
        return "Successfully changed setting for {}.".format(setting_name)
    else:
        "Could not find setting name {}.".format(setting_name)


# Define method that will change the value of a particular variable in an external file based on whether cards were downloaded
def hasCardListBeenDownloaded():
    """
    Method that will change a variable within a file based on whether card list has been downloaded
    :return: T/F based on whether card list variable in config list is yes
    """
    with open(config_filepath, 'r') as fJson:
        loaded_config = json.load(fJson)
        if loaded_config['createdCardList'] is 'F':
            return False
        else:
            return True


# Define method that will return a value depending on whether an update of the card list is needed
def hasCardListBeenUpdated():
    """
    Method that will check new cards and determine whether a update to the card list is necessary
    :return: Return true or false based on whether the card list has been modified
    """
    pass
