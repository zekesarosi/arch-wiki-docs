#!/bin/bash

echo "Installing Requirements"
sudo pacman -S arch-wiki-docs
pip install -r "scripts/pip_requirements.txt"

sudo python3 scripts/parse_txt.py

