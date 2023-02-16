#!/bin/bash

read -p "Title for article: " title

source ~/.AACT/.venv/bin/activate

python3 ~/.AACT/text/articles/simple_article.py "$title"

deactivate

mkdir -p ~/Documents/AACT/articles

mv *.txt ~/Documents/AACT/articles