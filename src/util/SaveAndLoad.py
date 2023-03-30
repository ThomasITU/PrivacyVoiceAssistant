import json
import jsonpickle
import pickle

from model.Profile import Profile

class SaveAndLoad():

    def save_as_json(path:str, data):
        with open(path, 'w') as outfile:
            serialized = jsonpickle.encode(data, outfile)
            json.dump(serialized, outfile)

    def load_from_json(path:str): 
        with open(path) as json_file:
            data = json.load(json_file)
            decode = jsonpickle.decode(data)
            if(isinstance(decode, Profile)):
                decode.voiceSamples = sorted(decode.voiceSamples)
                decode.policy = sorted(decode.policy)
            return decode
        
    def encode(data:Profile) -> bytes:
        serialize = pickle.dumps(data)
        return serialize

    def decode(data:bytes) -> Profile:
        profile:Profile = pickle.loads(data)
        profile.voiceSamples = sorted(profile.voiceSamples)
        profile.policy = sorted(profile.policy)
        return profile