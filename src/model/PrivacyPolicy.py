import datetime
from model.enumerations.Purpose import Purpose
from model.enumerations.Entity import Entity

class DUR:
    def __init__(self, purposes:set[Purpose], timestamp:datetime):
        self.purposes = purposes
        self.timestamp = timestamp
    
    def get_purposes(self):
        return self.purposes
    
    def get_timestamp(self):
        return self.timestamp
    
    def add_purpose(self, purpose:Purpose):
        self.purposes.add(purpose)

    def remove_purpose(self, purpose:Purpose):
        self.purposes.remove(purpose)

class Expression:
    NotImplemented

class DCR:
    def __init__(self, conditions:set[Expression], entity:Entity, dataUsageRules:DUR):
        self.conditions = conditions
        self.entity = entity
        self.dataUsageRules = dataUsageRules

    def get_conditions(self):
        return self.conditions

    def get_entity(self):
        return self.entity

    def get_dur(self):
        return self.dataUsageRules
    
    def add_expression(self, exp:Expression):
        self.conditions.app(exp)

    def remove_expression(self, exp:Expression):
        self.conditions.remove(exp)
    
    def set_dur(self, dur:DUR):
        self.dataUsageRules = dur
    
    def set_entity(self, entity:Entity):
        self.entity = entity

class TR:
    def __init__(self, transferRules:set[DCR]):
        self.transferRules = transferRules
    
    def get_transferRules(self):
        return self.transferRules

    def add_transferRule(self, dataCommunicationRule:DCR):
        self.transferRules.add(dataCommunicationRule)

    def remove_transferRule(self, dataCommunicationRule:DCR):
        self.transferRules.remove(dataCommunicationRule)

class PrivacyPolicy:
    
    def __init__(self, datatype:str, dataCommunicationRules:DCR, transferRules:TR):
        self.datatype = datatype
        self.dataCommunicationRules = dataCommunicationRules
        self.transferRules = {}
