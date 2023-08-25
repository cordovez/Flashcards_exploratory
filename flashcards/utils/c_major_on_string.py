SCALE = ["C", "D", "E", "F", "G", "A", "B"]
STRINGS = ["E", "A", "D", "G", "B", "E"]

scale_on_string = []

def notes_on_string(guitar_string):
    note_upper = guitar_string.upper().strip()
    start_position = SCALE.index(note_upper)
    position = start_position
    
    for _ in range(len(SCALE)):
        next_note = SCALE[position]
        if next_note not in scale_on_string:
            scale_on_string.append(next_note)
        position += 1
        position %= len(SCALE)
            
    # Ensure scale_on_string has a length of 8 (including the octave)
    while len(scale_on_string) < 8:
        scale_on_string.append(scale_on_string[start_position-start_position])  
        
    return scale_on_string  # Return only the first 8 notes

