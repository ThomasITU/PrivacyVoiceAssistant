import datetime
from os import getcwd
import os
import sys
sys.path.append("../src/")
from util.SaveAndLoadJson import SaveAndLoadJson as util
from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose
from util.SentencesParser import parseIniFile, removeEntityFromIntent, removePurposeFromIntent

path = getcwd() +  "/resources/"

def test_parseIniFile_given_ini_file_returns__matching_dictionary():

    # Arrange
    purposeDict = {}
    entityDict = {}
    for p in Purpose:
        purposeDict[p] = True
    for e in Entity:
        entityDict[e] = purposeDict
    expectedIntentsDict = {
        "LongSentence": entityDict,
        "GetTime": entityDict
    }

    # Act
    actualIntentsDict = parseIniFile(path + "/sentenceTest.ini")

    hasPurpose = actualIntentsDict.get("LongSentence").get(Entity.ALEXA).get(Purpose.CALENDER)
   
    # Assert
    assert True == hasPurpose
    assert expectedIntentsDict == actualIntentsDict

def test_removeEntityFromIntent_removes_entity():

    # Arrange
    purposeDict = {}
    entityDict = {}
    for p in Purpose:
        purposeDict[p] = True
    for e in Entity:
        entityDict[e] = purposeDict
    intentDict = {
        "LongSentence": entityDict,
        "GetTime": entityDict
    }

    #Pre-Assert
    assert (Entity.ALEXA in intentDict.get("LongSentence"))

    # Act
    removeEntityFromIntent(intentDict, "LongSentence", Entity.ALEXA)
    # Assert
    assert (Entity.ALEXA not in intentDict.get("LongSentence"))


def test_removePurposeFromIntent_removes_purpose_from_specified_intent():
    # Arrange
    purposeDict = {}
    entityDict = {}
    for p in Purpose:
        purposeDict[p] = True
    for e in Entity:
        entityDict[e] = purposeDict
    intentDict = {
        "LongSentence": entityDict,
        "GetTime": entityDict
    }

    preAssertedDictionary = intentDict.get("LongSentence")

    #Pre-assert
    assert (Purpose.CALENDER in preAssertedDictionary.get(Entity.ALEXA))
    assert (Purpose.CALENDER in preAssertedDictionary.get(Entity.GOOGLE))

    # Act
    #Remove calendar from all entities in LongSentence
    removePurposeFromIntent(preAssertedDictionary, "LongSentence", Purpose.CALENDER)


    # Assert
    assert (Purpose.CALENDER not in preAssertedDictionary.get(Entity.ALEXA))
    assert (Purpose.CALENDER not in preAssertedDictionary.get(Entity.GOOGLE))