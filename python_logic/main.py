"""
Entry point file. Will call in other elements needed, execute main logic

Author: Tom Anderson 

&copy 2018

"""

import json
# get the card data
monsters_parsed = json.load(open('data/monsterCards.json'))

# print(monsters_parsed)

# define a generic card class:

class Card:
    """
    Define generic card:

    Type: String - Monster or Spell
    ID: String - the ID of the card
    Name: String - Name of the card
    """

    type = ""
    id = ""
    name = ""

    def get_info_by_id(self, id):
        card_info = monsters_parsed[id]
        return card_info

# test out the thing:

users_id = input("ID of card you want to check out:")

new_card = Card()

this_card_info = new_card.get_info_by_id(users_id)

print(this_card_info)
