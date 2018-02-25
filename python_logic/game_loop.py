"""
Put the command line came loop in here
"""

import re

from util_functions import UtilFunctions as utils

class GameLoop:
    def __init__(self):
        pass

    def start_game(self):
        print("Enter q to quit")
        command = input("What would you like to do next? \n")
        self.handle_commands(command)

    def handle_commands(self, command):
        # check for what type of card it is.
        view = re.search("view", command)
        if(view is not None):
            print("That's a view!")

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
            print(utils.get_info_by_id(self, command, card_check_type))
        elif(command == "help" or command == "Help" or command == "h"):
            print("Type q to quit \n")
        else:
            print("Command not recognized, please try again")

        while command != "q":
            # self.handle_commands(command)
            command = input("What would you like to do next? \n")
            self.handle_commands(command)
        
        quit()


