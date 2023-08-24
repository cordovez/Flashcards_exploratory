
from abc import ABC 
from typing import Optional

class Content(ABC):
    """ Basic representation of a single flashcard """
    front: str
    back: Optional[tuple] = None
