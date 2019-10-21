from Gradient import Gradient
from colour import Color

class Instagram(Gradient):
    def __init__(self):
        self.__color1 = Color("#833ab4")
        self.__color2 = Color("#fd1d1d")
        self.__color3 = Color("#fcb045")
        # TODO: get rid of 100 hardcode
        self.__grad = list(self.__color1.range_to(self.__color2, 101)) # 100 correlates with MAXITERATIONS
        # self.__grad.append(self.__color2.range_to(self.__color3, 51))

    def getColor(self, count):
        return self.__grad[count]

    def getSize(self, numColors):
        pass