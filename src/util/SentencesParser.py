import sys
from os import getcwd
import copy as _

sys.path.append(getcwd() + "/../")
from util.SaveAndLoadJson import SaveAndLoadJson as util
from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose


def parseIniFile(filename):
    purpose = {}
    for p in Purpose:
        purpose[p] = True
    entities = {}
    for e in Entity:
        entities[e] = _.deepcopy(purpose)
    intents = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                intent = line[1:-1]
                intents[intent] = _.deepcopy(entities)
    return intents


    # removeEntityFromIntent(intents, "LongSentence", Entity.ALEXA)
def removeEntityFromIntent(intents:dict, intent:str, entity:Entity):
    entities:dict = intents.get(intent)
    del entities[entity]

   # removePurposeFromIntent(intents, "LongSentence", Purpose.CALENDAR)
def removePurposeFromIntent(intents:dict, intent:str, purpose:Purpose):
    entities:dict = intents.get(intent)
    print(entities)
    for entity in entities:
        keys = entity.items()
        for key in keys:
            if (entity[key]== purpose):
                del entity[key]
        
        


if __name__ == '__main__':
    intents = parseIniFile(sys.argv[1])
    # removeEntityFromIntent(intents, "LongSentence", Entity.ALEXA)
    # print(intents)
    # print("hello")
    removePurposeFromIntent(intents, "LongSentence", Purpose.CALENDER)
    print(intents)
    util.saveAsJson(sys.argv[2], intents)    