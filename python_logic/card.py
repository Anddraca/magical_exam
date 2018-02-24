# holding the card base model

# get the card data

import json

monsters_parsed = json.load(open('data/monsterCards.json'))
spells_parsed = json.load(open('data/spellCards.json'))
friendlies_parsed = json.load(open('data/friendlyCreatures.json'))

class Card:
    id = ""
    properties = {}

    def getProperties(self, id):
        # get the card data from the json
        if(id.startswith("M")):
            try:
                properties = monsters_parsed[id]
                return properties
            except KeyError:
                print("Not a valid id, please try again")
                return None
        elif(id.startswith("S")):
            try:
                properties = spells_parsed[id]
                return properties
            except KeyError:
                print("Not a valid id, please try again")
                return None
        else:
            try:
                properties = friendlies_parsed[id]
                return properties
            except KeyError:
                print("Not a valid id, please try again")
                return None

