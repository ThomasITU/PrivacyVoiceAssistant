import sys
sys.path.append("/privacyVoiceAssistant/src")
sys.path.append("../src/")

from util.SentencesParser import parse_ini_file
from model.Profile import Profile
from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose



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
        is_successful_entity = (False, None) 

        for policy in policies:
            entity = policy.dataCommunicationRules.get_entity()
            if entity not in entities:
                continue

            purposes = policy.dataCommunicationRules.dataUsageRules.get_purposes()
            if not purposes:  
                continue
            
            entity_purposes:set[Purpose] = set(entities[entity])
            is_strict_superset = entity_purposes.issuperset(purposes) and entity_purposes != purposes
            if is_strict_superset:
                continue
            tmp = (True, entity)
            is_successful_entity = tmp
        return is_successful_entity
