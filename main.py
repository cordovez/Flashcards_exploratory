from flashcards.utils.c_major_on_string import notes_on_string


    
def main():
    note = "E"
    for each in notes_on_string(note):
        print(each, end=" ")

if __name__ == "__main__":
    main()