#/usr/bin/bash

./screen-stop.sh

python3 ../backup-world.py ~/amo/minecraft/world/

./screen-start.sh