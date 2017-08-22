#!/bin/sh
# Author: Guillermo Robles
#
# Install all the Codified fonts in the ~/.local/share/fonts directory

# Definitions
FONT_DIR="$HOME/.local/share/fonts"

# Create the fonts directory (if it doesn't exist)
[ ! -d "${FONT_DIR}" ] && mkdir -p "${FONT_DIR}"

find . -name 'Codified*.ttf' -exec cp {} "${FONT_DIR}" \;

fc-cache -f -v
