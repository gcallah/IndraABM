#!/bin/bash
# This runs on the production server: fetches new code,
# installs needed packages, and restarts the server.

# get new source code onto the server
git pull origin master
# activate our virtual env:
source /home/IndraABM/.virtualenvs/indra-virtualenv/bin/activate
# install all of our packages:
pip install -r docker/requirements.txt
echo "Going to reboot the webserver"
API_TOKEN=$api_token pa_reload_webapp.py IndraABM.pythonanywhere.com
touch reboot
