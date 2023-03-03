from os import getcwd
import sys, pytest
path = "/home/boot/Desktop/VoiceAssistant/PrivacyVoiceAssistant"
sys.path.insert(0, path)

from services.VoiceAuthentication import VoiceAuthentication
from model.Profile import Profile
voicePath = "/home/boot/Desktop/PrivacyVoiceAssistant/voiceSamples/"
testPath = getcwd() + "/../voiceSamples/"

def test_CheckSample_given_same_voice_returns_1():
    voiceHandler = VoiceAuthentication()
    sample = voicePath + "Hello_speechbrain.wav"
    actual = voiceHandler.CheckSample(sample, [sample])

    assert 1 == pytest.approx(actual)


def test_FindBestMatch_given_different_voice_profiles_choose_best_match():
    voiceHandler = VoiceAuthentication()
    sample = voicePath + "What_is_lorem_ipsum.wav"

    profile1 = Profile("profile1",[], [voicePath + "test.wav", voicePath + "test.wav", voicePath + "test.wav"])
    profile2 = Profile("profile2",[], [voicePath + "der_kommer_måske_spyd_freyja.wav", voicePath + "der_kommer_måske_spyd_freyja.wav", voicePath + "der_kommer_måske_spyd_freyja.wav"])
    expected = Profile("Expected", [], [voicePath + "Hello_speechbrain.wav", voicePath + "What_is_lorem_ipsum.wav", voicePath + "set_a_timer.wav"])

    profileSamples = [profile1, expected, profile2]

    actual:Profile = voiceHandler.FindBestMatch(sample, profileSamples)

    assert expected == actual

