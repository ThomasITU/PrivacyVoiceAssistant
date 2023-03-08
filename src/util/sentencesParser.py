import sys
from os import getcwd

sys.path.append(getcwd() + "/../")
from util.SaveAndLoadJson import SaveAndLoadJson as util
print(sys.path)
from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose


def parse_ini_file(filename):
    purpose = {}
    for p in Purpose:
        purpose[p] = True
    entities = {}
    for e in Entity:
        entities[e] = purpose
    intents = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                intent = line[1:-1]
                intents[intent] = entities
    return intents


if __name__ == '__main__':
    intents = parse_ini_file(sys.argv[1])
    util.saveAsJson(sys.argv[2], intents)    
    load = util.loadFromJson(sys.argv[2]) 
    print(load)