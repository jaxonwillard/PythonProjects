from Gradient import Gradient
from colour import Color

class Tranquil(Gradient):
    def __init__(self):
        self.__color1 = Color("#eecda3")
        self.__color2 = Color("#ef629f")
        # TODO: get rid of 100 hardcode
        self.__grad = list(self.__color1.range_to(self.__color2, 100)) # 100 correlates with MAXITERATIONS

    def getColor(self, count):
        return self.__grad[count]

    def getSize(self, numColors):
        pass
