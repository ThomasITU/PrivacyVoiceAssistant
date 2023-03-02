#!/usr/bin/env bash

# Available environment variables
# -------------------------------
# Base directory of Rhasspy: ${RHASSPY_BASE_DIR}
# Name of current profile: ${RHASSPY_PROFILE}
# Profile directory: ${RHASSPY_PROFILE_DIR}

# Output should be JSON
cat >> /tmp/intentCat.json

path="/tmp/voiceFiles/"
curl --output ${path}lastCommand.wav http://localhost:12101/api/play-recording


echo "{
	"speech": {
		"text": "Saved file at ${path}lastCommand.wav"
 	 }
}"
