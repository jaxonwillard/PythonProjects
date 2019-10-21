from Gradient import Gradient
from colour import Color

class RedAndBlue(Gradient):
    def __init__(self):
        self.__color1 = Color("red")
        self.__color2 = Color("blue")
        # TODO: get rid of 100 hardcode
        self.__grad = list(self.__color1.range_to(self.__color2, 101)) # 1000 correlates with MAXITERATIONS

    def getColor(self, count):
        return self.__grad[count]

    def getSize(self, numColors):
        pass
