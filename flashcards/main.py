from models.flashcard import FlashCard
from models.inversions import Inversion
import json

def main():
    set = []
    for inversion in list(Inversion):
        front = inversion.name
        back = inversion.value
        card = FlashCard(name=front, id=back, 
                                      question=front, answer=back)
        set.append(json.dumps(card.__dict__))
    
    print(set)
    
if __name__ == "__main__":
    main()
    