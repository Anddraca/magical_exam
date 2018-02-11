"""
Entry point file. Will call in other elements needed, execute main logic

Author: Tom Anderson

&copy 2018

"""

import json
import re

import game_loop
from printing import PrintThings
from card import Card

# get the card data
monsters_parsed = json.load(open('data/monsterCards.json'))
spells_parsed = json.load(open('data/spellCards.json'))
# print(monsters_parsed)

# define a generic card class:

# class Card:
#    """
 #   Define generic card:

  #  Type: String - Monster or Spell
   # ID: String - the ID of the card
   # Name: String - Name of the card
   # """

  #  type = ""
   # id = ""
   # name = ""

   # def get_info_by_id(self, id):
    #    try:
     #       card_info = monsters_parsed[id]
      #      return card_info
      #  except KeyError:
       #     print("Not a valid ID, please try again")
        #    return None


def get_info_by_id(id, type):
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

class Stack:
    cards_in_stack = []
    level_of_stack = 0
    
    def number_of_cards(self, stack):
        return len(stack)

    # shuffle function will be in util functions

class MonsterStack(Stack):
    number_of_defeated = 0


class SpellStack(Stack):
    school = ""

# test card class:
someCard = Card
someCard.getProperties("M101")
print(someCard.properties)

# test out the thing:
PrintThings.printWelcome()
print("Enter q to quit")
command = input("What would you like to do next? \n")

def handle_commands(command):
    # check for what type of card it is.
    # if M###, it's a monster card:
    m = re.search("M\d\d\d", command)
    card_check_type = ""

    if(m is not None):
        card_check_type = "M"

    # if S###, it's a spell card:
    s = re.search("S\d\d\d", command)
    if(s is not None):
        card_check_type = "S"
   
    if(card_check_type is not ""):
        print(get_info_by_id(command, card_check_type))
    elif(command == "help" or command == "Help" or command == "h"):
        print("Type q to quit \n")
    else:
        print("Command not recognized, please try again")

while command != "q":
    handle_commands(command)
    command = input("What would you like to do next? \n")

# users_id = input("ID of card you want to check out:")

new_card = Card()

# this_card_info = new_card.get_info_by_id(users_id)
formatted_info = ""

#if this_card_info is not None:
 #   formatted_info = "Name: " + this_card_info['name'] + "\nHP: " + this_card_info['hp'] + "\nAttack: " + this_card_info['attack'] + "\nLevel: " + this_card_info['level'] + "\nFlavor Text: " + this_card_info['flavorText'] + "\nText: " + this_card_info['text']
  #  print(formatted_info)
