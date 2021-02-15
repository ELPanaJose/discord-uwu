#!/bin/bash
clear
python3 twitch.py &
node reddit.js &
while :
do
python3 main.py 
done
