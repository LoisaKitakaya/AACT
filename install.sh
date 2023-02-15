#!/bin/bash

sudo rm -r /usr/local/share/AACT

sudo mkdir -p /usr/local/share/AACT
sudo mkdir -p ~/Documents/AACT

sudo cp requirementes.txt /usr/local/share/AACT

sudo cp -rv *[^.] /usr/local/share/AACT

sudo cd /usr/local/share/AACT

sudo python3 -m venv .venv
sudo source .venv/bin/activate
sudo pip install --upgrade pip
sudo pip install -r -U requirements.txt
deactivate

sudo rm requirements.txt

cd -

mkdir -p ~/Documents/AACT

clear

echo "Installation complete."