
from dataclasses import dataclass

from models import flash_card_content

@dataclass
class FlashCard:
    question: flash_card_content
    answer: flash_card_content
    name : str
    id : str
