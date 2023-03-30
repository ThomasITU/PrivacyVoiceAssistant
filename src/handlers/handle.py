#!/usr/bin/env python

import logging
import subprocess
import sys
import json
import uuid
from os import getcwd


sys.path.append(getcwd() + "/../")
from handlers.IntentHandler import IntentHandler
from handlers.PolicyHandler import PolicyHandler
from services.VoiceAuthentication import VoiceAuthentication
from model.Constant import Constant
from util.SaveAndLoad import SaveAndLoad
from util.SentencesParser import parse_ini_file



def save_intent_to_file(intent:str, file_name:str):
    file_name = f"{file_name.removesuffix('.wav')}.json"
    SaveAndLoad.save_as_json(file_name, intent)

def save_voice_file(path = Constant.VOICE_PATH) -> str:
    file_name = str(uuid.uuid4())+".wav"
    process = subprocess.Popen(['curl', '--output', path+file_name, Constant.LAST_VOICE_COMMAND_ENDPOINT], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    return file_name

def get_intent() -> str:
    # get json from stdin and load into python dict
    global dictionary
    dictionary = json.loads(sys.stdin.read())
    intent = dictionary["intent"]["name"]
    return intent

def voice_assistant_speech(text:str):
    speech = dict()
    speech["speech"] = {"text": text}
    print(json.dumps(speech))


def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    
    try:
        logging.info("Start handling intent")
        intent:str = get_intent()
        file_name:str = save_voice_file()
        save_intent_to_file(intent, file_name)
        logging.info("Start voice authentication")
        profile = VoiceAuthentication.find_best_match_above_threshold(voiceSample=file_name,threshold=Constant.PROFILE_AUTHENTICATION_THRESHOLD)
        logging.info("Start policy comparison")
        policy_handler = PolicyHandler(intent_dict=parse_ini_file(Constant.INI_FILE_PATH))
        is_allowed = policy_handler.comparePolicyWithProfile(profile, intent)
        if (is_allowed[0]):
            response = IntentHandler.handle_intent(intent)
            voice_assistant_speech(response)
        else:
            voice_assistant_speech(is_allowed[1])
    except OSError as e:
        logging.error(e)
        voice_assistant_speech(e)

if __name__ == '__main__':
    main()