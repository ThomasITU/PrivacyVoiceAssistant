import sys, pytest
path = "/home/main/Desktop/VoiceAssistant/PrivacyVoiceAssistant"
sys.path.insert(0, path)
from VoiceAuthentication import VoiceAuthentication
from PolicyHandler import Profile
path += "/VoiceSamples/"

def test_CheckSample_given_same_voice_returns_1():
    voiceHandler = VoiceAuthentication()
    sample = path + "Hello_speechbrain.wav"
    actual = voiceHandler.CheckSample(sample, [sample])

    assert 1 == pytest.approx(actual)


def test_FindBestMatch_given_different_voice_profiles_choose_best_match():
    voiceHandler = VoiceAuthentication()
    sample = path + "What_is_lorem_ipsum.wav"

    profile1 = Profile("profile1",[], [path + "test.wav", path + "test.wav", path + "test.wav"])
    profile2 = Profile("profile2",[], [path + "der_kommer_spyd.wav", path + "der_kommer_spyd.wav", path + "der_kommer_spyd.wav"])
    expected = Profile("Expected", [], [path + "Hello_speechbrain.wav", path + "What_is_lorem_ipsum.wav", path + "set_a_timer.wav"])

    profileSamples = [expected, profile1, profile2]

    actual:Profile = voiceHandler.FindBestMatch(sample, profileSamples)

    assert expected == actual

