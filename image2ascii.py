#!/usr/bin/python3
"""
image2ascii.py -- image to ASCII art in the terminal
More info: https://massimo-nazaria.github.io/ascii-art.html
"""

import os
import sys
import argparse
from PIL import Image

# ascii character palette (assumes dark terminal)
PALETTE = " .,'-:/|%@#"

parser = argparse.ArgumentParser(description="image to ASCII art in the terminal")
# of course an input image must be provided
parser.add_argument("image", help="input image file", type=str)
args = parser.parse_args()

# open image in grayscale mode
image = Image.open(args.image).convert("L")

# image size (width, height)
iw, ih = image.size
# terminal size (width, height)
tw, th = os.get_terminal_size()

# (if needed) resize image so it fits terminal width
if iw > tw:
	niw = tw
	# new image height proportional to new width
	nih = int((niw/iw)*ih)
	image = image.resize((niw, nih))
	iw = niw
	ih = nih

# for each pixel print corresponding ascii character in the palette
for i in range(ih):
	for j in range(iw):
		# gray pixel value (i.e. integer in range 0..255)
		gray = image.getpixel((j, i))
		# map pixel value from range 0..255 to 0..len(palette)-1
		idx = int((gray/255)*(len(PALETTE)-1))
		# print ascii character (no newline)
		print(PALETTE[idx], end='')
	# newline
	print()

sys.exit(0)
