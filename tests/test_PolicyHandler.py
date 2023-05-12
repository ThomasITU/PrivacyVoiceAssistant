import datetime
from os import getcwd
import sys
sys.path.append("../src/")
from util.Generate import Generate as _

from handlers.PolicyHandler import PolicyHandler
from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy
from model.Profile import Profile
from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose
from model.Constant import Constant


path = getcwd() +  "/resources/"

def test_comparePolicyWithProfile_returns_proper_tuple():
    #Arrange
    profile = _.dummyProfile()
    expectedTrue = (True, Entity.GOOGLE)
    expectedFalse = (False, None)
    
    #Arrange IntentDicts
    dictPurposes = {Purpose.WEATHER, Purpose.CALENDER, Purpose.SEARCH}
    dictEntities = {Entity.GOOGLE: dictPurposes,Entity.ALEXA: dictPurposes}
    dictIntent = {"DummyIntent": dictEntities}

    dictEntitiesDifferent = {Entity.ALEXA: dictPurposes}
    dictIntentDifferent = {"DummyIntent": dictEntitiesDifferent}

    #Arrange PolicyHandler dictionaries
    policyHandlerSame = PolicyHandler(intent_dict=dictIntent)
    policyHandlerDifferent = PolicyHandler(intent_dict=dictIntentDifferent)

    #Act
    actualTrue = policyHandlerSame.comparePolicyWithProfile(profile, "DummyIntent")
    actualFalse = policyHandlerDifferent.comparePolicyWithProfile(profile, "DummyIntent")

    #Assert

    assert expectedTrue[0] == actualTrue[0]
    assert expectedTrue[1] == actualTrue[1]

    assert expectedFalse[0] == actualFalse[0]
    assert expectedFalse[1] == actualFalse[1]