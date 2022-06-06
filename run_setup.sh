#!/bin/bash

echo "Installing Requirements"
sudo pacman -S arch-wiki-docs
pip3 install -r "pip_requirements.txt"

sudo python3 parse_txt.py

