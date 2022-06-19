#!/bin/bash
tmux attach -d
cd 22.SUM.17-IR-Portfolio-Website
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new | cd app | export FLASK_APP=__init__.py | flask run --host=0.0.0.0