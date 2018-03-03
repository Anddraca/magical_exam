# will hold functions for printing the state of things based on the player's commands

# print out a welcome screen
import textwrap
from colors import Colors as fmt

class PrintThings:
    def __init__(self):
        self.wrapper = textwrap.TextWrapper()

    def print_welcome(self):
        print("#"*30)
        print("\n")
        print(" "*5 + fmt.BOLD + fmt.BLUE + "Welcome to Card Game!" + fmt.END)
        print("\n")
        print("#"*30)

    # print a card info for 'view'
    def print_monster_card_info(self, card_info):
        # set defaults for the dimensions for wrapping for this type of card
        self.wrapper.width = 20
        self.wrapper.break_long_words = False

        print("#"*24)
        print("#" + " "*22 + "#")
        wrapped_card_name = self.wrapper.wrap(card_info['name'])
        for word in wrapped_card_name:
            print("# ", end="")
            if(len(word) < self.wrapper.width):
                dif = self.wrapper.width - len(word)
                print(word, end="")
                for i in range(dif):
                    print(" ", end="")
                print(" #")
            else:
                print(word + " #")
        # print("# " + card_info['name'])
        print("#" + " "*22 + "#")
        wrapped_card_text = self.wrapper.wrap(card_info['text'])
        for word in wrapped_card_text:
            print("# ", end="")
            if(len(word) < self.wrapper.width):
                dif = self.wrapper.width - len(word)
                print(word, end="")
                for i in range(dif):
                    print(" ", end="")
                print(" #")
            else:
                print(word + " #")
        # print("# " + card_info['text'])
        print("#" + " "*22 + "#")
        print("#" + " "*4 + card_info['attack'] + " "*12 + card_info['hp'] + " "*4 + "#")
        print("#"*24)
        print("\n")