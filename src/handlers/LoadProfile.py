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
import os
from os import getcwd
from pathlib import Path


absolute_path = Path("debug.log").resolve()
logging.basicConfig(format='%(asctime)s - %(message)s', 
                        level=logging.INFO,
                        handlers=[logging.FileHandler(absolute_path),logging.StreamHandler()])
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

path = "/privacyVoiceAssistant/resources/profiles/test1.json"
profile:Profile = SaveAndLoad.load_from_json(path)
logging.info(profile)
print(profile.policy)

data_usage_rules = DUR(purposes={Purpose.WEATHER,Purpose.CALENDER,Purpose.SEARCH,Purpose.NAVIGATION},timestamp = datetime.datetime(1972, 1, 1))
data_communication_rule = DCR(set(),Entity.GOOGLE, data_usage_rules)
pilot = [PrivacyPolicy("Audio",data_communication_rule,set())]
profile.policy = pilot
print(profile.policy)
SaveAndLoad.save_as_json(path,profile)
