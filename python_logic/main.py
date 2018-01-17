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
        try:
            card_info = monsters_parsed[id]
            return card_info
        except KeyError:
            print("Not a valid ID, please try again")
            return None


class MonsterCard(Card):
    """
    Adds HP and Attack values
    """

    attack = ""
    hp = ""

class playerHand:
    """
    is a list of cards (by id) in the player's hand
    """

    cards_in_hand = []

    def add_to_hand(self, id):
        self.cards_in_hand.append(id)

# test out the thing:

print("Enter q to quit")
command = input("What would you like to do next?")

def handle_commands(command):
    if(command == "M101"):
        print("That is card M101")
    else:
        print("Command not recognized, please try again")

while command != "q":
    handle_commands(command)
    command = input("What would you like to do next?")

# users_id = input("ID of card you want to check out:")

new_card = Card()

# this_card_info = new_card.get_info_by_id(users_id)
formatted_info = ""

#if this_card_info is not None:
 #   formatted_info = "Name: " + this_card_info['name'] + "\nHP: " + this_card_info['hp'] + "\nAttack: " + this_card_info['attack'] + "\nLevel: " + this_card_info['level'] + "\nFlavor Text: " + this_card_info['flavorText'] + "\nText: " + this_card_info['text']
  #  print(formatted_info)
