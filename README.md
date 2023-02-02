# PrivacyVoiceAssistant

## steps

Create conda environment on a new device
```cmd
conda env create <NameEnv> --file speechbrain.yml
```

Run as admin
```cmd
conda activate <NameEnv>
conda run python core.py
``` 

Export env
```cmd
conda env export > speechbrain.yml 
```
