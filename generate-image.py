#!/usr/bin/env python

import os
import png

RED = [255, 0, 0]
BLUE = [0, 0, 255]

def generateImage(directoryName, fileName, colour, width = 255, height = 255):
    def createImgRow():
        row = []
        for _ in range(width):
            row.extend(colour)
        return row

    img = [createImgRow() for _ in range(height)]

    if not os.path.exists(directoryName):
        os.makedirs(directoryName)
    filePath = os.path.join(directoryName, fileName)

    with open(filePath, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

# 255 x 255
generateImage('Output-255', 'red.png',  RED)
generateImage('Output-255', 'blue.png', BLUE)

# 720 ("HD") - 1280 x 720
generateImage('Output-720', 'red.png',  RED,  width=1280, height=720)
generateImage('Output-720', 'blue.png', BLUE, width=1280, height=720)

# 1080 ("Full HD") - 1920 x 1080
generateImage('Output-1080', 'red.png',  RED,  width=1920, height=1080)
generateImage('Output-1080', 'blue.png', BLUE, width=1920, height=1080)

# 2K - 2560 x 1440
generateImage('Output-2K', 'red.png',  RED,  width=2560, height=1440)
generateImage('Output-2K', 'blue.png', BLUE, width=2560, height=1440)

# 4K - 3840 x 2160
generateImage('Output-4K', 'red.png',  RED,  width=3840, height=2160)
generateImage('Output-4K', 'blue.png', BLUE, width=3840, height=2160)
