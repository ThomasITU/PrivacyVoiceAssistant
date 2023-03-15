import json
import jsonpickle

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
        
