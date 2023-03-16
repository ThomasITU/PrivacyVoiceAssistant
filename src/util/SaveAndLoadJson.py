import json
import jsonpickle

from model.Profile import Profile

class SaveAndLoadJson():

    def saveAsJson(path:str, data):
        with open(path, 'w') as outfile:
            serialized = jsonpickle.encode(data, outfile)
            json.dump(serialized, outfile)

    def loadFromJson(path:str): 
        with open(path) as json_file:
            data = json.load(json_file)
            decode = jsonpickle.decode(data)
            return decode
        
    def encode(data:Profile) -> str:
        serialize = jsonpickle.encode(data)
        return json.dumps(serialize) 

    def decode(data:str) -> Profile:
        profile:Profile = jsonpickle.decode(data)

        return profile