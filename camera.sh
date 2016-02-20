#!/bin/bash

echo 'Say cheese !'
DATE=$(date +"%Y-%m-%d_%H%M%S")

raspistill -vf -hf -o $DATE.jpg

echo 'Done mofos!'
