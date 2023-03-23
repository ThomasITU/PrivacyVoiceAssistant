from os import getcwd
import os
import sys
from pydub import AudioSegment

sys.path.append("../src/")

import datetime
from model.PrivacyPolicy import DUR, DCR, TR, Expression, PrivacyPolicy
from model.enumerations.Purpose import Purpose
from model.enumerations.Entity import Entity
from model.Profile import Profile
from util.SaveAndLoad import SaveAndLoad as util
from util.Generate import Generate as _
from model.VoiceSample import VoiceSample


path = getcwd() +  "/resources/"

def test_saveAsJson_given_profile_saves_to_path():
    
    # Arrange
    profile = _.dummyProfile()
    profile.name ="userLoad"
    expectedPath = path + profile.name + ".json"

    # Act
    if(os.path.isfile(expectedPath)):
        os.remove(expectedPath)
    assert False == os.path.isfile(expectedPath)

    util.saveAsJson(expectedPath,profile)
    
    # Assert
    assert True == os.path.isfile(expectedPath) 

def test_loadFromJson_given_json_returns_profile_with_all_attributes():  

    # Arrange
    expectedName = "user1"
    expectedVoiceFiles = [path+"voiceFiles/" + expectedName + "/Hello_speechbrain.wav", path+"voiceFiles/" + expectedName +"/What_is_lorem_ipsum.wav"]
    expectedPurpose = {Purpose.WEATHER, Purpose.CALENDER}
    expectedTimestamp = datetime.datetime(1972, 1, 1, 0, 0, 0)
    expectedDur =  DUR(expectedPurpose, expectedTimestamp)
    expectedEntity = Entity.GOOGLE
    expectedDcr = DCR(set(),expectedEntity,expectedDur)
    expectedPolicies = [PrivacyPolicy("Audio",expectedDcr,set())]
    expectedProfile = Profile(expectedName, expectedPolicies, expectedVoiceFiles, [])
    
    expectedPath = path + expectedName + ".json"
    util.saveAsJson(path + expectedName + ".json",expectedProfile)
    
    # Act
    actualProfile = util.loadFromJson(expectedPath)
    
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

def test_saveAsJson_given_profile_saves_audio_files_as_wav_files():
    # Arrange
    profile = _.dummyProfile()
    wavObj = VoiceSample(path + "voiceFiles/", "Hello_speechbrain.wav")
    wavObjs:list[VoiceSample] = [wavObj]
    profile.wavObjects = wavObjs
    
    expectedPath = path + "profiles/"+ profile.name +".json"

    # Act
    util.saveAsJson(expectedPath,profile)

    # Assert
    assert os.path.isfile(expectedPath)
    # assert os.path.isfile(f"{path}profiles/{profile.name}/voiceSamples/{wavObj.fileName}")

def test_loadAsJson_given_profile_path_loads_audio_files_as_wav_files():

    # Arrange
    expectedProfile = _.dummyProfile()
    expectedWavObj = VoiceSample(path + "voiceFiles/", "Hello_speechbrain.wav")
    expectedWavObjs:list[VoiceSample] = [expectedWavObj]
    expectedProfile.wavObjects = expectedWavObjs

    # Act
    actual:Profile = util.loadFromJson(path + "profiles/" + expectedProfile.name + ".json")

    # Assert
    assert expectedProfile.wavObjects == actual.wavObjects
    assert expectedProfile.wavObjects[0] == expectedWavObj