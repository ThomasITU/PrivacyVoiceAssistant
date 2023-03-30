import datetime
import sys
from os import getcwd

sys.path.append(getcwd() + "/../src/")
from handlers.IntentHandler import IntentHandler


def test_handle_intent_given_LongSentence_returns_string():
    
    # Arrange
    expected = "This is a very long sentence"

    # Act
    actual = IntentHandler.handle_intent(any,"LongSentence")

    # Assert
    assert actual == expected


def test_handle_intent_given_GetTime_returns_time():
    
    # Arrange
    now = datetime.datetime.now()
    expected = f"It's {now.strftime('%H')} {now.minute} {now.strftime('%p')}."

    # Act
    actual = IntentHandler.handle_intent(any,"GetTime")

    # Assert
    assert actual == expected

def test_handle_intent_given_non_existing_intent_returns_response():
    
    # Arrange
    expected = "Currently we cannot provide NonExistingIntent as it is not implemented yet"

    # Act
    actual = IntentHandler.handle_intent(any,"NonExistingIntent")

    # Assert
    assert actual == expected
