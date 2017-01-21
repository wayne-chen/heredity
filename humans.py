from .traits import *

class Human:
    # what does a human possess
    def __init__(self):
        self._age = 0.0
        self._sex = enumTraits.enumSex.Female
    

class Offspring:
    def __init__(self, traits):
        # what determines birth?
        self._arr = []  # contains array of traits
 
