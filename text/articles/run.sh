#!/bin/bash

clear

read -p "Title for article: " title

source ~/.AACT/.venv/bin/activate

python3 ~/.AACT/text/articles/simple_article.py "$title"

deactivate

mv *.txt ~/Documents/AACT/articles 1> /dev/null 2>&1