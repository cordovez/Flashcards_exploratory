class Major:
    def __init__(self, key):
        self.key = key
        # self.key = key.upper() 
        # #upper doesn't work because I can't use lower case 'b' as a flat.

    @property
    def key(self):
        """The Key property. Setting the key determines the notes returned by
        scale"""
        return self._key
    
    @key.setter
    def key(self, new_key):
        self._key = new_key
        # self._key = new_key.upper()
        # #upper doesn't work because I can't use lower case 'b' as a flat.


    @key.deleter
    def key(self):
        print(f"the key of {self.key} was deleted")
        del self._key
        
    @property
    def scale(self):
        """The notes generated based on the key"""
        NOTES = ["C", "C#/Db", "D", "D#/Eb", "E", "F", 
                 "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
        
        INTERVALS = ["W", "W", "H", "W", "W", "W", "H"]

        _scale = []
        starting_note = self.key
        starting_position = NOTES.index(starting_note)
        _scale.append(starting_note)
        
        position = starting_position
        
        for step in  INTERVALS:
            if step == "W":
               position += 2
            elif step == "H":
               position +=1
               
            # Handle wrapping around to the beginning if needed
            position %= len(NOTES)
        
            _scale.append(NOTES[position])
            
        while len(_scale) < 8:
            _scale.append(NOTES[position])
        
        return _scale