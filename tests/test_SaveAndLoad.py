from os import getcwd
import pickle
import sys

sys.path.append("../src/")
from util.Generate import Generate as _
from util.SaveAndLoad import SaveAndLoad
from model.Profile import Profile


def test_encode_given_profile_returns_bytes():
    # Arrange
    profile = _.dummyProfile()

    # Act
    actual = SaveAndLoad.encode(profile)
    
    # Assert
    assert pickle.dumps(pickle.loads(actual)) == actual

def test_decode_given_bytes_returns_profile():
    # Arrange
    profile = _.dummyProfile()
    encoded = SaveAndLoad.encode(profile)

    # Act
    actual:Profile = SaveAndLoad.decode(encoded)

    # Assert
    assert isinstance(actual, Profile)
    assert actual == profile

def test_decode_given_bytes_returns_profile_with_all_attributes():
    # Arrange
    expectedProfile = _.dummyProfile()
    encoded = SaveAndLoad.encode(expectedProfile)
    expectedPolicy = expectedProfile.policy[0]
    expectedDcr = expectedProfile.policy[0].dataCommunicationRules
    expectedDur = expectedProfile.policy[0].dataCommunicationRules.dataUsageRules
    expectedPurposes = expectedProfile.policy[0].dataCommunicationRules.dataUsageRules.purposes
    expectedName = expectedProfile.name

    # Act
    actual = SaveAndLoad.decode(encoded)
    actualPolice = actual.policy[0]

    # Assert
    assert actual == expectedProfile
    assert actual.name == expectedName
    assert actualPolice == expectedPolicy
    assert actualPolice.dataCommunicationRules == expectedDcr
    assert actualPolice.dataCommunicationRules.dataUsageRules == expectedDur
    assert actualPolice.dataCommunicationRules.dataUsageRules.purposes == expectedPurposes
