import sys
from os import getcwd
import copy as _

sys.path.append(getcwd() + "/../")
from util.SaveAndLoad import SaveAndLoad as util
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



def removePurposeFromIntent(intents:dict, intent_name:str, purpose_name:Purpose):
    if intent_name not in intents:
        raise ValueError(f"Intent '{intent_name}' not found in intents dictionary")

    intent = intents[intent_name]
    for entity in intent:
        if purpose_name in intent[entity]:
            intent[entity].pop(purpose_name)



if __name__ == '__main__':
    intents = parseIniFile(sys.argv[1])
    if len(sys.argv) > 2:
        util.saveAsJson(sys.argv[2], intents)    
    print(intents)