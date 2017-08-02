#!/usr/bin/env python
"""
Generate a codified font from another one.

Based in the script by jfmdev (https://github.com/jfmdev/TuringFonts)

Author: Guillermo Robles
"""

import fontforge
from os import remove


FONT_NAME = "Codified-atbash"
FAMILY_NAME = "Codified"
FULLNAME = FONT_NAME
VERSION = "0.1"
COPYRIGHT = "Font based in Carlito, by tyPoland Lukasz Dziedzic. Licensed under the SIL Open Font License, Version 1.1"


def transformate(character):
    # Receive a character, return the codified character
    return chr((ord('z') - ord(character)) + ord('a'))


# End of editable values


def generate_dictionary(transformate):
    transformation = {}
    for i in range(ord('a'), ord('a') + 26):
        transformation[chr(i)] = transformate(chr(i))
    return transformation


def generate_font(from_font,
                  transformation,
                  font_name,
                  family_name,
                  fullname,
                  version,
                  copyright):
    # Get the font to be modified (Current font)
    myFont = fontforge.open(from_font)

    # Create a font to use as auxiliar variable
    temporal = fontforge.font()

    # Change the order of the letters
    for i in transformation:
        # Lowercase glyph
        myFont.selection.select(i)
        myFont.copy()
        temporal.selection.select(transformation[i])
        temporal.paste()
        # Uppercase glyphs
        myFont.selection.select(i.upper())
        myFont.copy()
        temporal.selection.select(transformation[i].upper())
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
    myFont.fontname = font_name
    myFont.familyname = family_name
    myFont.fullname = fullname
    myFont.version = version
    myFont.copyright = copyright

    temporal.close()

    myFont.generate(font_name + ".sfd")
    myFont.close()
    myFont = fontforge.open(font_name + ".sfd")
    myFont.generate(font_name + ".ttf")
    myFont.close()

    remove(font_name + ".sfd")
    remove(font_name + ".afm")


def main():
    generate_font("../original/Carlito-Regular.ttf",
                  generate_dictionary(transformate),
                  FONT_NAME,
                  FAMILY_NAME,
                  FULLNAME,
                  VERSION,
                  COPYRIGHT)


if __name__ == "__main__":
    main()
