#!/bin/bash
node reddit.js &
python3 twitch.py &
while :
do
python3 main.py
done

