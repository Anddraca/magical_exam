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
            print("# ",  end="")
            # print(word)
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

    def print_spell_card_info(self, card_info):
        # same defaults from above
        self.wrapper.width = 20
        self.wrapper.break_long_words = False

        print("#"*24)
        print("#" + " "*22 + "#")
        wrapped_card_name = self.wrapper.wrap(card_info['name'])
        print(wrapped_card_name)

    def make_rows(self, arr_of_cards):
        rows = {[],[],[],[],[]}


    def build_rows(self, board):
        rows = {}
        cell_width = 24
        title = "#"
        L5 = "#"
        L4 = "#"
        L3 = "#"
        L2 = "#"
        L1 = "#"

        titles = ["DESTRCUTION", "CONSTRUCTION", "SUMMON", "ILLUSION"]
        for cat in titles:
            # title
            add_to_row = ""
            name = cat
            length_of_name = len(name)
            blanks = cell_width - length_of_name
            buff = blanks//2
            add_buff = 0
            if(buff + length_of_name + buff < cell_width):
                add_buff = cell_width - (buff*2 + length_of_name)

            add_to_row = " "*buff + name + " "*(buff + add_buff) + "#"

            title = title + add_to_row

        L5s = ['L5D', 'L5C', 'L5S', 'L5I']
        for cat in L5s:
            add_to_row = ""
            name = board[cat][0]
            length_of_name = len(name)
            blanks = cell_width - length_of_name
            buff = blanks//2
            add_buff = 0
            if(buff + length_of_name + buff < cell_width):
                add_buff = cell_width - (buff*2 + length_of_name)

            add_to_row = " "*buff + name + " "*(buff + add_buff) + "#"

            L5 = L5 + add_to_row
        
        L4s = ['L4D', 'L4C', 'L4S', 'L4I']
        for cat in L4s:
            add_to_row = ""
            name = board[cat][0]
            length_of_name = len(name)
            blanks = cell_width - length_of_name
            buff = blanks//2
            add_buff = 0
            if(buff + length_of_name + buff < cell_width):
                add_buff = cell_width - (buff*2 + length_of_name)

            add_to_row = " "*buff + name + " "*(buff + add_buff) + "#"

            L4 = L4 + add_to_row

        L3s = ['L3D', 'L3C', 'L3S', 'L3I']
        for cat in L3s:
            add_to_row = ""
            name = board[cat][0]
            length_of_name = len(name)
            blanks = cell_width - length_of_name
            buff = blanks//2
            add_buff = 0
            if(buff + length_of_name + buff < cell_width):
                add_buff = cell_width - (buff*2 + length_of_name)

            add_to_row = " "*buff + name + " "*(buff + add_buff) + "#"

            L3 = L3 + add_to_row
        
        L2s = ['L2D', 'L2C', 'L2S', 'L2I']
        for cat in L2s:
            add_to_row = ""
            name = board[cat][0]
            length_of_name = len(name)
            blanks = cell_width - length_of_name
            buff = blanks//2
            add_buff = 0
            if(buff + length_of_name + buff < cell_width):
                add_buff = cell_width - (buff*2 + length_of_name)

            add_to_row = " "*buff + name + " "*(buff + add_buff) + "#"

            L2 = L2 + add_to_row

        L1s = ['L1D', 'L1C', 'L1S', 'L1I']
        for cat in L1s:
            add_to_row = ""
            name = board[cat][0]
            length_of_name = len(name)
            blanks = cell_width - length_of_name
            buff = blanks//2
            add_buff = 0
            if(buff + length_of_name + buff < cell_width):
                add_buff = cell_width - (buff*2 + length_of_name)

            add_to_row = " "*buff + name + " "*(buff + add_buff) + "#"

            L1 = L1 + add_to_row
        
        rows['title'] = title
        rows['L5'] = L5
        rows['L4'] = L4
        rows['L3'] = L3
        rows['L2'] = L2
        rows['L1'] = L1
        return rows

    def print_board(self, board):
        board_width = 101
        cell_width = 24
        print("AVAILABLE BOARD")
        print(board)
        print("#"*board_width)

        all_rows = self.build_rows(board)
        # print(board['L5D'][0])
        print(all_rows['title'])
        print("#"*board_width)
        print(all_rows['L5'])
        print("#"*board_width)
        print(all_rows['L4'])
        print("#"*board_width)
        print(all_rows['L3'])
        print("#"*board_width)
        print(all_rows['L2'])
        print("#"*board_width)
        print(all_rows['L1'])
        print("#"*board_width)

        # for column in board.keys():
        #     # L5's:
        #     L5 = column['L5'][0]
        #     L4 = column['L4'][0]
        #     L3 = column['L3'][0]
        #     L2 = column['L2'][0]

        # build each cell

        # length_of_name = len(name)


        # figure out the length of the cards that are available (pass in a board state)
        # print("#"*board_width)
        # print("#" + " "*cell_width +  "#" + " "*cell_width + "#" + " "*cell_width + "#" + " "*cell_width + "#")
        # print("#"*board_width)
        # print("#" + " "*cell_width +  "#" + " "*cell_width + "#" + " "*cell_width + "#" + " "*cell_width + "#")
        # print("#"*board_width)
        # print("#" + " "*cell_width +  "#" + " "*cell_width + "#" + " "*cell_width + "#" + " "*cell_width + "#")
        # print("#"*board_width)
        # print("#" + " "*cell_width +  "#" + " "*cell_width + "#" + " "*cell_width + "#" + " "*cell_width + "#")
        # print("#"*board_width)
        # print("#" + " "*cell_width +  "#" + " "*cell_width + "#" + " "*cell_width + "#" + " "*cell_width + "#")
