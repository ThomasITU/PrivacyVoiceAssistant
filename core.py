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


    
    print("Same template voice file")
    score, prediction = verification.verify_batch(templateVoice, templateVoice)
    print(prediction, score)

    print("Template and same Voice")
    score, prediction = verification.verify_batch(templateVoice, sameVoice)
    print(prediction, score)

    print("different voice files")
    score, prediction = verification.verify_batch(templateVoice, testVoice)
    print(prediction, score)
     
test()
