
class SexTraits:
    def __init__(self, arr):
        self._traits = arr

    @property
    def Female(self):
        return self._traits["F"]

    @property
    def Male(self):
        return self._traits["M"]


