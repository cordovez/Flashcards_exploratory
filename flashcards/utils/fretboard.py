from flashcards.utils.notes_on_strings import Guitar_Strings

def fretboard(tunning, scale):
    strings = []

    for open_note in tunning:
        open_note = Guitar_Strings(f"{open_note}", scale)
        strings.append(open_note)

    for string in strings:
        print( "".join(string.notes_on_strings)+"|") 