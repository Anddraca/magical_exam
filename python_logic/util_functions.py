"""

some helper functions to be used universally

"""

import json

# get the card data
monsters_parsed = json.load(open('data/monsterCards.json'))
spells_parsed = json.load(open('data/spellCards.json'))


class UtilFunctions:
    # get card info by id:
    def get_info_by_id(self, id, type):
        if(type == "M"):
            try:
                card_info = monsters_parsed[id]
                return card_info
            except KeyError:
                print("Not a valid ID, please try again")
                return None

        if(type == "S"):
            try:
                card_info = spells_parsed[id]
                return card_info
            except KeyError:
                print("Not a valid ID, please try again")
                return None
