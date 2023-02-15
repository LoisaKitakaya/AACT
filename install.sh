#!/bin/bash

if [ -d ~/.AACT ]; then
    rm -rv ~/.AACT;
fi

mkdir -pv ~/.AACT
mkdir -pv ~/Documents/AACT

cp -rv * ~/.AACT

rm ~/.AACT/LICENSE
rm ~/.AACT/install.sh
rm ~/.AACT/README.md

cd ~/.AACT

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

deactivate

cd -

clear

echo "Installation complete."