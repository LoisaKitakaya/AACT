#!/bin/bash

clear

echo -e "This program allows you to do one of the following operations:\n"
echo -e "\n1. Generate code from a user provided prompt.\n2. Explain code from a user provided file.\n"

read -p "Choose between [1|2]: " operation

if [ $operation == "1" ]; then

    source ~/.AACT/.venv/bin/activate

    python3 ~/.AACT/code/write_code.py

    deactivate

    mv *.py *.js ~/Documents/AACT/codex 1> /dev/null 2>&1

elif [ $operation == "2" ]; then

    read -p "Enter file path to desired document: " filepath

    source ~/.AACT/.venv/bin/activate

    python3 ~/.AACT/code/explain_code.py $filepath

    deactivate

fi