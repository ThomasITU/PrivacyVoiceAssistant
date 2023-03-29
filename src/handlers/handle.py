#!/usr/bin/env python

import subprocess
import sys
import json
import random
import datetime
import uuid
from handlers.PolicyHandler import PolicyHandler

from services.VoiceAuthentication import VoiceAuthentication

ENDPOINT = "http://localhost:12101/api/play-recording"
PATH = "/tmp/voiceFiles/"
global o
def save_intent_to_file(intent:str, fileName:str):
    f = open("/tmp/lastIntent.txt", "w")
    f.write(intent + "\n")
    f.close()

def save_voice_file() -> str:
    fileName = PATH+uuid.uuid4()+".wav"
    process = subprocess.Popen(['curl', '--output', fileName, ENDPOINT], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    return fileName

def get_intent(file_name:str) -> str:
    # get json from stdin and load into python dict
    o = json.loads(sys.stdin.read())

    intent = o["intent"]["name"]
    return intent

def speech(text):
    o["speech"] = {"text": text}



if intent == "GetTime":
    now = datetime.datetime.now()
    speech("It's %s %d %s." % (now.strftime('%H'), now.minute, now.strftime('%p')))

elif intent == "Hello":
    replies = ['Hi!', 'Hello!', 'Hey there!', 'Greetings.']
    speech(random.choice(replies))

# convert dict to json and print to stdout
print(json.dumps(o))

def main():
    fileName = save_voice_file()
    intent = save_intent_to_file()
    (profile, response) = VoiceAuthentication.FindBestMatch(fileName,)
    isAllowed = PolicyHandler.comparePolicyWithProfile()
    if (isAllowed[0]):
        iisAllowed[1]

if __name__ == '__main__':
    main()