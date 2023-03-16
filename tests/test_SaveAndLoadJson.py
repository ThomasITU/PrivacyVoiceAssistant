from os import getcwd
import os
import pickle
import sys

sys.path.append("../src/")

import json
import jsonpickle
from util.Generate import Generate as _
from util.SaveAndLoadJson import SaveAndLoadJson
from model.Profile import Profile


def test_encode_given_profile_returns_bytes():
    # Arrange
    profile = _.dummyProfile()

    # Act
    actual = SaveAndLoadJson.encode(profile)
    
    # Assert
    assert pickle.dumps(pickle.loads(actual)) == actual

def test_decode_given_bytes_returns_profile():
    # Arrange
    profile = _.dummyProfile()
    encoded = SaveAndLoadJson.encode(profile)

    # Act
    actual:Profile = SaveAndLoadJson.decode(encoded)

    # Assert
    assert isinstance(actual, Profile)
    assert actual == profile
