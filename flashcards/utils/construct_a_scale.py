MAJOR_SCALE = ["W", "W", "H", "W", "W", "W", "H"]
SHARP_NOTES = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#", "B"]
scale = []



def get_notes_of_major_scale(note):
    starting_note = note.upper()
    # Find the starting note's position
    start_position = SHARP_NOTES.index(starting_note)
    scale.append(starting_note)

    # Initialize the position counter
    position = start_position

    # Loop through the major scale pattern to construct the scale
    for step in MAJOR_SCALE:
        if step == "W":
            # Whole step, advance by 2 positions
            position += 2
        elif step == "H":
            # Half step, advance by 1 position
            position += 1

        # Handle wrapping around to the beginning if needed
        position %= len(SHARP_NOTES)

        # Append the note to the scale
        scale.append(SHARP_NOTES[position])

    # Ensure the scale has a length of 8 (including the octave)
    while len(scale) < 8:
        scale.append(SHARP_NOTES[position])

    return scale
