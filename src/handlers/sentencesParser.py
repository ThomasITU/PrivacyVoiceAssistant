import json
import sys, configparser
sys.path.append("/home/freyja/BscProject/PrivacyVoiceAssistant/src")
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


def write_ini_file(filename, entities):
    config = configparser.ConfigParser()
    for intent, entity in entities:
        section_name = f"[{intent}]"
        config[section_name] = {}
        for key, value in entity:
            purpose_name = value[1].name
            config[section_name][key] = purpose_name.lower()
    with open(filename, 'w') as f:
        config.write(f)

def saveIntentToFile(intent:str):
    f = open("/tmp/lastIntent.txt", "w")
    f.write(intent + "\n")
    f.close()

def saveAsJson(path:str, ):
    with open(path+".json", 'w') as outfile:
        serialized = jsonpickle.encode(profile, outfile)
        json.dump(serialized, outfile)

def loadFromJson(path:str) -> Profile: 
    with open(path) as json_file:
        data = json.load(json_file)
        decode = jsonpickle.decode(data)

        return decode


if __name__ == '__main__':
    intents = parse_ini_file(sys.argv[1])
    print(json.dumps(intents))
    write_ini_file(sys.argv[2]+".ini", intents)