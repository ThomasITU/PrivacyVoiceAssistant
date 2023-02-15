ARG DEBIAN_FRONTEND=noninteractive
FROM python:3.8-slim-buster

WORKDIR src/
RUN git config --global core.autocrlf false

COPY . .

# install bash and dos2unix 
RUN sudo apt-get update && sudo apt-get -y install bash &&\
    sudo apt-get install -y dos2unix &&\
    sudo apt install python3-pip &&\

# install python
# run sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev &&\
#     wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz &&\
#     tar -xvf Python-3.10.0.tgz &&\
#     cd Python-3.10.0 &&\
#     sudo ./configure --enable-optimizations &&\
#     export core=$(nproc) &&\
#     sudo make -j $core &&\
#     sudo make altinstall &&\
#     python3.10 --version 

RUN bash dev_setup.sh\
# get expect package and script expect 
# bash dev_setup.sh\
# cd /workspaces/PrivacyVoiceAssistant/mycroft-core/.venv/bin/python3


# dos2unix dev_setup.sh, start, stop, install-mimic.sh