#!/bin/bash
cd 22.SUM.17-IR-Portfolio-Website
git fetch && git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build