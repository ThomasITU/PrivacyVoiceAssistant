from typing import Final

class Constant:
    LAST_VOICE_COMMAND_ENDPOINT: Final[str] = "http://localhost:12101/api/play-recording"
    VOICE_PATH: Final[str] = "/tmp/voiceFiles/"
    INTENT_PATH: Final[str] = "/tmp/intents/"
    DEFAULT_PROFILE_PATH: Final[str] = "/privacyVoiceAssistant/resources/profiles/"
    BLUETOOTH_BUFFER_SIZE: Final[int] = 1024
    PROFILE_AUTHENTICATION_THRESHOLD: Final[float] = 0.0005
    INI_FILE_PATH: Final[str] = "/profiles/en/sentences.ini"
    SPEECHBRAIN_PATH: Final[str] = "/privacyVoiceAssistant/lib/speechbrain"
    LOGGING_PATH: Final[str] = "/tmp/debug.log"
    TEMP_PATH: Final[str] = "/tmp/voiceModels"