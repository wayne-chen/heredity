# maybe useful constants???

oneDay = 1.0/365.0  # is this useful?

# End Constants

from enum import Enum

class PhysicalTrait(Enum):
    ugly = 0
    pretty = 1
    blue-eyed = 2
    # increment size after each addition to the traits list.
    size = 3  
              
class MentalTrait(Enum):

class MentalTrait(Enum):

def AgeEstimator(traitsArr):
    
    # life expectancy should start at some constant
    age = 76.0

    for trait in traitsArr:
        if trait == Trait.ugly:
            age -= 5.0  # ur gonna be alone for a while
        
        elif trait == Trait.pretty:
            age += 5.0  # live long and prosper

    
        
# need distribution of probability for rolling some of these traits as well

def RollTrait(playerTraits):
    # how should probability be determined for these, esp. by ethnicity/gender/that stuff?
    pass

class Player:
    def __init__(self, name, gender):
        self._arr = []  # contains array of traits
        self._gender = gender
        self._name = name
        self._age = 0.0
    def InheritFromParents(self, parents):
        # inherit parents' traits
        [self._arr.append(parent.trait) for parent in parents]
   
    def Speak(self):
        print("hi my name is %s and im %.1f!\n" % (self._name, self._age))
        
