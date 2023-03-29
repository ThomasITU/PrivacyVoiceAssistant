from os import getcwd
import sys, pytest
path = getcwd() + "/../"
sys.path.append(path)

from services.VoiceAuthentication import VoiceAuthentication
from model.Profile import Profile
testPath = getcwd() + "/../voiceSamples/"

def test_CheckSample_given_same_voice_returns_1():
    voiceHandler = VoiceAuthentication()
    sample = testPath + "Hello_speechbrain.wav"
    actual = voiceHandler._check_sample(sample, [sample])

    assert 1 == pytest.approx(actual)


def test_FindBestMatch_given_different_voice_profiles_choose_best_match():
    voiceHandler = VoiceAuthentication()
    sample = testPath + "What_is_lorem_ipsum.wav"

    profile1 = Profile("profile1",[], [testPath + "test.wav", testPath + "test.wav", testPath + "test.wav"])
    profile2 = Profile("profile2",[], [testPath + "der_kommer_måske_spyd_freyja.wav", testPath + "der_kommer_måske_spyd_freyja.wav", testPath + "der_kommer_måske_spyd_freyja.wav"])
    expected = Profile("Expected", [], [testPath + "Hello_speechbrain.wav", testPath + "What_is_lorem_ipsum.wav", testPath + "set_a_timer.wav"])

    profileSamples = [profile1, expected, profile2]

    actual:Profile = voiceHandler._find_best_match(sample, profileSamples)

    assert expected == actual

