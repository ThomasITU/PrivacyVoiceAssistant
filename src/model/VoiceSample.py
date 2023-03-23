from pydub import AudioSegment

class VoiceSample:
    
    def __init__(self, directoryPath:str, fileName:str, format = "wav"):
        self.directoryPath = directoryPath
        self.fileName = fileName
        self.format = format
        self.wav = AudioSegment.from_file(file=directoryPath+fileName,format=format)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, VoiceSample):
            # don't attempt to compare against unrelated types
            return NotImplemented
        
        return self.fileName == other.fileName and self.format == other.format and self.wav == other.wav