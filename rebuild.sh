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
API_TOKEN=830cfdea135023dfc162d0986700b6d1f4ac9dfd pa_reload_webapp.py IndraABM.pythonanywhere.com
touch reboot
