from os import getcwd
import os
import sys

sys.path.append("../src/")

import json
import jsonpickle
from util.Generate import Generate as _
from util.SaveAndLoadJson import SaveAndLoadJson
from model.Profile import Profile


def test_encode_given_profile_returns_JSON_string():
    # Arrange
    profile = _.dummyProfile()

    # Act
    actual = SaveAndLoadJson.encode(profile)
    
    # Assert
    assert jsonpickle.dumps(jsonpickle.decode(actual)) == actual

def test_decode_given_JSON_string_returns_profile():
    # Arrange
    profile = _.dummyProfile()
    encoded = SaveAndLoadJson.encode(profile)

    # Act
    actual:Profile = SaveAndLoadJson.decode(encoded)

    # Assert
    assert isinstance(actual, Profile)
    assert actual == profile
