#!/usr/bin/python3

# maybe useful constants???

oneDay = 1.0/365.0    # is this useful?

# End Constants

import json

import random, enum

# cls = json.decoder.JSONDecoder

class Sex(enum.Enum):
    Male = 'male'
    Female = 'female'

class GenericTrait:
    def RollTrait(self, trait):
        try:
            if trait.size == 0:
               raise AttributeError    
            return cls(random.randint(0, trait.size.value))
        except AttributeError: 
            print("couldn't roll a random trait")


class Traits:
    
    # overriding array arguments

    def __init__(self):
        self._arr = []
    
    def __add__(self, value):
        self._arr.__add__(value)

    def __contains__(self, key):
        self._arr.__contains__(key)

    def __delitem__(self, key):
        self._arr.__delitem(key)

    def __getitem__(self, idx):
        return self._arr[idx]

    def __len__(self):
        return len(self._arr)

    def append(self, trait):
        try:
            if 'Trait' in type(trait):
                _arr.append(trait)
            else:
                raise TypeError
        except TypeError:
            print('Failed at adding trait. Trait is incorrect type.')


class PhysicalTrait(enum.Enum):
    ugly = 'ugly'
    pretty = 'pretty'
    blue_eyed = 'blue-eyed' 
    # increment size after each addition to the traits list.
    size = 3 
    
    def __init__(self):
        super(PhysicalTrait, self).__init__()

    def RollTrait(self):
        super.RollTrait(self)
    

class MentalTrait(enum.Enum):
    normie = 'normie'
    mentally_challenged = 'mentally challenged'
    gifted = 'gifted'
    size = 3 

    def __init__(self):
        super(MentalTrait, self).__init__()

    def RollTrait(self):
        super.RollTrait(self)

def AgeEstimator(traitsArr):
    # life expectancy should start at some constant
    age = 76.0
    for trait in traitsArr:
        if trait == PhysicalTrait.ugly:
            age -= 5.0  # ur gonna be alone for a while
        elif trait == PhysicalTrait.pretty:
            age += 5.0  # live long and prosper
        elif trait == MentalTrait.gifted:
            age += 5.0  # you outsmart your life expectancy. wow.
        elif trait == MentalTrait.mentally_challenged:
            age -= 5.0  # life is frickin hard
        #etc.

def RollTrait(playerTraits):
    # how should probability be determined for these, esp. by ethnicity/sex/that stuff?
    if playerTraits == []:
        # choose physical or mental
        # use a random algorithm to determine a trait
        if random.randint(0, 1):
            return PhysicalTrait
        else:
            return MentalTrait
        return 1

class Player:
    def __init__(self, name, sex):
        self._arr = []  # contains array of traits
        self._sex = sex
        self._name = name
        self._age = 0.0
    def InheritFromParents(self, parents):
        # inherit parents' traits
        [self._arr.append(parent.trait) for parent in parents]
    def Speak(self):
        print("hi my name is %s and im %.1f!\n" % (self._name, self._age))
    def ChooseTraits(self, offspring):
        pass

class Human:
    # what does a human possess
    def __init__(self):
        self._age = 0
        self._sex = Sex.Female

class Offspring:
    def __init__(self, traits):
        # what determines birth?
        self._arr = []  # contains array of traits
         
class Game:
    def __init__(self, playerName, playerGender):
        self.player = Player(playerName, playerGender) 

    def Start(self):
        pass 
