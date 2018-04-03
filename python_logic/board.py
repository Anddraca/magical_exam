# define the spell board as well as the elements within
import json
# from random import shuffle

spells_parsed = json.load(open('data/spellCards.json'))

########################################
# the board should just be flat. just make it with the coords and the
# arrays that correspond
# "L1D": [spell1, spell2, spell3]
# print what's on topi
# available is is [0]
# user is all blank to start out
#
# get rid of the overly nested situation that's present in starting_board()

########################################


class SpellBoard:
    def starting_board(self):
        board = {'L1D': ['L1D'], 'L2D': ['L2D'], 'L3D': ['L3D'],
                              'L4D': ['L4D'], 'L5D': ['L5D'],
                'L1C': ['L1C'], 'L2C': ['L2C'], 'L3C': ['L3C'],
                               'L4C': ['L4C'], 'L5C': ['L5C'],
                'L1S': ['L1S'], 'L2S': ['L2S'], 'L3S': ['L3S'],
                            'L4S': ['L4S'], 'L5S': ['L5S'],
                'L1I': ['L1I'], 'L2I': ['L2I'],
                              'L3I': ['L3I'], 'L4I': ['L4I'], 'L5I': ['L5I']}

        return board

    # take the top level keys that are in spellCards.json and determine how
    # many columns there should be
    # def build_board(self):
      #  columns = {}
      #  for cat in spells_parsed.keys():
      #      columns[cat] = {}
      #      for level in spells_parsed[cat].keys():
      #          columns[cat][level] = []
      #          for spell in spells_parsed[cat][level].keys():
      #              columns[cat][level].append(spells_parsed[cat][level]
      # [spell]['name'])
      #
      #          shuffle(columns[cat][level])
      #
      #  return columns
    def build_board(self):
        board =  {"L5D": [], "L4D": [], "L3D": [], "L2D": [], "L1D": [],
                  "L5C": [], "L4C": [], "L3C": [], "L2C": [], "L1C": [],
                  "L5S": [], "L4S": [], "L3S": [], "L2S": [], "L1S": [],
                  "L5I": [], "L4I": [], "L3I": [], "L2I": [], "L1I": []}

        for cat in spells_parsed.keys():
            if(cat != 'name_map'):
                first_letter = cat[0].upper()
                for level in spells_parsed[cat].keys():
                    entry = level + first_letter
                    for spell in spells_parsed[cat][level].keys():
                        board[entry].append(spells_parsed[cat][level][spell]
                                        ['name'])

        return board

    # will represent what is available in the board
    def user_board(self):
        # user_board is what the user currently has access to. starts out with
        # empties for every level

        user_board = {"L5D": "", "L4D": "", "L3D": "", "L2D": "", "L1D": "",
                      "L5C": "", "L4C": "", "L3C": "", "L2C": "", "L1C": "",
                      "L5S": "", "L4S": "", "L3S": "", "L2S": "", "L1S": "",
                      "L5I": "", "L4I": "", "L3I": "", "L2I": "", "L1I": ""}

        return user_board

    def available_board(self, board):
        # what is available to the user to select
        available_board = {}

        # counter = 1
        # for level in board['destruct']:
        #    available_board['L' + str(counter) + "D"] = board['destruct']
        # [level][0]
        #    counter += 1

        # counter = 1
        # for level in board['construct']:
        #    available_board['L' + str(counter) + 'C'] = board['construct']
        # [level][0]
        #    counter += 1

        # counter = 1
        # for level in board['summon']:
        #    available_board['L' + str(counter) + 'S'] = board['summon']
        # [level][0]
        #    counter += 1

        # counter = 1
        # for level in board['illusion']:
        #    available_board['L' + str(counter) + 'I'] = board['illusion']
        # [level][0]
        #    counter += 1

        for key in board.keys():
            available_board[key] = board[key][0]

        return available_board
