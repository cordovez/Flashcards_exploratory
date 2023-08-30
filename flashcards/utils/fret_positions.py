STRINGS = ["E", "A", "D", "G", "B", "E"]
STRINGS.reverse()

SCALE = ["C", "D", "E", "F", "G", "A", "B"]
MAJOR_INTERVALS = ["W", "W", "H", "W", "W", "W", "H"]


note = ""
empty_fret = "---|"
note_fret = f"-{note}-"


E = [True, False, True, False, True]
A = [False, True, True, False, True]
D = [False, True, True, False, True]
D = [False, True, False, True, True]
D = [False, False, True, False, True]
E = [True, False, True, False, True]



for string in STRINGS:
    print(f"{string}]---|---|---|---|---|")

print("   1   2   3   4   5 ")
    