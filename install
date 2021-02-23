echo "
╭━╮╭━╮╱╱╱╱╱╱╭╮╱╱╱╭━╮╱╱╱╱╱╱╱╱╭╮
┃┃╰╯┃┃╱╱╱╱╱╱┃┃╱╱╱┃╭╯╱╱╱╱╱╱╱╱┃┃
┃╭╮╭╮┃╭━━╮╭━╯┃╭╮╭╯╰╮╭╮╭━━╮╭━╯┃
┃┃┃┃┃┃┃╭╮┃┃╭╮┃┣┫╰╮╭╯┣┫┃┃━┫┃╭╮┃
┃┃┃┃┃┃┃╰╯┃┃╰╯┃┃┃╱┃┃╱┃┃┃┃━┫┃╰╯┃
╰╯╰╯╰╯╰━━╯╰━━╯╰╯╱╰╯╱╰╯╰━━╯╰━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱   Deployment in progress
"
echo '
        Getting Packages and Installing
'

export DEBIAN_FRONTEND=noninteractive


apt-get update;apt-get upgrade -y
apt-get install -y --no-install-recommends ffmpeg neofetch mediainfo megatools python3 python3-pip python3-dev git wget
apt-get autoremove --purge

# apt-get update && apt upgrade -y && apt-get install sudo -y
# apt-get install -y axel apt-utils bash bzip2 build-essential curl cmake coreutils espeak ffmpeg figlet gcc g++ git gifsicle imagemagick tesseract-ocr tesseract-ocr-eng libgl1 libpq-dev libffi-dev libwebp-dev libjpeg-dev libevent-dev libmagic-dev libsqlite3-dev libsqlite3-dev libreadline-dev libfreetype6-dev libcurl4-openssl-dev musl megatools mediainfo neofetch openssl procps python3 policykit-1 postgresql python3-pip python3-dev postgresql-client postgresql-server-dev-all recoverjpeg sqlite3 wget zip zipalign zlib1g-dev 

echo '
        •• Loading  Tools
'
pip3 install --upgrade pip setuptools wheel
pip3 install --upgrade pip


if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
rm -r /root/.cache
wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip && unzip opencv.zip && mv -f opencv-master /usr/bin/ && rm opencv.zip

echo '
	•• Installing
'
virtualenv -p /usr/bin/python3 venv
 . ./venv/bin/activate
git clone https://github.com/GbeshMod/modified /root/modified/
mkdir /root/modified/bin/
chmod +x /usr/local/bin/*
pip3 install -r requirements.txt
python3 -m modified
 
echo "
╭━╮╭━╮╱╱╱╱╱╱╭╮╱╱╱╭━╮╱╱╱╱╱╱╱╱╭╮
┃┃╰╯┃┃╱╱╱╱╱╱┃┃╱╱╱┃╭╯╱╱╱╱╱╱╱╱┃┃
┃╭╮╭╮┃╭━━╮╭━╯┃╭╮╭╯╰╮╭╮╭━━╮╭━╯┃
┃┃┃┃┃┃┃╭╮┃┃╭╮┃┣┫╰╮╭╯┣┫┃┃━┫┃╭╮┃
┃┃┃┃┃┃┃╰╯┃┃╰╯┃┃┃╱┃┃╱┃┃┃┃━┫┃╰╯┃
╰╯╰╯╰╯╰━━╯╰━━╯╰╯╱╰╯╱╰╯╰━━╯╰━━╯
			•°• Deployed Successfully °•°
		   •• Wait till python images are pushed...
"
