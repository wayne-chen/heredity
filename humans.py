from .traits import *

class Human:
    # what does a human possess
    def __init__(self, *args, **kwargs):
        # a human is born
        if kwargs.get('age') != None:
            self._age = kwargs.get('age')
        else:
            self._age = 0.0
        if kwargs.get('sex') != None:
            self._sex = sex
        else:
            self._sex = enumTraits.enumSex.Female

    @property
    def Sex(self):
        return self._sex
    
    @Sex.setter
    def Sex(self, sex):
        self._sex = sex

    @Sex.deleter
    def Sex(self):
        del self._sex

class Offspring(Human):
    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        # what determines birth?  Answer: milestone reached, 
        self._traits = kwargs.get('traits')
        pass

