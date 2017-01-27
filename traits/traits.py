import random

class GenericTrait:
    def RollTrait(self, trait):
        try:
            if trait.size == 0:
               raise AttributeError    
            return trait[random.randint(0, trait.size.value - 1)]
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


class PhysicalTrait(GenericTrait):
    
    def __init__(self):
        super(PhysicalTrait, self).__init__()
    
    def __getitem__(self, idx):
        try:
            if idx < enumPhysicalTrait.size:
                return [x for x,_ in enumPhysicalTrait.__members__.items()][idx]
        except:
            print("Error: tried to fetch an item outside of physical trait's bounds")

    def RollTrait(self):
        super.RollTrait(self)
    

class MentalTrait(GenericTrait):
    def __init__(self):
        super(MentalTrait, self).__init__()

    def __getitem__(self, idx):
        try:
            if idx < enumPhysicalTrait.size:
                return [x for x,_ in enumPhysicalTrait.__members__.items()][idx]
        except:
            print("Error: tried to fetch an item outside of mental trait's bounds")

    def RollTrait(self):
        super.RollTrait(self)


