#!/bin/bash

mkdir -p ~/Documents/AACT/articles

read -p "Title for article: " title

source ~/.AACT/.venv/bin/activate

python3 ~/.AACT/text/articles/simple_article.py "$title"

deactivate

mv *.txt ~/Documents/AACT/articles