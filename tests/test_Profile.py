import datetime
from os import getcwd
import os
import sys, pytest
sys.path.append("../src/")
from model.PrivacyPolicy import DUR, DCR, TR, Expression, PrivacyPolicy
from model.enumerations.Purpose import Purpose
from model.enumerations.Entity import Entity
from model.Profile import Profile, loadFromJson, saveAsJson

path = getcwd() +  "/resources/"


def test_saveAsJson_given_profile_returns_json():
    
    # Arrange
    name = "user_load"
    voiceFiles = [path+"voiceFiles/" + name +"/Hello_speechbrain.wav", path+"voiceFiles/" + name + "/What_is_lorem_ipsum.wav"]
    purpose = set([Purpose.WEATHER, Purpose.CALENDER])
    time = datetime.datetime.now()
    dur =  DUR(purpose, time)
    сonditions = set()
    entity = Entity.GOOGLE
    dcr = DCR(сonditions,entity,dur)
    policy = PrivacyPolicy("Audio",dcr,set())
    profile = Profile(name, policy, voiceFiles)
    
    expectedPath = path + name + ".json"

    # Act +
    saveAsJson(path + name,profile)
    
    # Assert
    assert True == os.path.isfile(expectedPath) 

def test_loadFromJson_given_json_returns_profile():  

    # Arrange
    name = "user_load"
    voiceFiles = [path+"voiceFiles/" + name + "/Hello_speechbrain.wav", path+"voiceFiles/" + name +"/What_is_lorem_ipsum.wav"]
    purpose = set([Purpose.WEATHER, Purpose.CALENDER])
    time = datetime.datetime.year()
    dur =  DUR(purpose, time)
    сonditions = set()
    entity = Entity.GOOGLE
    dcr = DCR(сonditions,entity,dur)
    policy = PrivacyPolicy("Audio",dcr,set())
    name = "user1"
    profile = Profile(name, policy, voiceFiles)
    
    expectedPath = path + name + ".json"
    saveAsJson(path + name,profile)
    
    # Act
    actualProfile = loadFromJson(expectedPath)
    
    # Assert
    assert profile.name == actualProfile.name
    assert profile.policy == actualProfile.policy
    assert profile.voiceSamples == actualProfile.voiceSamples