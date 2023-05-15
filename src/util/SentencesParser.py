import sys
from os import getcwd
import copy as _
import logging
import sys
sys.path.append("/privacyVoiceAssistant/src")
sys.path.append(getcwd() + "/../")

try:
    from util.Generate import Generate
    Generate.logingConfig(logging)
    from util.SaveAndLoad import SaveAndLoad as util
    from model.enumerations.Entity import Entity
    from model.enumerations.Purpose import Purpose
except Exception as e:
    logging.info(e)

def parse_ini_file(filename):
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

def remove_entity_from_intent(intents:dict, intent:str, entity:Entity):
    entities:dict = intents.get(intent)
    del entities[entity]

def remove_purpose_from_intent(intents:dict, intent_name:str, purpose_name:Purpose):
    if intent_name not in intents:
        raise ValueError(f"Intent '{intent_name}' not found in intents dictionary")

    intent = intents[intent_name]
    for entity in intent:
        if purpose_name in intent[entity]:
            intent[entity].pop(purpose_name)

if __name__ == '__main__':
    intents = parse_ini_file(sys.argv[1])
    if len(sys.argv) > 2:
        util.save_as_json(sys.argv[2], intents)    
    print(intents)