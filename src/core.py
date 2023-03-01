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

    templateVoice, fs = torchaudio.load("VoiceSamples/Hello_speechbrain.wav")
    sameVoice, fs = torchaudio.load("VoiceSamples/What_is_lorem_ipsum.wav")
    # testVoice, fs = torchaudio.load("VoiceSamples/der_kommer_spyd.flac")
    testVoice, fs = torchaudio.load("VoiceSamples/test.wav")
    print(fs)
    freyjaSpyd, fs = torchaudio.load("VoiceSamples/der_kommer_spyd_freyja.wav")
    freyjaMaybeSpyd, fs = torchaudio.load("VoiceSamples/der_kommer_måske_spyd_freyja.wav")

    
    print("Same template voice file")
    score, prediction = verification.verify_batch(templateVoice, templateVoice)
    print(prediction, score)

    print("Template and same Voice")
    score, prediction = verification.verify_batch(templateVoice, sameVoice)
    print(prediction, score)

    print("different voice files")
    score, prediction = verification.verify_batch(templateVoice, testVoice)
    print(prediction, score)

    print("freyja time")
    score, prediction = verification.verify_batch(freyjaSpyd, freyjaMaybeSpyd)
    print(prediction, score)
     
test()
