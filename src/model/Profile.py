from model.PrivacyPolicy import PrivacyPolicy
from model.VoiceSample import VoiceSample
from pydub import AudioSegment


class Profile:

    def __init__(self, name:str, policy:list[PrivacyPolicy], voiceSamples:list[str], wavObjects:list[VoiceSample]):
        self.name = name
        self.policy = policy
        self.voiceSamples = voiceSamples
        self.wavObjects = wavObjects
        
    def __eq__(self, other): 
        if not isinstance(other, Profile):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name and self.voiceSamples == other.voiceSamples and self.policy == other.policy 

    def __str__(self) -> str:
        policies = ""
        for policy in self.policy:
            policies += "\t"+policy.__str__() + "\n"
        return f"Profilname: {self.name}, voice files: {self.voiceSamples}, Policy's:\n{policies}"

    def __hash__(self) -> int:
        return super(Profile, self).__hash__()