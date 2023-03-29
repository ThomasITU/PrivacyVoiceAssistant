
from datetime import datetime
from os import getcwd
import sys



sys.path.append("../src/")
from util.SentencesParser import parseIniFile
from model.Profile import Profile
from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy
from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose

class PolicyHandler:
    
    def __init__(self, intent_dict = parseIniFile(f"{getcwd()}/../.config/profiles/sentences.ini")):
        self.intentDict = intent_dict


    def comparePolicyWithProfile(self, profile:Profile, intent:str) -> tuple[bool, Entity]:
        entities:dict = self.intentDict[intent]
        policies:list = profile.get_policy()
        print(policies)
        isSuccessfulEntity = (False, None) 

        for p in policies:
            entity = p.dataCommunicationRules.get_entity()
            if entity not in entities:
                break
            for purposes in p.dataCommunicationRules.dataUsageRules.get_purposes():
                if purposes not in entities[entity]:
                    break
            isSuccessfulEntity = (True, entity)
        return isSuccessfulEntity