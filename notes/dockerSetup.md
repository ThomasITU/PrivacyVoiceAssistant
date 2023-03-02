# notes for docker setup 


## connect to rhasspy container through with a bash shell

```bash
sudo docker exec -it rhasspy /bin/bash
```

## "/dev/snd:/dev/snd": no directory
```bash
sudo docker run -d -p 12101:12101 \
      --name rhasspy \
      --restart unless-stopped \
      -v "$HOME/.config/rhasspy/profiles:/profiles" \
      -v "/etc/localtime:/etc/localtime:ro" \
      --device /dev/snd:/dev/snd \
      rhasspy/rhasspy \
      --user-profiles /profiles \
      --profile en
``` 

## Docker container is running rename or remove

```bash
sudo docker container start rhasspy
```

## Text to speak issues

```bash
speaker-test
```

aplay works on linux doesnt work in docker container
move wav files to test in docker - 

```bash
sudo docker cp <dir/soundfiles/> <container id>:/media
```

doesnt work in docker container 

```bash
sudo docker exec -it <container id> /bin/bash
aplay -t wav <file.wav>
```

## Error message : alsa lib unable to open slave - https://www.alsa-project.org/wiki/Asoundrc#The_.asoundrc_file_format

1. ensure /var/cache/apt/amd64/archives/partial exist if not create it cd + mkdir
2. apt-get update && apt-get install -y vim
3. create vi asound.conf /etc/asound.conf in docker container  
4. follow - https://github.com/interaction-lab/HARMONI/issues/6 
	- where hw:<card>, device, get device and card by CMD ```bash
	aplay -[l/L]```

pcm.!default {
        type plug 
        slave {
                pcm "hw:1,0"
        }
}

ctl.!default {
        type hw
        card 1
}

## Save latestCommand - 
curl --output <filename> http:<localhost><port>/<api-endpoint>
curl --output lastCommand.wav http://localhost:12101/api/play-recording


### save audio python [rhasspy community](https://community.rhasspy.org/t/how-to-save-the-last-spoken-command-to-an-audio-file-and-access-it/1184/4)

ensure <program> is executable, chmod +x <program>
## send command [rhasspy](https://rhasspy.readthedocs.io/en/latest/intent-handling/#command)
"handle": {
  "system": "command",
  "command": {
      "program": "/home/handle.sh",
      "arguments": []
  }
}

### return text in speech key : pair -> text to speech system will convey the message
{
  "speech": {
    "text": "Some text to speak."
  }
}

### Overvej at bruge [remote http hermes](https://github.com/rhasspy/rhasspy-remote-http-hermes) MQTT system

git clone https://github.com/rhasspy/rhasspy-remote-http-hermes
cd rhasspy-remote-http-hermes
./configure
make
make install


bin/rhasspy-remote-http-hermes <ARGS>

bin/rhasspy-remote-http-hermes --tts-url <TTS_URL>
http://localhost:12101/api/text-to-speech)


## copy file from container to host
docker cp <containerId>:/file/path/in/container/file /host/local/path/file