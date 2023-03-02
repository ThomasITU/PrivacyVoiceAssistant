import json
from os import getcwd
import jsonpickle
from model.PrivacyPolicy import PrivacyPolicy


class Profile:

    def __init__(self, name:str, policy:list[PrivacyPolicy], voiceSamples:list[str]):
        self.name = name
        self.policy = policy
        self.voiceSamples = voiceSamples

def saveAsJson(path:str, profile:Profile):
    with open(path+".json", 'w') as outfile:
        serialized = jsonpickle.encode(profile, outfile)
        json.dump(serialized, outfile)

def loadFromJson(path:str) -> Profile: 
    with open(path) as json_file:
        data = json.load(json_file)
        decode = jsonpickle.decode(data)

        return decode


