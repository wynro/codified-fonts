# Codified Font Family

I volunteer in a young association. Sometimes, I have to create Hint/Relay games, in which a group of kids go to a certain place (Relay) and get a codified message that points them to the next Relay (Hint). After a bunch of these, the group gets to the goal.

A important part of these games are the hints. Usually, they are messages with simple substitution-based codifications, like Morse or ROT13. Creating the messages is a pain, specially if you want to create complex paths, with a lot of hints. This project's aim is to simplify the codification process, both for me and for my companions in the association.

# Basic idea

Fonts allow a text editing program to apply different looks to the characters. What if some of those looks where already codified?.

\(After some investigation, this is by no means an original idea. In any case, is an opportunity to learn some things about font creation and editing)

What if a font already codified the Caesar cipher?. You could easily just write your message, select it and then select "Codified-Caesar" as the font. Automagically, your message gets codified, without the use of external tools, just using your favorite text editing software.

# Limitations

## Only one by one correspondency

This system only works for basic, substitution, monoalphabetic ciphers, so it has no use as a "real" codification.

As far as I know, some writing systems (like Devanagari or Arabic) allows to change the glyph according to its surroundings. Although this would (Theoretically, I haven't tested it) allow more complex ciphers, I feel it would destroy the simplicity I pursuit.

## Only monochromatic glyphs

Although there are extensions that allows [colorized fonts](https://www.colorfonts.wtf/), they are not widely extended, and I simply have no idea how to use them. Maybe later.

## Copying fonts has problems

The spacing, ligature, and some other glyph characteristics are currently just copied, which means that some characters appear weirdly aligned. I'll fix it someday <!-- Read: At the heat dead of the universe, or when I learn how to do it, whichever happens before -->

# Alphabets I would like to support

- [x] Atbash (With alignment problems)
- [x] Caesar (With alignment problems)
- [x] ROT-N (For all N, not only 13)
- [x] Morse
- [x] NATO Phonetic Alphabet
- [x] Flag Semaphore
- [x] Braille
- [x] International Maritime Signal Flag (in Black and White)
- [x] Pigpen
- [x] Templar
- [x] Polybius Square/Tap Code

And once I learn how to do colorized fonts
- [ ] International Maritime Signal Flag

