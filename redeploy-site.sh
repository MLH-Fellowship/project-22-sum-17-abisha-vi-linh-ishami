#!/bin/bash
cd 22.SUM.17-IR-Portfolio-Website
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
systemctl daemon-reload
systemctl restart myportfolio