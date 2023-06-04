#!/usr/bin/env python

import os
import png
import subprocess

OUTPUT_DIR = 'Output'

RED = [255, 0, 0]
BLUE = [0, 0, 255]

def generateImage(filePath, colour, width = 255, height = 255):
    def createImgRow():
        row = []
        for _ in range(width):
            row.extend(colour)
        return row

    img = [createImgRow() for _ in range(height)]

    with open(filePath, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)


def generate(name, size):
    dirName = os.path.join(OUTPUT_DIR, name)
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    redFilePath  = os.path.join(dirName, 'red')
    blueFilePath = os.path.join(dirName, 'blue')

    print('## Generating', name, 'images and video')

    generateImage(redFilePath  + '.png', RED,  width=size[0], height=size[1])
    generateImage(blueFilePath + '.png', BLUE, width=size[0], height=size[1])

    subprocess.check_call(['ffmpeg', '-hide_banner', '-loglevel', 'warning', '-stats', '-y', '-loop', '1', '-i', redFilePath  + '.png', '-c:v', 'libx264', '-t', '60', redFilePath  + '.mp4'])
    subprocess.check_call(['ffmpeg', '-hide_banner', '-loglevel', 'warning', '-stats', '-y', '-loop', '1', '-i', blueFilePath + '.png', '-c:v', 'libx264', '-t', '60', blueFilePath + '.mp4'])

    print('')


generate('255',  [ 255,  255])
generate('720',  [1280,  720])
generate('1080', [1920, 1080])
generate('2K',   [2560, 1440])
generate('4K',   [3840, 2160])
