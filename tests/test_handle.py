import json
import sys
from os import getcwd
sys.path.append(getcwd() + "/../src/")
from handlers.handle import voice_assistant_speech


def test_voice_assistant_speech_given_hello_prints_dictionary_to_stdout(capsys):
    
    # Arrange
    text = "hello"
    expectedDict = dict()
    expectedDict["speech"] = {"text": text}
    expectedOutput = json.dumps(expectedDict)

    # Act
    voice_assistant_speech(text)
    captured = capsys.readouterr()
    actual = str(captured.out).removesuffix("\n")

    # Assert
    assert actual == expectedOutput

def test_get_intent_reads_stdin_and_returns_intent(capsys):
    NotImplemented

def test_get_intent_given_file_name_saves_intent(capsys):
    NotImplemented