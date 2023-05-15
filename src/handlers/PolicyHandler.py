import sys

import logging
import sys
sys.path.append("/privacyVoiceAssistant/src")
sys.path.append("../src/")

from util.Generate import Generate
Generate.logingConfig(logging)
from util.SentencesParser import parse_ini_file
from model.Profile import Profile
from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy
from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose
from model.Constant import Constant


class PolicyHandler:

    def __init__(self, intent_dict):
        logging.info(len(intent_dict))
        if isinstance(intent_dict, dict):
            self.intentDict = intent_dict
        elif isinstance(intent_dict,str):
            self.intentDict = parse_ini_file(intent_dict)
        else:
            raise ValueError("intent_dict must be either a dictionary or a string")


    def comparePolicyWithProfile(self, profile:Profile, intent:str) -> tuple[bool, Entity]:
        entities:dict = self.intentDict[intent]
        policies:list = profile.get_policy()

        logging.info(len(policies))
        isSuccessfulEntity = (False, None) 

        for policy in policies:
            entity = policy.dataCommunicationRules.get_entity()
            if entity not in entities:
                continue

            purposes = policy.dataCommunicationRules.dataUsageRules.get_purposes()
            if not purposes:  
                continue
            
            entityPurposes:set[Purpose] = set(entities[entity])
            logging.info(f"entityPurposes: {len(entityPurposes)}")
            logging.info(f"purposes: {len(purposes)}")
            isStrictSuperset = entityPurposes.issuperset(purposes) and entityPurposes != purposes
            logging.info(f"isSuperset: {isStrictSuperset}")
            if isStrictSuperset:
                continue
            tmp = (True, entity)
            isSuccessfulEntity = tmp
        return isSuccessfulEntity
