#!/bin/bash
# This runs on the production server: fetches new code,
# installs needed packages, and restarts the server.

# get new source code onto the server
git pull origin master
# activate our virtual env:
source /home/IndraABM/.virtualenvs/indra-virtualenv/bin/activate
# install all of our packages:
pip install -r requirements/requirements.txt
echo "Going to reboot the webserver"
API_TOKEN=1bd1d39b21de527564c04430402fe8eae3b2825b pa_reload_webapp.py IndraABM.pythonanywhere.com
touch reboot
