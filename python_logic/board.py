# define the spell board as well as the elements within
import json
from random import shuffle

spells_parsed = json.load(open('data/spellCards.json'))

class SpellBoard:
    def starting_board(self):
        board = {'destruct': {'L1': ['L1D'], 'L2': ['L2D'], 'L3': ['L3D'], 'L4': ['L4D'], 'L5': ['L5D']}, 'construct': {'L1': ['L1C'], 'L2': ['L2C'], 'L3': ['L3C'], 'L4': ['L4C'], 'L5': ['L5C']}, 'summon': {'L1': ['L1S'], 'L2': ['L2S'], 'L3': ['L3S'], 'L4': ['L4S'], 'L5': ['L5S']}, 'illusion': {'L1': ['L1I'], 'L2': ['L2I'], 'L3': ['L3I'], 'L4': ['L4I'], 'L5': ['L5I']}}
        
        return board
    
    # take the top level keys that are in spellCards.json and determine how many columns there should be
    def build_board(self):
        columns = {}
        for cat in spells_parsed.keys():
            columns[cat] = {}
            for level in spells_parsed[cat].keys():
                columns[cat][level] = []
                for spell in spells_parsed[cat][level].keys():
                    columns[cat][level].append(spells_parsed[cat][level][spell]['name'])
                
                shuffle(columns[cat][level])
        
        return columns
