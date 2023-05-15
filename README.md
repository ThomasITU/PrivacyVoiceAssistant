# Privacy Voice Assistant

## Pre-requesites

- Linux operative system
- Docker engine
- Microphone, Speaker and Bluetooth device
- Python 3.10 

## How to run on a Linux system

Ensure docker compose is installed

### Only intial setup (Reinstall scripts)  

From repository root

```sh
cd .devcontainer
docker compose up 
```

Open the docker container with an interactive terminal and install dependencies using the following script.

```sh
docker exec -it rhasspy /bin/bash
source /privacyVoiceAssistant/scripts/SetupDependencies.sh
```

### After initial setup

```sh
docker compose start
```

Access the [web interface](http://localhost:12101/settings#microphone) 
- Microphone is picked up 
    ![pyaudio](/notes/images/Pyaudio_Microphone.png)

- Speaker can output sound using the speech-to-text  
    ![speaker](/notes/images/speaker_audio.png)

### Test speaker config

```sh
docker exec -it rhasspy /bin/bash
speaker-test 
```

### In case of error aplay / ALSA error modify the etc/asound.conf file 

```sh 
aplay -l
```

Find your sound card device and adjust the etc/asound.conf file 

### If Playback open error: -16,Device or resource busy

```sh
lsof | grep snd
```

Look for pulseaudi process id's

```sh
kill <PID>
```


### In case of microphone not being picked up 

Use the Rhasspy's [webinterface](http://localhost:12101/settings#microphone) and use the test feature, look for working mic or the (*) next to the devices 

If this doesn't work look for potential PID's and apply the kill  

```sh
fuser -v /dev/snd/*
```

### When the voice assistant is running 

Try to activate the voice assistant with the hotword "Blueberry" followed by "What's the time" look into ***.config/profiles/sentences.ini*** for other sentences.

Use the ***/src/handlers/LoadProfile.py*** class to adjust PrivacyPolicies for the files located in ***/resources/profiles*** also adjust the voice files.   



### To stop the container

```sh
docker compose stop
```


## Bluetooth communication

Firstly ensure the bluetooth device is setup look at the [notes](/notes/Bluetooth.md) or execute this script. 

```sh
source .devcontainer/scripts/SetupBluetooth.sh
```

### To run the Bluetooth server

```sh
cd /src/services
python3.10 BluethoothServer.py   
```

If this fails try look revisit the [notes](/notes/Bluetooth.md) or google.

### To run the Bluetooth Client

```sh
cd /src/services
python3.10 BluethoothClient.py  
```

Respond to the prompts and provide the MAC address of the Bluetooth Server for biggest chance of success.
![Bluetoothclient](/notes/images/BluetoothClient.png)

The profile send is a dummy profile, to change the profile being sent, look at BluetoothClient.py line 47.

### Also be aware the BluetoothClient doesn't send voice files 

## How to run test 

```sh
cd test
pytest 
```

```sh
cd test
pytest <test_file.py>
```

Be aware some of the Voice assistant test will fail as the paths for profiles voice samples paths are based on the system created at.  
