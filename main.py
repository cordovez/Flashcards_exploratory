from flashcards.utils.major import Major
# from flashcards.utils.notes_on_strings import Guitar_Strings
from flashcards.utils.fretboard import fretboard

STANDARD_TUNING = ["E", "B", "G", "D", "A", "E"]

def main():
    key = input("Enter key ... Chose C to begin: ")
    major = Major(key.title())
    scale = major.scale
    
    print(fretboard(STANDARD_TUNING, scale))
    
if __name__ == "__main__":
    main()