from os import getcwd
import sys
sys.path.append("../src/")

from model.enumerations.Entity import Entity
from model.enumerations.Purpose import Purpose
from util.SentencesParser import parseIniFile
import copy as _
path = getcwd() +  "/resources/sentencesTest.ini"

def generateDummyDictionary() -> dict:
    purposes = dict()
    for p in Purpose:
        purposes[p] = True

    entitities = dict()
    for e in Entity:
        entitities[e] = _.deepcopy(purposes)

    dummyDict = dict()
    dummyDict["LongSentence"] = _.deepcopy(entitities)
    dummyDict["GetTemperature"] = _.deepcopy(entitities)
    dummyDict["GetGarageState"] = _.deepcopy(entitities)
    dummyDict["ChangeLightState"] = _.deepcopy(entitities)

    return dummyDict



def test_parseIniFile_given_ini_file_returns_dictionary():
    # Arrange
    expected:dict = generateDummyDictionary()

    # Act
    actual = parseIniFile(path)

    # Assert
    assert actual == expected
    assert actual.get("LongSentence").get(Entity.ALEXA).get(Purpose.WEATHER) == True
    assert actual.get("ChangeLightState").get(Entity.GOOGLE).get(Purpose.SEARCH) == True
    assert ("random" not in actual) == True 