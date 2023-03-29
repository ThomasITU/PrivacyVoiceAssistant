#!/usr/bin/env python

import subprocess
import sys
import json
import random
import datetime
import uuid
from os import getcwd
sys.path.append(getcwd() + "/../")
from handlers.IntentHandler import IntentHandler
from handlers.PolicyHandler import PolicyHandler
from services.VoiceAuthentication import VoiceAuthentication

ENDPOINT = "http://localhost:12101/api/play-recording"
VOICEPATH = "/tmp/voiceFiles/"
INTENTPATH ="/tmp/intents/"

def save_intent_to_file(intent:str, file_name:str):
    file_name = f"{file_name.removesuffix('.wav')}.txt"
    f = open(INTENTPATH+file_name, "w")
    f.write(intent + "\n")
    f.close()

def save_voice_file() -> str:
    file_name:str = uuid.uuid4()+".wav"
    process = subprocess.Popen(['curl', '--output', VOICEPATH+file_name, ENDPOINT], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    return file_name

def get_intent(file_name:str) -> str:
    # get json from stdin and load into python dict
    global dictionary
    dictionary = json.loads(sys.stdin.read())
    intent = dictionary["intent"]["name"]
    save_intent_to_file(intent, file_name)
    return intent

def voice_assistant_speech(text:str):
    speech = dict()
    speech["speech"] = {"text": text}
    print(json.dumps(speech))



def main():
    fileName = save_voice_file()
    intent = save_intent_to_file()
    (profile, response) = VoiceAuthentication.FindBestMatch(fileName,)
    isAllowed = PolicyHandler.comparePolicyWithProfile()
    if (isAllowed[0]):
        iisAllowed[1]

if __name__ == '__main__':
    main()