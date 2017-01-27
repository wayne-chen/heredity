import random
from ..traits.enumTraits import *

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
    return age

# TODO: is this needed? if not, delete.
# a way to determine the weight of previously loaded traits and how they affect the end result of the roll
def RollTraitWeighted(playerTraits):
    # how should probability be determined for these, esp. by ethnicity/sex/that stuff?
    if playerTraits == []:
        # choose physical or mental
        # use a random algorithm to determine a trait
        if random.randint(0, 1):
            return random.randint(0, (enumPhysicalTrait.size.value) - 1)
        else:
            return enumMentalTrait(0, (enumMentalTrait.size.value) - 1)
    else:
        # use some algorithm to get one of these?
        pass
    return 1


