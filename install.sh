#!/bin/bash
sudo apt-get install r-base sqlite apache2 apache2-doc apache2-utils python2 python-pip curl
echo 'install.packages("RSQLite")' | sudo R --vanilla
pip install requests
pip install gtfs-realtime-bindings protobuf
