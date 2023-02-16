#!/bin/bash

if [ -d ~/.AACT ]; then
    echo "deleting previous version";
    rm -rv ~/.AACT;
fi

echo "Installing new version"

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

echo "Type in which shell you use."
read -p "[bash | zsh | fish]? " ushell

if [ $ushell == "bash" ]; then

    echo -e "alias 'Cassiopeia'=bash ~/.AACT/text/bot/run.sh" >> ~/.bashrc
    echo -e "alias 'simple_article'=bash ~/.AACT/text/article/run.sh" >> ~/.bashrc
    echo -e "alias 'aact --help'=bash ~/.AACT/commands.sh" >> ~/.bashrc

    source ~/.bashrc

elif [ $ushell == "zsh" ]; then

    echo -e "alias 'Cassiopeia'=bash ~/.AACT/text/bot/run.sh" >> ~/.zshrc
    echo -e "alias 'simple_article'=bash ~/.AACT/text/article/run.sh" >> ~/.zshrc
    echo -e "alias 'aact --help'=bash ~/.AACT/commands.sh" >> ~/.zshrc

    source ~/.zshrc

elif [ $ushell == "fish" ]; then

    echo -e "alias 'Cassiopeia'=bash ~/.AACT/text/bot/run.sh" >> ~/.fishrc
    echo -e "alias 'simple_article'=bash ~/.AACT/text/article/run.sh" >> ~/.fishrc
    echo -e "alias 'aact --help'=bash ~/.AACT/commands.sh" >> ~/.fishrc

    source ~/.fishrc

fi

clear

echo "Installation complete."

echo "\nTo view AACT commands, run the following command:\n'aact --help'"