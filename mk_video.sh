#!/bin/sh

ffmpeg -loop 1 -i red.png  -c:v libx264 -t 60 red.mp4
ffmpeg -loop 1 -i blue.png -c:v libx264 -t 60 blue.mp4
