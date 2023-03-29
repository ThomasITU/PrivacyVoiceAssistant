
import datetime
import sys
sys.path.append("../src/")

from model.enumerations.Entity import Entity
from model.PrivacyPolicy import DCR, DUR, PrivacyPolicy, Purpose
from util.Generate import Generate as _

def test_get_dcr_returns_dataCommunicationRules():
    # Arrange
    profile = _.dummyProfile()
    dataUsageRules = DUR(purposes = {Purpose.WEATHER, Purpose.SEARCH},timestamp = datetime.datetime(1972, 1, 1))
    expectedDcr = DCR(set(),Entity.GOOGLE,dataUsageRules)

    # Act
    actual = profile.policy[0].dataCommunicationRules

    # Assert
    assert actual.dataUsageRules == expectedDcr.dataUsageRules
    assert actual.entity == expectedDcr.entity
    assert actual.conditions == expectedDcr.conditions
    assert actual == expectedDcr
    
def test_get_dur_returns_dataUsageRules():
    # Arrange
    profile = _.dummyProfile()
    expectedDur = DUR(purposes = {Purpose.WEATHER, Purpose.SEARCH},timestamp = datetime.datetime(1972, 1, 1))

    # Act
    actual = profile.policy[0].dataCommunicationRules.dataUsageRules
     
    # Assert   
    assert actual.purposes == expectedDur.purposes
    assert actual.timestamp == expectedDur.timestamp
    assert actual == expectedDur 

def test_get_purpose_returns_purpose():
    # Arrange
    profile = _.dummyProfile()
    expectedPurposes = {Purpose.WEATHER, Purpose.SEARCH}

    # Act
    actual = profile.policy[0].dataCommunicationRules.dataUsageRules.purposes

    # Assert
    assert actual == expectedPurposes
    

