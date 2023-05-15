import json
import jsonpickle
import pickle
import logging
import sys
sys.path.append("/privacyVoiceAssistant/src")
from util.Generate import Generate
Generate.logingConfig(logging)
from model.Profile import Profile

class SaveAndLoad():

    def save_as_json(path:str, data):
        logging.info("save_as_json")
        with open(path, 'w') as outfile:
            serialized = jsonpickle.encode(data, outfile)
            json.dump(serialized, outfile)

    def load_from_json(path:str): 
        logging.info("load_from_json")
        with open(path) as json_file:
            data = json.load(json_file)
            logging.info(f"data: {data}")
            decode = jsonpickle.decode(data)
            logging.info(f"decode: {decode}")
            if(isinstance(decode, Profile)):
                logging.info("isinstance Profile" )
                decode.voiceSamples = sorted(decode.voiceSamples)
                logging.info(f"decode.voiceSamples: {decode.voiceSamples}")
                decode.policy = sorted(decode.policy)
                logging.info(f"decode.policy: {decode.policy}")
            return decode
        
    def encode(data:Profile) -> bytes:
        serialize = pickle.dumps(data)
        return serialize

    def decode(data:bytes) -> Profile:
        profile:Profile = pickle.loads(data)
        profile.voiceSamples = sorted(profile.voiceSamples)
        profile.policy = sorted(profile.policy)
        return profile