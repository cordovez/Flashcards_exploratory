
from enum import Enum

class Inversion(Enum):
    ROOT = ("R", "3", "5")
    FIRST = ( "3", "5", "R")
    SECOND = ("5", "R", 3)
