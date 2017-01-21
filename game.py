from .humans import *
from .traits import *

class Player(Human):
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

class Game:
    def __init__(self, playerName, playerGender):
        import json, os
        self.player = Player(playerName, playerSex) 
        data = ""
        f = open(os.path.dirname(os.path.abspath(__file__)) + '/traits.json', 'r')
        for line in f.readlines():
            data += line
        f.close()

        traitsData = json.loads(data)

    def Start(self):
        #start the game.
        pass 

    def MilestoneReached(self):
        # made it to a milestone! let's pick a trait for the player.
        self.player.ChooseTraits()
        pass

