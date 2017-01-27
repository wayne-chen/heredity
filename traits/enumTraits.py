import enum

class enumSex(enum.Enum):
    Male = 'male'
    Female = 'female'

class enumPhysicalTrait(enum.Enum):
    ugly = 'ugly'
    pretty = 'pretty'
    blue_eyed = 'blue-eyed' 
    # increment size after each addition to the traits list.
    size = 3 
 
class enumMentalTrait(enum.Enum):
    normie = 'normie'
    mentally_challenged = 'mentally challenged'
    gifted = 'gifted'
    # increment size after each addition to the traits list.
    size = 3 


