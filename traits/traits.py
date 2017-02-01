import random

class GenericTrait:
    def RollTrait(self, traits):
        try:
            if len(traits) == 0:
               raise AttributeError    
            random.shuffle(traits)
            return traits[random.randint(0, len(traits) - 1)]
        except AttributeError: 
            print("couldn't roll a random trait")

    def RandomNegativeTrait(self, negativeArr):
        import random
        return (negativeArr[random.randint(len(negativeArr) - 1)])

    def RandomPositiveTrait(self, positiveArr):
        import random
        return (positiveArr[random.randint(len(positiveArr) - 1)])

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
    
    def __init__(self, physArr):
        super(PhysicalTrait, self).__init__()
        self._negativeTraits = physArr["negative"] 
        self._positiveTraits = physArr["positive"] 

    def RandomPositiveTrait(self):
        super.RandomPositiveTrait(self._positiveTraits)

    def RandomNegativeTrait(self):
        super.RandomNegativeTrait(self._negativeTraits)

    def RollTrait(self):
        super.RollTrait(self._allTraits)
    

class MentalTrait(GenericTrait):
    def __init__(self):
        super(MentalTrait, self).__init__()
        self._negativeTraits = physArr["negative"] 
        self._positiveTraits = physArr["positive"] 
        self._allTraits = self._negativeTraits + self._positiveTraits
    def RandomPositiveTrait(self):
        super.RandomPositiveTrait(self._positiveTraits)

    def RandomNegativeTrait(self):
        super.RandomNegativeTrait(self._negativeTraits)

    def RollTrait(self):
        super.RollTrait(self._allTraits)


