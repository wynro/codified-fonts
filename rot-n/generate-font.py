#!/usr/bin/env fontforge
"""
Generate a codified font from another one.

Based in the script by jfmdev (https://github.com/jfmdev/TuringFonts)

Author: Guillermo Robles
License: GPLv2

    Copyright (C) 2017  Guillermo Robles

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import fontforge
from os import remove


FONT_NAME = "CodifiedROT{:02}-Regular"
FAMILY_NAME = FONT_NAME.split("-")[0]
FULLNAME = FONT_NAME
VERSION = "0.1"
COPYRIGHT = "Font based in Carlito, by tyPoland Lukasz Dziedzic. " + \
    "Licensed under the SIL Open Font License, version 1.1"


def transformate(character, value):
    # Receive a character, return the codified character
    return chr((ord(character) - ord('a') - value) % 26 + ord('a'))


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

    # Workaround for https://github.com/fontforge/fontforge/issues/3130
    myFont.generate(font_name + ".sfd")
    myFont.close()
    myFont = fontforge.open(font_name + ".sfd")
    myFont.generate(font_name + ".ttf")
    myFont.close()

    remove(font_name + ".afm")


def main():
    for i in range(1, 26):
        generate_font("../original/Carlito-Regular.ttf",
                      generate_dictionary(lambda x: transformate(x, i)),
                      FONT_NAME.format(i),
                      FAMILY_NAME.format(i),
                      FULLNAME.format(i),
                      VERSION,
                      COPYRIGHT)


if __name__ == "__main__":
    main()
