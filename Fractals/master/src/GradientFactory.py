from RedAndBlue import RedAndBlue
from Tranquil import Tranquil
from BloodyMary import BloodyMary
from Instagram import Instagram
from Peach import Peach
def makeGradient(gradient=""):
    if gradient == "redandblue":
        return RedAndBlue()
    elif gradient == "tranquil":
        return Tranquil()
    elif gradient == "bloodymary":
        return BloodyMary()
    elif gradient == "instagram":
        return Instagram()
    elif gradient == "peach":
        return Peach()
    else:
        return RedAndBlue()

