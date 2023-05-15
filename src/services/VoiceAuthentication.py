import os
import sys
sys.path.append("/privacyVoiceAssistant/src")
from model.Constant import Constant
sys.path.append(Constant.SPEECHBRAIN_PATH)
import torchaudio
from speechbrain.pretrained import SpeakerRecognition
from tempfile import mkdtemp


from model.Profile import Profile
from util.SaveAndLoad import SaveAndLoad   


class VoiceAuthentication:

    def __init__(self):
        self.tmp_dir = mkdtemp("tmpdir", dir=Constant.TEMP_PATH)
        self.speaker_recognition = SpeakerRecognition.from_hparams(
            source="speechbrain/spkrec-ecapa-voxceleb",
            savedir=self.tmp_dir,
        )
        
    def find_best_match_above_threshold(self, voice_sample:str, threshold=Constant.PROFILE_AUTHENTICATION_THRESHOLD):
        profiles = self.get_all_profiles()
        best_match = self._find_best_match(voice_sample, profiles)
        if (best_match[1] >= threshold):
            return best_match
        return None
    
    def _find_best_match(self, voice_sample:str, profiles:list[Profile]) -> tuple[Profile, float]:
        score_array = []
        for profile in profiles:
            score_array.append(self._check_sample(voice_sample, profile.voiceSamples))
        best_match = profiles[score_array.index(max(score_array))]
        return (best_match, max(score_array))

    def _check_sample(self, voice_sample:str, profile_samples:list[str]):
        score_array = self.generate_score_array(voice_sample, profile_samples)
        average = sum(score_array)/len(score_array)
        return average

    def generate_score_array(self, voice_file:str, profile_samples:list[str]):
        if (os.path.exists(voice_file) == False):
            raise Exception("File does not exist")
        voice_file, _ = torchaudio.load(voice_file, format="wav")
        score_array = []
        for file_path in profile_samples:
            sample_file, _ = torchaudio.load(file_path, format="wav")
            score, _ = self.speaker_recognition.verify_batch(sample_file, voice_file)
            score_array.append(score[0].item())
        return score_array

    def get_all_profiles(self, path = Constant.DEFAULT_PROFILE_PATH) -> list[Profile]:
        profiles:list[Profile] = []
        for file in os.listdir(path):
            if file.endswith(".json"):
                profile:Profile = SaveAndLoad.load_from_json(path+file)
                profiles.append(profile)  
        return profiles