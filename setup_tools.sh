#!/usr/bin/env bash
read -p "run: sudo apt-get update (y/n)?" CONT
if [ "$CONT" = "y" ]; then
    sudo apt-get update
fi
sudo apt install firefox-geckodriver
# Install python3.9
echo ""
echo "-> PYTHON3.9 DOWNLOAD TAKES A WHILE...(Don't worry)"
read -p "Download python3.9 (y/n)?" CONT
if [ "$CONT" = "y" ]; then
    wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz
    tar -xf Python-3.9.0.tar.xz
    cd Python-3.9.0
    ./configure
    sudo make altinstall
fi
--------------------
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install --user pipenv
pip3 install python-dateutil
pip3 install selenium
pip3 install firebase-admin
pip3 install ofxtools
pip3 install boto3
pip3 install pynubank
# Clean
if [[ -d Python-3.9.0 || -f Python-3.9.0.tar.xz || -f get-pip.py ]]; then
    echo "Download Completed (JUNK FILES EXIST)"
    sudo rm -rf Python-3.9.0
    sudo rm -rf Python-3.9.0.tar.xz
    rm get-pip.py
    echo "JUNK FILES DELETED"
else
    echo "NO JUNK FILES TO DELETE"
fi
