from os import getcwd
import os
import sys
sys.path.append("../src/")

import datetime
from model.PrivacyPolicy import DUR, DCR, TR, Expression, PrivacyPolicy
from model.enumerations.Purpose import Purpose
from model.enumerations.Entity import Entity
from model.Profile import Profile
from util.SaveAndLoadJson import SaveAndLoadJson as util

path = getcwd() +  "/resources/"


def test_saveAsJson_given_profile_returns_json():
    
    # Arrange
    name = "user_load"
    voiceFiles = [path+"voiceFiles/" + name +"/Hello_speechbrain.wav", path+"voiceFiles/" + name + "/What_is_lorem_ipsum.wav"]
    purpose = set([Purpose.WEATHER, Purpose.CALENDER])
    time = datetime.datetime(1972, 1, 1, 0, 0, 0)
    dur =  DUR(purpose, time)
    сonditions = set()
    entity = Entity.GOOGLE
    dcr = DCR(сonditions,entity,dur)
    policy = PrivacyPolicy("Audio",dcr,set())
    profile = Profile(name, policy, voiceFiles)
    
    expectedPath = path + name + ".json"

    # Act +
    util.saveAsJson(path + name + ".json",profile)
    
    # Assert
    assert True == os.path.isfile(expectedPath) 

def test_loadFromJson_given_json_returns_profile():  

    # Arrange
    name = "user_load"
    voiceFiles = [path+"voiceFiles/" + name + "/Hello_speechbrain.wav", path+"voiceFiles/" + name +"/What_is_lorem_ipsum.wav"]
    purpose = set([Purpose.WEATHER, Purpose.CALENDER])
    time = datetime.datetime(1972, 1, 1, 0, 0, 0)
    dur =  DUR(purpose, time)
    сonditions = set()
    entity = Entity.GOOGLE
    dcr = DCR(сonditions,entity,dur)
    policy = PrivacyPolicy("Audio",dcr,set())
    name = "user1"
    profile = Profile(name, policy, voiceFiles)
    
    expectedPath = path + name + ".json"
    util.saveAsJson(path + name + ".json",profile)
    
    # Act
    actualProfile = util.loadFromJson(expectedPath)
    
    # Assert
    assert profile == actualProfile
    assert profile.name == actualProfile.name
    assert profile.policy == actualProfile.policy
    assert profile.voiceSamples == actualProfile.voiceSamples