from os import getcwd
import os
import sys

sys.path.append("../src/")

import datetime
from model.PrivacyPolicy import DUR, DCR, PrivacyPolicy
from model.enumerations.Purpose import Purpose
from model.enumerations.Entity import Entity
from model.Profile import Profile
from util.Generate import Generate as _
from util.SaveAndLoad import SaveAndLoad as util

path = getcwd() +  "/resources/"


def test_saveAsJson_given_profile_returns_json():
    
    # Arrange
    name = "userLoad"
    voiceFiles = [path+"voiceFiles/" + name +"/Hello_speechbrain.wav", path+"voiceFiles/" + name + "/What_is_lorem_ipsum.wav"]
    purpose = {Purpose.WEATHER, Purpose.CALENDER}
    time = datetime.datetime(1972, 1, 1, 0, 0, 0)
    dur =  DUR(purpose, time)
    conditions = set()
    entity = Entity.GOOGLE
    dcr = DCR(conditions,entity,dur)
    policy = PrivacyPolicy("Audio",dcr,set())
    profile = Profile(name, policy, voiceFiles)
    
    expectedPath = path + name + ".json"

    # Act
    if(os.path.isfile(expectedPath)):
        os.remove(expectedPath)
    assert False == os.path.isfile(expectedPath)

    util.save_as_json(expectedPath,profile)
    
    # Assert
    assert True == os.path.isfile(expectedPath) 

def test_loadFromJson_given_json_returns_profile_with_all_attributes():  

    # Arrange
    expectedName = "user_load"
    expectedVoiceFiles = [path+"voiceFiles/" + expectedName + "/Hello_speechbrain.wav", path+"voiceFiles/" + expectedName +"/What_is_lorem_ipsum.wav"]
    expectedPurpose = {Purpose.WEATHER, Purpose.CALENDER}
    expectedTimestamp = datetime.datetime(1972, 1, 1, 0, 0, 0)
    expectedDur =  DUR(expectedPurpose, expectedTimestamp)
    expectedEntity = Entity.GOOGLE
    expectedDcr = DCR(set(),expectedEntity,expectedDur)
    expectedPolicies = [PrivacyPolicy("Audio",expectedDcr,set())]
    expectedName = "user1"
    expectedProfile = Profile(expectedName, expectedPolicies, expectedVoiceFiles)
    
    expectedPath = path + expectedName + ".json"
    util.save_as_json(path + expectedName + ".json",expectedProfile)
    
    # Act
    actualProfile = util.load_from_json(expectedPath)
    
    # Assert
    assert actualProfile == expectedProfile
    assert actualProfile.name == expectedName
    assert actualProfile.policy == expectedPolicies
    assert actualProfile.voiceSamples == expectedVoiceFiles
    assert actualProfile.policy[0].dataCommunicationRules == expectedDcr
    assert actualProfile.policy[0].dataCommunicationRules.dataUsageRules == expectedDur
    assert actualProfile.policy[0].dataCommunicationRules.dataUsageRules.purposes == expectedPurpose
    assert actualProfile.policy[0].dataCommunicationRules.dataUsageRules.timestamp == expectedTimestamp
    assert actualProfile.policy[0].dataCommunicationRules.entity == expectedEntity
    assert actualProfile.policy[0].dataCommunicationRules.conditions == set()

def test_get_policy_returns_list_of_privacy_policies():
    #Arrange
    profile = _.dummyProfile()
    
    dataUsageRules = DUR(purposes = {Purpose.WEATHER, Purpose.SEARCH},timestamp = datetime.datetime(1972, 1, 1))
    dataCommunicationRule = DCR(set(),Entity.GOOGLE,dataUsageRules)
    expectedPolicies = [PrivacyPolicy("Audio",dataCommunicationRule,set())]
    #Act
    actualPolicies = profile.get_policy()

    #Assert
    assert isinstance(actualPolicies, list)
    assert expectedPolicies == actualPolicies