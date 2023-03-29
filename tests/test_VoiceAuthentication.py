from os import getcwd
import sys, pytest

path = getcwd() + "/../src"
sys.path.append(path)

from services.VoiceAuthentication import VoiceAuthentication
from model.Profile import Profile
from util.Generate import Generate as _
from model.Constant import Constant
from model.PrivacyPolicy import PrivacyPolicy
from model.enumerations.Purpose import Purpose

test_path = getcwd() + "/../voiceSamples/"

def test_check_sample_given_same_voice_returns_1():

    # Arrange
    voice_handler = VoiceAuthentication()
    sample = test_path + "Hello_speechbrain.wav"

    # Act
    actual = voice_handler._check_sample(sample, [sample])

    # Assert
    assert 1 == pytest.approx(actual)


def test_find_best_match_given_different_voice_profiles_choose_best_match():

    # Arrange
    voiceHandler = VoiceAuthentication()
    sample = test_path + "What_is_lorem_ipsum.wav"

    profile1 = Profile("profile1",[], [test_path + "test.wav", test_path + "test.wav", test_path + "test.wav"])
    profile2 = Profile("profile2",[], [test_path + "der_kommer_måske_spyd_freyja.wav", test_path + "der_kommer_måske_spyd_freyja.wav", test_path + "der_kommer_måske_spyd_freyja.wav"])
    expected = Profile("Expected", [], [test_path + "Hello_speechbrain.wav", test_path + "What_is_lorem_ipsum.wav", test_path + "set_a_timer.wav"])

    profileSamples = [profile1, expected, profile2]

    # Act
    actual:Profile = voiceHandler._find_best_match(sample, profileSamples)

    # Assert
    assert expected == actual[0]

def test_get_all_profiles_returns_all_profiles():

    # Arrange
    voice_handler = VoiceAuthentication()
    old_path = Constant.DEFAULT_PROFILE_PATH 
    Constant.DEFAULT_PROFILE_PATH = f"{getcwd()}/resources/profiles/"
    voice_file_path =f"{getcwd()}/resources/voiceFiles/"
    expected_policy:list[PrivacyPolicy] = _.dummyProfile().policy
    expected_policy[0].dataCommunicationRules.dataUsageRules.add_purpose(Purpose.CALENDER)
    expected_policy[0].dataCommunicationRules.dataUsageRules.remove_purpose(Purpose.SEARCH)
    
    test1 = _path_to_profile(voice_file_path,"test1")
    test2 = _path_to_profile(voice_file_path,"test2")
    
    expected = [Profile("test1", expected_policy, sorted([test1 + "set_a_timer.wav", test1 + "Hello_speechbrain.wav", test1 + "What_is_lorem_ipsum.wav"])), 
                Profile("test2",expected_policy, sorted([test2 + "der_kommer_måske_spyd_freyja.wav", test2 + "der_kommer_spyd_freyja.wav"]))]
    expected_sorted = sorted(expected)
    
    # Act
    actual = voice_handler.get_all_profiles(Constant.DEFAULT_PROFILE_PATH)
    actual_sorted = sorted(actual)

    # Assert
    assert expected_sorted[0].name == actual_sorted[0].name
    assert expected_sorted[0].policy == actual_sorted[0].policy
    assert expected_sorted[0].voiceSamples == actual_sorted[0].voiceSamples

    assert expected_sorted[1].name == actual_sorted[1].name
    assert expected_sorted[1].policy == expected_sorted[1].policy
    assert expected_sorted[1].voiceSamples == actual_sorted[1].voiceSamples


def _path_to_profile(path:str, profile_name:str) -> str:
    return f"{path}{profile_name}/"