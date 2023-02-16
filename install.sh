#!/bin/bash

if [ -d ~/.AACT ]; then
    echo "deleting previous version";
    rm -r ~/.AACT;
fi

echo -e "\nInstalling new version\n"

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

    echo -e "alias Cassiopeia='bash ~/.AACT/text/bot/run.sh'" >> ~/.bashrc
    echo -e "alias simple_article='bash ~/.AACT/text/article/run.sh'" >> ~/.bashrc
    echo -e "alias aact_commands='bash ~/.AACT/commands.sh'" >> ~/.bashrc

    clear

    echo "Installation complete."
    echo -e "\n1. To activate AACT commands, type & run the following command: 'source ~/.bashrc'"

elif [ $ushell == "zsh" ]; then

    echo -e "alias Cassiopeia='bash ~/.AACT/text/bot/run.sh'" >> ~/.zshrc
    echo -e "alias simple_article'='bash ~/.AACT/text/article/run.sh'" >> ~/.zshrc
    echo -e "alias aact_commands='bash ~/.AACT/commands.sh'" >> ~/.zshrc

    clear

    echo "Installation complete."
    echo -e "\n1. To activate AACT commands, type & run the following command: 'source ~/.zshrc'"

elif [ $ushell == "fish" ]; then

    echo -e "alias Cassiopeia='bash ~/.AACT/text/bot/run.sh'" >> ~/.fishrc
    echo -e "alias simple_article='bash ~/.AACT/text/article/run.sh'" >> ~/.fishrc
    echo -e "alias aact_commands='bash ~/.AACT/commands.sh'" >> ~/.fishrc

    clear

    echo "Installation complete."
    echo -e "\n1. To activate AACT commands, type & run the following command: 'source ~/.fishrc'"

fi

echo -e "\n2. To view AACT commands, type & run the following command: 'aact_commands'\n"