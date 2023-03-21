# PrivacyVoiceAssistant

## how to run on linux

Ensure docker compose is installed

```sh
docker compose up
```

Check the localhost [settings](http://localhost:12101/settings)


### test speaker config

```sh
docker exec -it rhasspy /bin/bash
speaker-test 
```

### In case of error aplay / ALSA error modify the etc/asound.conf file 

```bash 
aplay -l
```
find the sound card device file <expand later>



## how to run test 

```sh
cd test
pytest 
```

```sh
cd test
pytest <test_file.py>
```