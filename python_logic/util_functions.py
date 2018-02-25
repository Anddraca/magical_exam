"""

some helper functions to be used universally

"""

import json
import re

# get the card data
monsters_parsed = json.load(open('data/monsterCards.json'))
spells_parsed = json.load(open('data/spellCards.json'))


class UtilFunctions:
    # get card info by id:
    def get_info_by_id(self, id):
        if(re.search("M\d\d\d", id)):
            if(id in monsters_parsed["L1"]):
                return monsters_parsed["L1"][id]
            elif(id in monsters_parsed["L2"]):
                return monsters_parsed["L2"][id]
            elif(id in monsters_parsed["L3"]):
                return monsters_parsed["L3"][id]
            elif(id in monsters_parsed["L4"]):
                return monsters_parsed["L4"][id]
            elif(id in monsters_parsed["L5"]):
                return monsters_parsed["L5"][id]
        elif(re.search("L\d[D,S,C,I]\d", id)):
            if(id in spells_parsed["destruct"]["L1"]):
                return spells_parsed["destruct"]["L1"][id]
            elif(id in spells_parsed["desctruct"]["L2"]):
                return spells_parsed["destruct"]["L2"][id]
            elif(id in spells_parsed["desctruct"]["L3"]):
                return spells_parsed["destruct"]["L3"][id]
            elif(id in spells_parsed["desctruct"]["L4"]):
                return spells_parsed["destruct"]["L4"][id]
            elif(id in spells_parsed["desctruct"]["L5"]):
                return spells_parsed["destruct"]["L5"][id]
            elif(id in spells_parsed["construct"]["L1"]):
                return spells_parsed["construct"]["L1"][id]
            elif(id in spells_parsed["construct"]["L2"]):
                return spells_parsed["construct"]["L2"][id]
            elif(id in spells_parsed["construct"]["L3"]):
                return spells_parsed["construct"]["L3"][id]
            elif(id in spells_parsed["construct"]["L4"]):
                return spells_parsed["construct"]["L4"][id]
            elif(id in spells_parsed["construct"]["L5"]):
                return spells_parsed["construct"]["L5"][id]
            elif(id in spells_parsed["summon"]["L1"]):
                return spells_parsed["summon"]["L1"][id]
            elif(id in spells_parsed["summon"]["L2"]):
                return spells_parsed["summon"]["L2"][id]
            elif(id in spells_parsed["summon"]["L3"]):
                return spells_parsed["summon"]["L3"][id]
            elif(id in spells_parsed["summon"]["L4"]):
                return spells_parsed["summon"]["L4"][id]
            elif(id in spells_parsed["summon"]["L5"]):
                return spells_parsed["summon"]["L5"][id]
            elif(id in spells_parsed["illusion"]["L1"]):
                return spells_parsed["illusion"]["L1"][id]
            elif(id in spells_parsed["illusion"]["L2"]):
                return spells_parsed["illusion"]["L2"][id]
            elif(id in spells_parsed["illusion"]["L3"]):
                return spells_parsed["illusion"]["L3"][id]
            elif(id in spells_parsed["illusion"]["L4"]):
                return spells_parsed["illusion"]["L4"][id]
            elif(id in spells_parsed["illusion"]["L5"]):
                return spells_parsed["illusion"]["L5"][id]
        else:
            return "ID not found, please try again"
