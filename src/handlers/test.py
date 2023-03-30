#!/usr/bin/env python3.10

import sys
import json
import random
import datetime
import logging
import subprocess
import sys
import json
import uuid
from os import getcwd
logging.basicConfig(format='%(asctime)s - %(message)s', 
                        level=logging.INFO,
                        handlers=[logging.FileHandler("tmp/debug.log"),logging.StreamHandler()])
logging.info("importing modules")

sys.path.append("/privacyVoiceAssistant/src")
sys.path.append(getcwd() + "../../src/")

try:
    from handlers.IntentHandler import IntentHandler
    from handlers.PolicyHandler import PolicyHandler
    from services.VoiceAuthentication import VoiceAuthentication
    from model.Constant import Constant
    from util.SaveAndLoad import SaveAndLoad
    from util.SentencesParser import parse_ini_file
except Exception as e:
    logging.info(getcwd())
    logging.info(e)

def speech(text):
    global o
    o["speech"] = {"text": text}


# get json from stdin and load into python dict
o = json.loads(sys.stdin.read())

intent = o["intent"]["name"]

if intent == "GetTime":
    now = datetime.datetime.now()
    speech("It's %s %d %s." % (now.strftime('%H'), now.minute, now.strftime('%p')))

elif intent == "Hello":
    replies = ['Hi!', 'Hello!', 'Hey there!', 'Greetings.']
    speech(random.choice(replies))

with open("/tmp/test.json", 'w') as outfile:
    json.dump(o, outfile)
# convert dict to json and print to stdout

print(json.dumps(o))
