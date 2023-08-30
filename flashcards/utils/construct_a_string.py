MAJOR_SCALE = ["W", "W", "H", "W", "W", "W", "H"]
SHARP_NOTES = ["C", "C#", "D", "C#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
# C_major = ["C", "D", "E", "F", "G", "A", "B"]

string = []


class Build_Major_Scale:
    key: str = None
    
    def __init__(self, note):
        self.key = note.upper()
        self.note = note.upper()
    
    def get_notes_of_major_scale(self):
        scale = []
        starting_note = self.note
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
    
C_scale = Build_Major_Scale("C")
C_scale_notes = C_scale.get_notes_of_major_scale()
        
        
class Guitar_String:
    def __init__(self, string):
        self.string = string
        
    def notes_on_string(self):
        # what scale?
       
        start_position = C_scale_notes.index(self.string)
        print(start_position)
    


E_string = Guitar_String("E")

print(E_string.notes_on_string())