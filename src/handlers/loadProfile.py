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
try:
    from handlers.IntentHandler import IntentHandler
    from handlers.PolicyHandler import PolicyHandler
    from services.VoiceAuthentication import VoiceAuthentication
    from model.Constant import Constant
    from util.SaveAndLoad import SaveAndLoad
    from util.SentencesParser import parse_ini_file
    from model.Profile import Profile
    from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy
    from model.enumerations.Entity import Entity
    from model.enumerations.Purpose import Purpose
except Exception as e:
    logging.info(getcwd())
    logging.info(e)

path = "/privacyVoiceAssistant/resources/profiles/test2.json"
profile:Profile = SaveAndLoad.load_from_json(path)
logging.info(profile)
print(profile.policy)

dataUsageRules = DUR(purposes = {Purpose.NAVIGATION},timestamp = datetime.datetime(1972, 1, 1))
dataCommunicationRule = DCR(set(),Entity.GOOGLE,dataUsageRules)
pilot = [PrivacyPolicy("Audio",dataCommunicationRule,set())]
profile.policy = pilot
print(profile.policy)
SaveAndLoad.save_as_json(path,profile)
