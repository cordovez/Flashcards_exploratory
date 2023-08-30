from flashcards.utils.major import Major

    
def main():
 
    scale = Major("B")
    scale.key="C"
    notes = scale.scale
    print(notes)
if __name__ == "__main__":
    main()