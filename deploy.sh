#!/bin/bash
# This shell file deploys a new version to our server.

export project_name=IndraABM

echo "SSHing to PythonAnywhere."
sshpass -p $1 ssh -o StrictHostKeyChecking=no $project_name@ssh.pythonanywhere.com << EOF
    cd ~/$project_name; ~/$project_name/rebuild.sh $2
EOF
