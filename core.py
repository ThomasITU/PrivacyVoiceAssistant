import speechbrain as sb
from IPython.display import Audio
from speechbrain.pretrained import SpeakerRecognition
import torchaudio
from tempfile import mkdtemp


#main function
def test():
    tmpdir = mkdtemp("tmpdir")

    verification = SpeakerRecognition.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        savedir=tmpdir,
    )

    defaultVoice, fs = torchaudio.load("VoiceSamples/Hello_speechbrain.wav")
    sameVoice, fs = torchaudio.load("VoiceSamples/What_is_lorem_ipsum.wav")
    # testVoice, fs = torchaudio.load("VoiceSamples/der_kommer_spyd.flac")
    testVoice, fs = torchaudio.load("VoiceSamples/test.wav")


    
    print("Default Voice")
    score, prediction = verification.verify_batch(defaultVoice, defaultVoice)
    print(prediction, score)

    print("Default and Same Voice")
    score, prediction = verification.verify_batch(defaultVoice, sameVoice)
    print(prediction, score)

    print("different voice")
    score, prediction = verification.verify_batch(defaultVoice, testVoice)
    print(prediction, score)
     
test()
