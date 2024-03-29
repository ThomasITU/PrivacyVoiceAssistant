import sys
import datetime
import random
sys.path.append("/privacyVoiceAssistant/src")
sys.path.append("../src/")

class IntentHandler:

    def handle_intent(self, intent:str):
        try:
            match intent:
                case "Hello":
                    return _hello()
                case "LongSentence":
                    return _long_sentence()
                case "GetTime":
                    return _get_time()
                case "GetTemperature":
                    return _get_temperature()
                case _:
                    return f"Currently we cannot provide {intent} as it is not implemented yet"
        except Exception as _:
            return "Sorry, something went wrong"

def _get_time() -> str:
    now = datetime.datetime.now()
    return "It's %s %d %s." % (now.strftime('%H'), now.minute, now.strftime('%p'))

def _long_sentence() -> str:
    return "This is a very long sentence"

def _hello() -> str:
    replies = ['Hi!', 'Hello!', 'Hey there!', 'Greetings.']
    return random.choice(replies)
               
def _get_temperature() -> str:
    return "It is 20 degrees Celsius"