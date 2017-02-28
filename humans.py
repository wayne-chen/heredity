from traits.traits import *

class Human:
    # what does a human possess
    def __init__(self, *args, **kwargs):
        # a human is born
        if kwargs.get('name') != None:
            self._name = kwargs.get('name')
        else:
            self._name = ""
        if kwargs.get('age') != None:
            self._age = kwargs.get('age')
        else:
            self._age = 0.0
        if kwargs.get('sex') != None:
            self._sex = kwargs.get('sex')
        else:
            self._sex = "female"
        if kwargs.get('traits') != Non:
            self._traits = kwargs.get('traits')
        elif kwargs.get('trait') != None:
            self._traits = [str(kwargs.get('trait'))]
        else:
            self._traits = []
    
    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    @Name.deleter
    def Name(self):
        del self._name

    @property
    def Trait(self):
        return self._traits[0]

    @property
    def Traits(self):
        return self._traits

    @Traits.setter
    def Traits(self, traits):
        self._traits = traits

    @Traits.deleter
    def Traits(self):
        del self._traits

    @property
    def Sex(self):
        return self._sex
    
    @Sex.setter
    def Sex(self, sex):
        self._sex = sex

    @Sex.deleter
    def Sex(self):
        del self._sex

    @property
    def Age(self):
        return self._age

    @Age.setter
    def Age(self, age):
        self._age = age

    @Age.deleter
    def Age(self):
        del self._age

class Offspring(Human):
    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        # what determines birth?  Answer: milestone reached, 
        self._traits = kwargs.get('traits')
        pass

