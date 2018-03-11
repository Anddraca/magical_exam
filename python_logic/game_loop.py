"""
Put the command line came loop in here
"""

import re

from util_functions import UtilFunctions
from printing import PrintThings
from board import SpellBoard

class GameLoop:
    utils = UtilFunctions()
    printer = PrintThings()

    def __init__(self):
        spell_board = SpellBoard()
        self.start_board = spell_board.starting_board()
        self.board = spell_board.build_board()

    def start_game(self):
        print("Enter q to quit")
        command = input("What would you like to do next? \n")
        self.handle_commands(command)

    def handle_commands(self, command):
        # check for what type of card it is.
        view = re.search("view", command)
        board = re.search("board", command)

        if(view):
            # strip off "view"
            id = command[5:]
            card_info = self.utils.get_info_by_id(id)
            self.printer.print_monster_card_info(card_info)
        elif(board):
            self.printer.print_board(self.board)
        elif(command == "help" or command == "Help" or command == "h"):
            print("Type q to quit \n")
        else:
            print("Command not recognized, please try again")

        while command != "q":
            # self.handle_commands(command)
            command = input("What would you like to do next? \n")
            self.handle_commands(command)
        
        quit()


