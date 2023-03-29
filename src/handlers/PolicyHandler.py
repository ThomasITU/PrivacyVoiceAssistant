
import sys


sys.path.append("../src/")
from util.SaveAndLoadJson import SaveAndLoadJson as _
from profile import Profile
class PolicyHandler:
    
    def __init__(self, intentDict:dict, profile:Profile):
        self.intentDict = _.loadFromJson("/home/freyja/BscProject/PrivacyVoiceAssistant/.config/profiles/sentenceshoohoo.json")
        self.profile = _.loadFromJson("/home/freyja/BscProject/PrivacyVoiceAssistant/tests/resources/userLoad.json")


    def comparePolicyWithProfile(self, intent:str):
        entities:dict = self.intentDict[intent]
        self.profile
        NotImplemented
