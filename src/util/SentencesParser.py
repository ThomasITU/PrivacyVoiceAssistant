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
    intent:dict = intents.get(intent)
    del intent[entity]
   
def removePurposeFromIntent(intents:dict, intent:str, purpose:Purpose):
    entities:dict = intents.get(intent)
    for entity, purposes in entities:
        return
        


if __name__ == '__main__':
    intents = parseIniFile(sys.argv[1])
    # removeEntityFromIntent(intents, "LongSentence", Entity.ALEXA)
    # print(intents)
    # print("hello")
    util.saveAsJson(sys.argv[2], intents)    