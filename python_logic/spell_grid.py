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
    level_of_stack = 0

    def number_of_cards(self, stack):
        return len(stack)

    # shuffle function will be in util functions

class SpellGrid:
    # a column of Stacks
    stack = Stack
    column = []
    
