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

    def __eq__(self, other): 
        if not isinstance(other, DUR):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.purposes == other.purposes and self.timestamp == other.timestamp


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
    
    def __eq__(self, other): 
        if not isinstance(other, DCR):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.conditions == other.conditions and self.entity == other.entity and self.dataUsageRules == other.dataUsageRules
    
    def __hash__(self) -> int:
        return super(DCR, self).__hash__()


class TR:
    def __init__(self, transferRules:set[DCR]):
        self.transferRules = transferRules
    
    def get_transferRules(self):
        return self.transferRules

    def add_transferRule(self, dataCommunicationRule:DCR):
        self.transferRules.add(dataCommunicationRule)

    def remove_transferRule(self, dataCommunicationRule:DCR):
        self.transferRules.remove(dataCommunicationRule)

    def __eq__(self, other):
        if not isinstance(other, TR):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.transferRules == other.transferRules

class PrivacyPolicy:
    
    def __init__(self, datatype:str, dataCommunicationRules:DCR, transferRules:TR):
        self.datatype = datatype
        self.dataCommunicationRules = dataCommunicationRules
        self.transferRules = {}

    def __eq__(self, other): 
        if not isinstance(other, PrivacyPolicy):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.datatype == other.datatype and self.dataCommunicationRules == other.dataCommunicationRules and self.transferRules == other.transferRules 

