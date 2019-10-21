#!/bin/env python3

# Julia Set Visualizer
from Gradient import Gradient
from Fractal import Fractal


class Pheonix(Fractal):

    def __init__(self, name, centerX, centerY, axisLength):
        self.__name = name
        self.__gradient = Gradient()
        self.__width = 1024
        self.__size = 512
        self.__centerX = centerX
        self.__centerY = centerY
        self.__axisLength = axisLength


    def getName(self): return self.__name

    def getWidth(self): return self.__width

    def getSize(self): return self.__size

    def getCenterX(self): return float(self.__centerX)

    def getCenterY(self): return float(self.__centerY)

    def getAxisLength(self): return float(self.__axisLength)

    def count(self, z):

        """Return the index of the color of the current pixel within the Julia set
        in the gradient array"""


        # Here 76 refers to the number of colors in the gradient
        c = complex(1, 0)

        # 78 is number of colors in gradient
        y = complex(0,0)
        p = -.5
        for i in range(78):
            z = z * z + c + y * p
            y = z
            if abs(z) > 2:
                return i  # The sequence is unbounded
        return 77        # Else this is a bounded sequence


