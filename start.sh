#!/bin/bash
while :
do
node reddit.js & python3 main.py & python3 twitch.py
done


