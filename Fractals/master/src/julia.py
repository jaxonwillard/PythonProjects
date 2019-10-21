#!/bin/env python3

# Julia Set Visualizer
from Gradient import Gradient
from Fractal import Fractal


class Julia(Fractal):

    def __init__(self, name, centerX, centerY, axisLength, cReal=-1.0, cImag=0.0 ):
        self.__name = name
        self.__gradient = Gradient()
        self.__width = 1024
        self.__size = 512
        self.__centerX = centerX
        self.__centerY = centerY
        self.__axisLength = axisLength
        self.__cReal = cReal
        self.__cImag = cImag

    def getName(self): return self.__name

    def getWidth(self): return self.__width

    def getSize(self): return self.__size

    def getCenterX(self): return float(self.__centerX)

    def getCenterY(self): return float(self.__centerY)

    def getAxisLength(self): return float(self.__axisLength)

    def count(self, z):

        """Return the index of the color of the current pixel within the Julia set
        in the gradient array"""

        # c is the Julia Constant; varying this value can yield interesting images
        c = complex(self.__cReal, self.__cImag)

        # Here 76 refers to the number of colors in the gradient
        for i in range(78):
            z = z * z + c  # Iteratively compute z1, z2, z3 ...
            if abs(z) > 2:
                return i  # The sequence is unbounded
        return 77        # Else this is a bounded sequence


