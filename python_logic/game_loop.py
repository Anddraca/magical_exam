"""
Put the command line came loop in here
"""

import re

import util_functions

class game_loop:
    def start_game():
        print("Enter q to quit")
        command = input("What would you like to do next? \n")

    def handle_commands(command):
        """
        The available commands include:
            view [stuff]
                stuff can be card_id, board, monsters, monster deck, status
                (status is for state of the game: player life, etc)
            play [spell]
                name of spell to play

        """
        # check if it's a card search
        # check what kind of card it is

        # if M###, it's a monster card:
        m = re.search("M\d\d\d", command)
        card_check_type = ""

        if(m is not None):
            card_check_type = "M"

        # If S###, it's a spell card:
        s = re.search("S\d\d\d", command)
        if(s is not None):
            card_check_type = "S"

       # if(card_check_type is not ""):
        #    print(get_info_by_id



