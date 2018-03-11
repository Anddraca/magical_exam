"""
Entry point file. Will call in other elements needed, execute main logic

Author: Tom Anderson

&copy 2018

"""

import json
import re

from game_loop import GameLoop
from printing import PrintThings
from card import Card
from spell_grid import Stack, SpellGridColumn
from board import SpellBoard

# get the card data
monsters_parsed = json.load(open('data/monsterCards.json'))
spells_parsed = json.load(open('data/spellCards.json'))
# print(monsters_parsed)


class MonsterCard(Card):
    """
    Adds HP and Attack values
    """

    attack = ""
    hp = ""

class AvailableCards:
    """
    is a list of cards (by id) in the player's hand
    """

    cards_available = []

    def add_to_available_cards(self, stack_pos):
        #
        pass

    def list_available_cards(self):
        return self.cards_available

class MonsterStack(Stack):
    number_of_defeated = 0


class SpellStack(Stack):
    school = ""

# build monster column
all_monsters = monsters_parsed.keys()
level_one_monsters = []
level_two_monsters = []
level_three_monsters = []
level_four_monsters = []
level_five_monsters = []
for monster in all_monsters:
    if(monster.find("M1") > -1):
        level_one_monsters.append(monster)
    if(monster.find("M2") > -1):
        level_two_monsters.append(monster)
    if(monster.find("M3") > -1):
        level_three_monsters.append(monster)
    if(monster.find("M4") > -1):
        level_four_monsters.append(monster)
    if(monster.find("M5") > -1):
        level_five_monsters.append(monster)

level_one_stack = Stack(level_one_monsters)
level_two_stack = Stack(level_two_monsters)
level_three_stack = Stack(level_three_monsters)
level_four_stack = Stack(level_four_monsters)
level_five_stack = Stack(level_five_monsters)

monster_stacks = [level_one_stack, level_two_stack, level_three_stack, level_four_stack, level_five_stack]

monster_grid = SpellGridColumn(monster_stacks)
# monster_grid.column["R1"].shuffle()

# shuffle 'em
for i in range(5):
    monster_grid.column["R" + str(i+1)].shuffle()


printer = PrintThings()
printer.print_welcome()
spell_board = SpellBoard()
board = spell_board.starting_board()
printer.print_board(board)

# print("Enter q to quit")
# command = input("What would you like to do next? \n")
game = GameLoop()
game.start_game()


# users_id = input("ID of card you want to check out:")

new_card = Card()

# this_card_info = new_card.get_info_by_id(users_id)
formatted_info = ""

#if this_card_info is not None:
 #   formatted_info = "Name: " + this_card_info['name'] + "\nHP: " + this_card_info['hp'] + "\nAttack: " + this_card_info['attack'] + "\nLevel: " + this_card_info['level'] + "\nFlavor Text: " + this_card_info['flavorText'] + "\nText: " + this_card_info['text']
  #  print(formatted_info)
