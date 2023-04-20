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
    def __init__(self, intent_dict:dict[str, dict[Entity, list[Purpose]]]):
        self.intentDict = intent_dict


    def comparePolicyWithProfile(self, profile:Profile, intent:str) -> tuple[bool, Entity]:
        try:
            entities:dict = self.intentDict[intent]
            policies:list = profile.get_policy()
            isSuccessfulEntity = (False, None) 

            for p in policies:
                logging.info(p)
                entity = p.dataCommunicationRules.get_entity()
                logging.info(entity)
                if entity not in entities:
                    break
                for purposes in p.dataCommunicationRules.dataUsageRules.get_purposes():
                    logging.info(purposes)
                    if purposes not in entities[entity]:
                        break
                tmp = (True, entity)
                isSuccessfulEntity = tmp
            logging.info(isSuccessfulEntity[0])
            logging.info("Entity: " + isSuccessfulEntity[1].name)
            return isSuccessfulEntity
        except Exception as e:
            logging.info(e)
            return (False, None)