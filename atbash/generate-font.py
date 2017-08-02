#!/usr/bin/env python
"""
Generate a codified font from another one.

Based in the script by 

Author: Guillermo Robles
"""

# Load module
import fontforge
import os


def transformate(character):
    # Receive a character, return the codified character
    return chr((ord('z') - ord(character))+ord('a'))


FONT_NAME = "Codified-atbash"
FAMILY_NAME = "Codified"
FULLNAME = FONT_NAME
VERSION = "0.1"
COPYRIGHT = "Font based in Carlito, by tyPoland Lukasz Dziedzic. Licensed under the SIL Open Font License, Version 1.1"

TRANSFORMATION = {}
for i in range(ord('a'), ord('a') + 26):
    TRANSFORMATION[chr(i)] = transformate(chr(i))

# Get the font to be modified (Current font)
myFont = fontforge.open("../original/Carlito-Regular.ttf")

# Create a font to use as auxiliar variable
temporal = fontforge.font()

# Change the order of the letters
for i in TRANSFORMATION:
    # Lowercase glyph
    myFont.selection.select(i)
    myFont.copy()
    temporal.selection.select(TRANSFORMATION[i])
    temporal.paste()
    # Uppercase glyph
    myFont.selection.select(i.upper())
    myFont.copy()
    temporal.selection.select(TRANSFORMATION[i].upper())
    temporal.paste()

# Copy back the letters in the auxiliar font to the original font.
temporal.selection.select(("ranges", None), "a", "z")
myFont.selection.select(("ranges", None), "a", "z")
temporal.copy()
myFont.paste()
temporal.selection.select(("ranges", None), "A", "Z")
myFont.selection.select(("ranges", None), "A", "Z")
temporal.copy()
myFont.paste()

# Edit font metadata
myFont.fontname = FONT_NAME
myFont.familyname = FAMILY_NAME
myFont.fullname = FULLNAME
myFont.version = VERSION
myFont.copyright = COPYRIGHT

temporal.close()

myFont.generate(FONT_NAME + ".sfd")
myFont.close()
myFont = fontforge.open(FONT_NAME + ".sfd")
myFont.generate(FONT_NAME + ".ttf")
myFont.close()

os.remove(FONT_NAME + ".sfd")
os.remove(FONT_NAME + ".afm")
