#!/usr/bin/env bash
sudo apt-get update
sudo apt install firefox-geckodriver
sudo apt-get update python3.7.5
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install --user pipenv
pip3 install python-dateutil
pip3 install selenium
pip3 install firebase-admin
pip3 install ofxtools
pip3 install boto3
