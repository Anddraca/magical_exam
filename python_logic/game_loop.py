"""
Put the command line came loop in here
"""

import re

from util_functions import UtilFunctions
from printing import PrintThings
from board import SpellBoard
from update_state import UpdateState

class GameLoop:
    utils = UtilFunctions()
    printer = PrintThings()
    update_state = UpdateState()

    def __init__(self):
        spell_board = SpellBoard()
        self.start_board = spell_board.starting_board()
        self.board = spell_board.build_board()
        # self.available_board = spell_board.available_board(self.start_board)
        self.available_board = self.start_board
        self.user_board = spell_board.user_board()

    def start_game(self):
        print("Enter q to quit")
        command = input("What would you like to do next? \n")
        self.handle_commands(command)

    def handle_commands(self, command):
        # check for what type of card it is.
        view = re.search("view", command)
        board = re.search("board", command)
        pick = re.search("pick", command)
        remove_card = re.search('remove', command)

        if(view):
            # strip off "view"
            id = command[5:]
            card_info = self.utils.get_info_by_id(id)
            self.printer.print_monster_card_info(card_info)
        elif(board):
            self.printer.print_board(self.available_board)
        elif(pick):
            position = command[5:]
            new_board = self.update_state.process_pick(position, self.available_board, self.board)
            print(new_board)
        elif(remove_card):
            position = command[7:]
            self.update_state.remove_top_card(position, self.available_board)
        elif(command == "help" or command == "Help" or command == "h"):
            print("'board' shows the current available spell board")
            print("'view' shows a specific card")
            print("'pick [id]' picks a spot by ID")
            print("'remove [id]' remove the top card of that column")
            print("q to quit \n")
        elif(command == 'q'):
            pass
        else:
            print("Command not recognized, please try again")

        while command != "q":
            # self.handle_commands(command)
            command = input("What would you like to do next? \n")
            self.handle_commands(command)
        
        quit()


