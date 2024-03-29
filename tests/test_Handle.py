import io
import json
import os
import sys
from os import getcwd
import time
import filetype

sys.path.append(getcwd() + "/../src/")
from handlers.handle import get_intent, voice_assistant_speech, save_intent_to_file, save_voice_file
from model.Constant import Constant
from util.SaveAndLoad import SaveAndLoad



def test_voice_assistant_speech_given_hello_prints_dictionary_to_stdout(capsys):
    
    # Arrange
    text = "hello"
    expected_dict = dict()
    expected_dict["speech"] = {"text": text}
    expected_output = json.dumps(expected_dict)

    # Act
    voice_assistant_speech(text)
    captured = capsys.readouterr()
    actual = str(captured.out).removesuffix("\n")

    # Assert
    assert actual == expected_output

def test_save_intent_given_intent_and_file_name_saves_file_as_txt():

    # Arrange
    old_path = Constant.INTENT_PATH
    path = f"{getcwd()}/resources/intents/"
    Constant.INTENT_PATH = path
    file_name = "101testXYZ"
    expected_file_name = f"{path}{file_name}.json"
    expected_intent = "GetTime"

    # Act
    save_intent_to_file(expected_intent, f"{path}{file_name}.wav")
    is_file = os.path.isfile(expected_file_name)
    Constant.INTENT_PATH = old_path
    if(is_file):
        actual_intent = SaveAndLoad.load_from_json(expected_file_name)
        os.remove(expected_file_name)

    # Assert
    assert True == is_file
    assert False == os.path.isfile(expected_file_name)
    assert actual_intent == expected_intent


def test_get_intent_reads_stdin_and_returns_intent(monkeypatch):
    
    # Arrange
    expected_intent = "GetTime"
    _print_to_stdin(monkeypatch)

    # Act
    actual = get_intent()

    # Assert
    assert actual == expected_intent

# only asserts true if voice assistant is running
def test_save_voice_file_saves_file_and_returns_file_name():

    # Arrange
    old_path = Constant.VOICE_PATH 
    Constant.VOICE_PATH = f"{getcwd()}/resources/voiceFiles/"
    path = Constant.VOICE_PATH

    # Act
    actual = save_voice_file(path)
    actual_path = path + actual
    time.sleep(2.5)
    is_file = os.path.isfile(actual_path)
    if(is_file):
        actual_file_info = filetype.guess(actual_path)
        time.sleep(1)
        os.remove(actual_path)
    Constant.VOICE_PATH = old_path

    # Assert
    assert isinstance(actual,str)
    assert len(actual) > 5
    assert True == is_file
    assert False == os.path.isfile(actual_path)
    assert actual_file_info.EXTENSION == 'wav' 
    assert actual_file_info.MIME == 'audio/x-wav'


# helper methods
def _print_to_stdin(monkeypatch):
    intent = _open_json(f"{getcwd()}/resources/IntentTest.json")
    monkeypatch.setattr('sys.stdin', io.StringIO(json.dumps(intent)))

def _open_json(path:str):
    with open(path) as json_file:
        intent = json.load(json_file)
    return intent