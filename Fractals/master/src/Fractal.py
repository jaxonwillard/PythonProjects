from Gradient import Gradient


class Fractal:
    # def __init__(self, name, centerY, centerX, axisLength):
    #     self.__name = name
    #     self.__gradient = Gradient()
    #     self.__width = 1024
    #     self.__size = 512
    #     self.__centerX = centerX
    #     self.__centerY = centerY
    #     self.__axisLength = axisLength

    def count(self, z):
        raise NotImplementedError("Subclass of Sequence must define its own current() operation")

    # def getName(self): return self.__name
    #
    # def getWidth(self): return self.__width
    #
    # def getSize(self): return self.__size
    #
    # def getCenterX(self): return self.__centerX
    #
    # def getCenterY(self): return self.__centerY
    #
    # def getAxisLength(self): return self.__axisLength

