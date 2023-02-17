import time
from functools import wraps
import gc

import speechbrain as sb
from IPython.display import Audio
from speechbrain.pretrained import SpeakerRecognition
import torchaudio
from tempfile import mkdtemp


#main function
class VoiceAuthentication:

    def __init__(self) :
        self.tmpdir = mkdtemp("tmpdir")
        self.speakerRecognition = SpeakerRecognition.from_hparams(
            source="speechbrain/spkrec-ecapa-voxceleb",
            savedir=self.tmpdir,
        )
        
    def GenerateScoreArray(self, voiceSample:str, profileSamples:list[str]):
        sampleVoiceLoaded, _ = torchaudio.load(voiceSample)
        scoreArray = []
        for sample in profileSamples:
            sampleLoaded, _ = torchaudio.load(sample)
            score, _ = self.speakerRecognition.verify_batch(sampleLoaded, sampleVoiceLoaded)
            certainty = score[0].item()
            # print(f"certainty: {certainty}")
            scoreArray.append(certainty)
        return scoreArray
voiceHandler = VoiceAuthentication()


def timeit(func):
    gc.disable()
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_counter_ns = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_counter_ns = time.perf_counter_ns()
        total_time = (end_counter_ns - start_counter_ns)/10**9
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    gc.enable()
    return timeit_wrapper


@timeit
def test(voiceSample:str, voiceHandler:VoiceAuthentication, profileSamples:list[str]):
    scoreArray = voiceHandler.GenerateScoreArray(voiceSample, profileSamples)
    print(f"score array:{scoreArray}")
    print(f"average: {sum(scoreArray)/len(scoreArray)}\n")


input("Press enter to start")
if __name__ == '__main__':
    profileSamples = ["VoiceSamples/Hello_speechbrain.wav", "VoiceSamples/Hello_speechbrain.wav","VoiceSamples/What_is_lorem_ipsum.wav" ]
    test("VoiceSamples/What_is_lorem_ipsum.wav", voiceHandler, profileSamples)

    profileSamples2 = ["VoiceSamples/test.wav"]          
    test("VoiceSamples/What_is_lorem_ipsum.wav", voiceHandler, profileSamples2)