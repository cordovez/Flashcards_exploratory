# Introduction

This is an initial repository to explore possible functionalities of a new app in progress. The app will be a tool for learning notes on a guitar fretboard. This "exploration" is also a learning process.

I have decided to do a final push of this repository as it is, and continue building more advanced functionality on a new repository. This way I can share these files for other beginners who wish to learn about object-oriented programming.

I am myself a beginner, so I advice caution if copying/pasting code. However, I think it is a cute way to see objects and functions in use in a scenario that doesn't involve cats, dogs, employees, cars, foo nor bar.

## How you can use play with it

If you clone this repository, all you need to do is navigate to the root of the project in your terminal and enter `python3 main.py`

You will then be prompted to enter a key. Your choices are ` ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]`

The result will be a fretboard drawn in your terminal, with the notes written on the fret they occur on the fretboard. If you were to enter `C`, the terminal would respond with:

```
E ]--F--|-----|--G--|-----|--A--|-----|--B--|--C--|-----|--D--|-----|--E--||
B ]--C--|-----|--D--|-----|--E--|--F--|-----|--G--|-----|--A--|-----|--B--||
G ]-----|--A--|-----|--B--|--C--|-----|--D--|-----|--E--|--F--|-----|--G--||
D ]-----|--E--|--F--|-----|--G--|-----|--A--|-----|--B--|--C--|-----|--D--||
A ]-----|--B--|--C--|-----|--D--|-----|--E--|--F--|-----|--G--|-----|--A--||
E ]--F--|-----|--G--|-----|--A--|-----|--B--|--C--|-----|--D--|-----|--E--||

```

if your browser window is wide enough, these lines should not be wrapping and you would see all 12 frets of the fretboard in one line.

Not a thing of beauty, but it helps me visualise the fretboard as I think of more advanced functionality.

## The big picture

Eventually, I would like to develop an app for learning the notes on a guitar fretboard using flashcards. To do this, I will break up the fretboard into seven positions (As Berklee College of Music does), and the notes on each position will be learned in groups of triads and their inversions.

## Some algorithmic homework for you ... if you should chose to accept the challenge

In theory, one only has to learn the notes of the key of C, which is all naturals, and just remember that the other frets are accidentals.

So how would you make your app render a fretboard with only only an "X" at a random fret where a note on the scale of "C" would fall. For example:

```
E ]-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----||
B ]-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----||
G ]-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----||
D ]-----|-----|--X--|-----|-----|-----|-----|-----|-----|-----|-----|-----||
A ]-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----||
E ]-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----||
```

And prompt the user to type in the note corresponding to that position.

## Some detail on the development of the future app

Cards are grouped into stacks. The user chooses a stack and cards are presented randomly from that stack. The user answers the question and self-grades his response. I would like to implement spaced repetition for the cards. So based on her grade for that card, the card is repeated at an appropriate time interval.
