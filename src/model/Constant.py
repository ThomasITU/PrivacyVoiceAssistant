from typing import Final

class Constant:
    LAST_VOICE_COMMAND_ENDPOINT: Final[str] = "http://localhost:12101/api/play-recording"
    VOICE_PATH: Final[str] = "/tmp/voiceFiles/"
    INTENT_PATH: Final[str] = "/tmp/intents/"
    DEFAULT_PROFILE_PATH: Final[str] = "/PivacyVoiceAssistant/resources/profiles/"
    BLUETOOTH_BUFFER_SIZE: Final[int] = 1024
    PROFILE_AUTHENTICATION_THRESHOLD: Final[float] = 0.75