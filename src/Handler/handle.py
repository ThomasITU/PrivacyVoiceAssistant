#!/usr/bin/env python

import subprocess
import sys
import json
import random
import datetime


ENDPOINT = "http://localhost:12101/api/play-recording"
PATH = "/tmp/voiceFiles/"
FILE_NAME = PATH+"lastCommand.wav"

def speech(text):
    global o
    o["speech"] = {"text": text}


# get json from stdin and load into python dict
o = json.loads(sys.stdin.read())

intent = o["intent"]["name"]

process = subprocess.Popen(['curl', '--output ${FILE_NAME}', '${ENDPOINT}'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

if intent == "GetTime":
    now = datetime.datetime.now()
    speech("It's %s %d %s." % (now.strftime('%H'), now.minute, now.strftime('%p')))

elif intent == "Hello":
    replies = ['Hi!', 'Hello!', 'Hey there!', 'Greetings.']
    speech(random.choice(replies))

# convert dict to json and print to stdout
print(json.dumps(o))



