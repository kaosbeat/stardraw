#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cp fragments.service /etc/systemd/system/


systemctl daemon-reload
systemctl enable fragments.service

