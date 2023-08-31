from flashcards.utils.major import Major
from flashcards.utils.notes_on_strings import Guitar_Strings

STANDARD_TUNING = ["E", "B", "G", "D", "A", "E"]

def main():
    key = input("Enter key ... Chose C to begin: ")
    major = Major(key.title())
    scale = major.scale
    strings = []
    
    for open_note in STANDARD_TUNING:
        open_note = Guitar_Strings(f"{open_note}", scale)
        strings.append(open_note)
    
    for string in strings:
        print("".join(string.notes_on_strings)+"|")
    
    
if __name__ == "__main__":
    main()