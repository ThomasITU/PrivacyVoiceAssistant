import sys

import logging
import sys
sys.path.append("/privacyVoiceAssistant/src")
sys.path.append("../src/")

try:
    from util.Generate import Generate
    Generate.logingConfig(logging)
    from util.SentencesParser import parse_ini_file
    from model.Profile import Profile
    from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy
    from model.enumerations.Entity import Entity
    from model.enumerations.Purpose import Purpose
    from model.Constant import Constant
except Exception as e:
    logging.info(e)


class PolicyHandler:

    def __init__(self, intent_dict):
        if isinstance(intent_dict, dict):
            self.intentDict = intent_dict
        elif isinstance(intent_dict,str):
            self.intentDict = parse_ini_file(intent_dict)
        else:
            raise ValueError("intent_dict must be either a dictionary or a string")


    def comparePolicyWithProfile(self, profile:Profile, intent:str) -> tuple[bool, Entity]:
        entities:dict = self.intentDict[intent]
        policies:list = profile.get_policy()

        print(policies)
        isSuccessfulEntity = (False, None) 

        for policy in policies:
            entity = policy.dataCommunicationRules.get_entity()
            if entity not in entities:
                continue

            purposes = policy.dataCommunicationRules.dataUsageRules.get_purposes()
            if not purposes:  
                continue
            
            for purpose in purposes:
                if purpose not in entities[entity]:
                    continue
            tmp = (True, entity)
            isSuccessfulEntity = tmp
        return isSuccessfulEntity
