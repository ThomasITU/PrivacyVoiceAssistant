#!/usr/bin/env python3.10

import subprocess
import json
import uuid

import logging
import sys
sys.path.append("/privacyVoiceAssistant/src")
try:
    from util.Generate import Generate
    Generate.logingConfig(logging)
    from handlers.IntentHandler import IntentHandler
    from handlers.PolicyHandler import PolicyHandler
    from services.VoiceAuthentication import VoiceAuthentication
    from model.Constant import Constant
    from util.SaveAndLoad import SaveAndLoad
    from util.SentencesParser import parse_ini_file
except Exception as e:
    process = subprocess.Popen(['python', '-V'],
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    logging.info(process.stdout.read())
    logging.info(e)


def save_intent_to_file(intent:str, file_name:str):
    file_name = f"{file_name.removesuffix('.wav')}.json"
    file_name = file_name.removeprefix(Constant.VOICE_PATH)
    SaveAndLoad.save_as_json(Constant.INTENT_PATH+file_name, intent)

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
    logging.info("Start voice assistant speech")
    speech = dict()
    speech["speech"] = {"text": text}
    print(json.dumps(speech))
    logging.info("End voice assistant speech")

logging.info("before main")
def main():
    
    try:
        logging.info("Start handling intent")
        intent:str = get_intent()
        file_name:str = save_voice_file()
        save_intent_to_file(intent, file_name)
        logging.info("Start voice authentication")
        voiceHandler = VoiceAuthentication()
        profile = voiceHandler.find_best_match_above_threshold(voiceSample=Constant.VOICE_PATH+file_name,threshold=Constant.PROFILE_AUTHENTICATION_THRESHOLD)
        logging.info(profile)
        logging.info("Start policy comparison")
        policy_handler = PolicyHandler(intent_dict=parse_ini_file(Constant.INI_FILE_PATH))
        is_allowed = policy_handler.comparePolicyWithProfile(profile[0], intent)
        if (is_allowed[0]):
            logging.info("Intent is allowed")
            intentHandler = IntentHandler()
            response = intentHandler.handle_intent(intent)
            logging.info(response)
            voice_assistant_speech(response)
            logging.info("Intent handled")
        else:
            logging.info("Intent is not allowed")
            voice_assistant_speech(is_allowed[1])
    except OSError as e:
        logging.error(e)
        voice_assistant_speech(e)
main()