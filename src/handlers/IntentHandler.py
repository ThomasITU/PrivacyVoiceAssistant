import datetime
import random
from model.Intent import Intent

class IntentHandler:

    def handle_intent(self, intent:str):
        match intent:
            case "Hello":
                return _hello()
            case "LongSentence":
                return _long_sentence()
            case "GetTime":
                return _get_time()
            case _:
                return f"Currently we cannot provide {intent} as it is not implemented yet"


def _get_time() -> str:
    now = datetime.datetime.now()
    return "It's %s %d %s." % (now.strftime('%H'), now.minute, now.strftime('%p'))

def _long_sentence() -> str:
    return "This is a very long sentence"

def _hello() -> str:
    replies = ['Hi!', 'Hello!', 'Hey there!', 'Greetings.']
    return random.choice(replies)
               
