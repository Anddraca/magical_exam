from random import shuffle
# define the spell grid that can be used to obtain cards
# the spell grid is a 4 by 5 grid of cards, each of which is a stack of cards
# 
# ==============================================================
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
#
# ==============================================================

class Stack:
    cards_in_stack = []

    def __init__(self, list_of_cards):
            self.cards_in_stack = list_of_cards

    def number_of_cards(self, stack):
        return len(stack)
    
    def get_top_card(self):
        return self.cards_in_stack[0]

    def shuffle(self):
        return shuffle(self.cards_in_stack)

    # shuffle function will be in util functions

class SpellGridColumn:
    # a column of Stacks
    column = {}

    def __init__(self, list_of_stacks):
        counter = 1
        for stack in list_of_stacks:
            self.column["R" + str(counter)] = stack
            counter += 1
