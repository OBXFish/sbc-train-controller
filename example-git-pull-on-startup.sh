#!/usr/bin/env bash
#
# Run this script every time the system boots.
# vim /etc/init.d/train-control-update.sh
# chmod 755 /etc/init.d/train-control-update.sh
# sudo update-rc.d train-control-update.sh defaults

GITHUB_TOKEN=''
GITHUB_USER=''
PROJECT='train-control'

# Check out the latest code
cd ~/workspace/scratch/
rm -rf ~/workspace/scratch/train-control/
git clone https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/pivotalservices/${PROJECT}


# Run the latest code
cd ~/workspace/scratch/train-control/
python ./BootLoader.py


