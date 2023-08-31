from flashcards.utils.major import Major
from flashcards.utils.notes_on_strings import Guitar_Strings

def main():
 
    C = Major("C")
    scale = C.scale
    e_string = Guitar_Strings("E", scale)
    b_string = Guitar_Strings("B", scale)
    g_string = Guitar_Strings("G", scale)
    d_string = Guitar_Strings("D", scale)
    a_string = Guitar_Strings("A", scale)
    e_string = Guitar_Strings("E", scale)
  
    # print(scale)
    print("".join(e_string.notes_on_strings))
    print("".join(b_string.notes_on_strings))
    print("".join(g_string.notes_on_strings))
    print("".join(d_string.notes_on_strings))
    print("".join(a_string.notes_on_strings))
    print("".join(e_string.notes_on_strings))
    
if __name__ == "__main__":
    main()