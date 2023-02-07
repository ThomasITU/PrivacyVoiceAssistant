# PrivacyVoiceAssistant

## steps

Create conda environment from file on a new device
```cmd
conda env create <NameEnv> --file environment.yml
```

Run as admin
```cmd
conda activate <NameEnv>
conda run python core.py
``` 

Export env
```cmd
conda env export > environment.yml 
```
