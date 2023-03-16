from os import getcwd
import sys
sys.path.append("../src/")
path = getcwd() +  "/resources/sentenceTest.ini"

from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose
from util.SentencesParser import parseIniFile, removeEntityFromIntent, removePurposeFromIntent
import copy as _

def generateDummyDictionary() -> dict:
    purposes = dict()
    for p in Purpose:
        purposes[p] = True
    entitities = dict()
    for e in Entity:
        entitities[e] = _.deepcopy(purposes)

    dummyDict = dict()
    dummyDict["LongSentence"] = _.deepcopy(entitities)
    dummyDict["GetTime"] = _.deepcopy(entitities)

    return dummyDict

def test_parseIniFile_given_ini_file_returns__matching_dictionary():

    # Arrange
    expected = generateDummyDictionary()

    # Act
    actual = parseIniFile(path)

    hasPurpose = actual.get("LongSentence").get(Entity.ALEXA).get(Purpose.CALENDER)
   
    # Assert
    assert True == hasPurpose
    assert expected == actual
    assert ("random" not in actual) == True 

def test_removeEntityFromIntent_removes_entity():

    # Arrange
    intentDict = generateDummyDictionary()

    #Pre-Assert
    assert (Entity.ALEXA in intentDict.get("LongSentence"))

    # Act
    removeEntityFromIntent(intentDict, "LongSentence", Entity.ALEXA)
    # Assert
    assert (Entity.ALEXA not in intentDict.get("LongSentence"))


def test_removePurposeFromIntent_removes_purpose_from_specified_intent():
    
    # Arrange
    intentDict = generateDummyDictionary()

    preAssertedDictionary = intentDict.get("LongSentence")

    #Pre-assert
    assert (Purpose.CALENDER in preAssertedDictionary.get(Entity.ALEXA))
    assert (Purpose.CALENDER in preAssertedDictionary.get(Entity.GOOGLE))

    # Act
    #Remove calendar from all entities in LongSentence
    removePurposeFromIntent(intentDict, "LongSentence", Purpose.CALENDER)

    # Assert
    assert (Purpose.CALENDER not in preAssertedDictionary.get(Entity.ALEXA))
    assert (Purpose.CALENDER not in preAssertedDictionary.get(Entity.GOOGLE))

    assert (Purpose.NAVIGATION in preAssertedDictionary.get(Entity.ALEXA))
    assert (Purpose.NAVIGATION in preAssertedDictionary.get(Entity.GOOGLE))

    assert (Entity.GOOGLE in intentDict.get("LongSentence"))
    assert (Entity.ALEXA in intentDict.get("GetTime"))
