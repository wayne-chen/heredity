from humans import *
from traits.traits import *
import calculations
class Player(Human):
    def __init__(self, name, sex, parents):
        self._traits = []  # contains array of traits
        self._sex = sex
        self._name = name
        self._age = 0.0
        self._estimatedAgeOfDeath = 0.0
        # list of parents
        self._parents = parents
        # self.InheritFromParents()

    # def Update(self):
    #    self.ReadjustEstimatedDeath

    # There might be other methods that must be re-evaluated, so this
    # might be packaged in a higher level "Update" method
    def ReadjustEstimatedDeath(self):
        self._estimatedAgeOfDeath = calculations.AgeEstimator(self._traits)

    def InheritFromParents(self):
        # inherit parents' traits
        [self._traits.append(parent.Trait()) for parent in self.parents]

    def Speak(self):
        print("hi my name is %s and im %.1f!\n" % (self._name, self._age))

    @property
    def Traits(self):
        return self._traits

    @Traits.setter
    def Traits(self, traits):
        # the setter appends a trait to the traits array
        self._traits = traits

    @Traits.deleter
    def Traits(self):
        del self._traits

    def AddTrait(self, trait):
        self._traits.append(trait)
        self.ReadjustEstimatedDeath()

class Game:
    def __init__(self, playerName, playerGender):
        import json, os
        self.player = Player(playerName, playerSex) 
        data = ""
        f = open(os.path.dirname(os.path.abspath(__file__)) + '/traits.json', 'r')
        for line in f.readlines():
            data += line
        f.close()
        self.traitsData = json.loads(data)['traits']
        Start(self.traitsData)

    def Start(self):
        # load parents
        # generate based on number of mental and physical traits
        # roll some positive traits
        print("Rolling parents...") 
        szPhysicalTraits = len(self.traitsData['physical']['positive'])
        szMentalTraits = len(self.traitsData['mental']['positive'])
        szRollableTraits = szPhysicalTraits + szMentalTraits
        import random
        # leave it like this for rolling in a way where it's a little more interesting later on, aka closer to pure randomness
        # do a random.randint(0, szRollableTraits)
        # have it weighted to get either physical or mental more based on some algorithm

        while True:
            # physicalTraitIdx = random.randint(0, szRollableTraits)
            physicalTraitIdx = random.randint(0, szPhysicalTraits - 1)
            # if physicalTraitIdx - szMentalTraits > szPhysicalTraits:
                # physicalTraitIdx -= szMentalTraits
                # break
            break
        while True:
            # mentalTraitIdx = random.randint(0, szRollableTraits)
            mentalTraitIdx = random.randint(0, szMentalTraits - 1)
            # if mentalTraitIdx - szPhysicalTraits > szMentalTraits:
                # mentalTraitIdx -= szPhysicalTraits
                # break
            break

        # for now, just use these indices to get mental and physical traits
        self.player.AddTrait(self.traitsData['physical']['positive'][physicalTraitIdx])
        self.player.AddTrait(pself.traitsData['physical']['positive'][mentalTraitIdx])
        
        #start the game.

        pass 

    # this occurs when there is another round of events
    def NextTurn(self):
        traits = []
        traits.append(self.RollOffspringTrait())
        newOffspring = Offspring(traits = traits)
        pass

    def RollOffspringTrait(self):
        #triggered from user action, maybe it will involve other ui stuff..
        return calculations.RollTraitWeighted(self.player.Traits())

    def SelectTrait(self):
        pass
   
    # triggered in UI, event occurs when life milestones occur
    def SelectPhysicalTrait(self):
        pass

    # triggered in UI, event occurs when life milestones occur
    def SelectMentalTrait(self):
        pass 

    def MilestoneReached(self):
        # made it to a milestone! let's pick a trait for the player.

        pass
