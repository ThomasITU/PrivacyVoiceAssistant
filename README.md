# PrivacyVoiceAssistant

## pre-requesites

- Linux machine
- Docker engine installed
- Microphone, Speaker and Bluetooth device
- Python 3.10 

## How to run on linux

Ensure docker compose is installed

### Only intial setup (Reinstall scripts)  

From root

```sh
cd .devcontainer
docker compose up 
```

### After initial setup
```sh
docker compose start
```

Open the docker container with an interactive terminal and install dependicies using the script

```sh
docker exec -it rhasspy /bin/bash
source /privacyVoiceAssistant/scripts/SetupDependencies.sh
```

Check the localhost [settings](http://localhost:12101/settings#microphone)
- Microphone is picked up 
    - ![pyaudio](/notes/images/Pyaudio_Microphone.png)

- Speaker can output sound using the speech-to-text  
    - ![speaker](/notes/images/speaker_audio.png)

### test speaker config

```sh
docker exec -it rhasspy /bin/bash
speaker-test 
```

### In case of error aplay / ALSA error modify the etc/asound.conf file 

```sh 
aplay -l
```

find the sound card device file <expand later>

### If Playback open error: -16,Device or resource busy

```sh
lsof | grep snd
```

Look for pulseaudi process id's

```sh
kill <PID>
```



### In case of microphone not being picked up 

```sh
```



## how to run test 

```sh
cd test
pytest 
```

```sh
cd test
pytest <test_file.py>
```

Be aware some of the Voice assistant test will fail as the paths for profiles voice samples paths are based on the system created at.   