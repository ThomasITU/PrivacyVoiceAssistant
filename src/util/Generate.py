from copy import deepcopy
from pathlib import Path
import datetime
import logging

from model.enumerations.Entity import Entity

from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy
from model.Profile import Profile,PrivacyPolicy
from model.enumerations.Purpose import Purpose


class Generate():

    def logingConfig(logger:logging):
        absolute_path = Path("/tmp/debug.log").resolve() 
        logger.basicConfig(format='%(asctime)s - %(message)s', 
                    level=logging.INFO,
                    handlers=[logging.FileHandler(absolute_path),logging.StreamHandler()])

    def dummyProfile() -> Profile: 
        dataUsageRules = DUR(purposes = {Purpose.WEATHER, Purpose.SEARCH},timestamp = datetime.datetime(1972, 1, 1))
        dataCommunicationRule = DCR(set(),Entity.GOOGLE,dataUsageRules)
        pilot = [PrivacyPolicy("Audio",dataCommunicationRule,set())]
        voiceFiles = ["unknown/hello.wav", "unknown/what_is_lorem_ipsum.wav"]

        profile = Profile("Test Profile", pilot, voiceFiles)
        return profile
    
    def dummyIntentDict():
        purposes = dict()
        for p in Purpose:
            purposes[p] = True
            entities = dict()
        for e in Entity:
            entities[e] = deepcopy(purposes)

        dummyDict = dict()
        dummyDict["LongSentence"] = deepcopy(entities)
        dummyDict["GetTime"] = deepcopy(entities)

        return dummyDict