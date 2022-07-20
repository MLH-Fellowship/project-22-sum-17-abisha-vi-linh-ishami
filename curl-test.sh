#!/bin/bash

curl -X POST http://localhost:5000/api/timeline_post -d 'name=Ishami&email=ishami.test@mlh.io&content=Testing my endpoints with a bash script.'

curl http://localhost:5000/api/timeline_post