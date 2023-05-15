#!/usr/bin/env bash



echo "creating directories"
source /privacyVoiceAssistant/scripts/createDirectories.sh

echo "installing python"
source /privacyVoiceAssistant/scripts/InstallPython.sh


chmod +x /privacyVoiceAssistant/src/handlers/handle.py


# echo "setting up bluetooth"
# source /privacyVoiceAssistant/scripts/SetupBluetooth.sh