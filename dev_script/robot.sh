#!/usr/bin/env bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ..
venv_file="venv/bin/activate"
if ! [ -e "$venv_file" ]
then
    RED='\033[0;31m'
    NC='\033[0m'
    echo -e "${RED}Python venv not configured${NC}"
    echo "Configure venv..."
    virtualenv venv
fi
source "$venv_file"
echo "Installing requirements..."
pip install -r requirements.txt
python stack_login.py >> log.txt