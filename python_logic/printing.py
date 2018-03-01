# will hold functions for printing the state of things based on the player's commands

# print out a welcome screen

class PrintThings:
    def print_welcome(self):
        for i in range(20):
            print("#", end="")
        print("\n")
        for i in range(6):
            print(" ", end="")
        print("Welcome!\n")
        for i in range(20):
            print("#", end="")
        print("\n")

    # print a card info for 'view'
    def print_card_info(self, card_info):
        for i in range(len(card_info['text'])):
            print("#", end="")
        print("\n#")
        print("# " + card_info['name'])
        print("#")
        print("# " + card_info['text'])
        print("#")
        print("# " + card_info['attack'] + "      " + card_info['hp'])
        for i in range(len(card_info['text'])):
            print("#", end='')
        print("\n")
