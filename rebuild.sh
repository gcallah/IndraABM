#!/bin/bash
# This runs on the production server: fetches new code,
# installs needed packages, and restarts the server.

export project_name=IndraABM

# get new source code onto the server
git pull origin master
# activate our virtual env:
source /home/project_name/.virtualenvs/indra-virtualenv/bin/activate
# install all of our packages:
pip install -r docker/requirements.txt
echo "Going to reboot the webserver"
API_TOKEN=$pa_pwd pa_reload_webapp.py project_name.pythonanywhere.com
touch reboot
