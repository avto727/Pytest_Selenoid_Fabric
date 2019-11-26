#!/usr/bin/env bash
source "./setup.sh"
rm -rf video/*
python3.8 -m venv venv3
source venv3/bin/activate
cd src
pip install --upgrade pip
pip3 install -r requirements.txt
pip install --upgrade pytest-metadata
fab -f fabfile.py execute_test:test_type=${test_type}
