#/usr/bin/bash

#send a stop command to the mc screen session
screen -S amo -p 0 -X stuff "stop^M"