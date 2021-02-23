FROM kalilinux/kali-rolling
ARG DEBIAN_FRONTEND=noninteractive
ENV TERM xterm-256color
RUN apt-get update && apt upgrade -y && apt-get install sudo -y

RUN apt-get install -y axel apt-utils bash bzip2 build-essential curl cmake coreutils espeak ffmpeg figlet gcc g++ git gifsicle imagemagick tesseract-ocr tesseract-ocr-eng libgl1 libpq-dev libffi-dev libwebp-dev libjpeg-dev libevent-dev libmagic-dev libsqlite3-dev libsqlite3-dev libreadline-dev libfreetype6-dev libcurl4-openssl-dev musl megatools mediainfo neofetch openssl procps python3 policykit-1 postgresql python3-pip python3-dev postgresql-client postgresql-server-dev-all recoverjpeg sqlite3 wget zip zipalign zlib1g-dev 


RUN apt-get autoremove --purge
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --upgrade pip
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb
RUN wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv -f chromedriver /usr/bin/ && rm chromedriver_linux64.zip
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip && unzip opencv.zip && mv -f opencv-master /usr/bin/ && rm opencv.zip
RUN git clone https://github.com/GbeshMod/modified /root/modified
RUN mkdir /root/modified/bin/
WORKDIR /root/modified/
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt
CMD ["python3","-m","modified"]
