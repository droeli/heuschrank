#!/usr/bin/bash

sudo cp heuschrank.service /etc/systemd/system/heuschrank.service 
sudo systemctl daemon-reload
sudo systemctl enable heuschrank
sudo systemctl start heuschrank
