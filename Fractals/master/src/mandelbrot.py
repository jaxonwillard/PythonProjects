#!/bin/env python3

# Mandelbrot Set Visualizer

from Gradient import Gradient
from Fractal import Fractal

class Mandelbrot(Fractal):
    def __init__(self, name, centerX, centerY, axisLength):
        self.__name = name
        self.__gradient = Gradient()
        self.__width = 640
        self.__size = 320
        self.__centerX = centerX
        self.__centerY = centerY
        self.__axisLength = axisLength

    def getName(self): return self.__name

    def getWidth(self): return self.__width

    def getSize(self): return self.__size

    def getCenterX(self): return self.__centerX

    def getCenterY(self): return self.__centerY

    def getAxisLength(self): return self.__axisLength

    def count(self, c):
        #TODO this is hardcoded!
        MAX_ITERATIONS = 100
        """Return the color of the current pixel within the Mandelbrot set"""
        z = complex(0, 0)  # z0
        for i in range(MAX_ITERATIONS):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                return i  # The sequence is unbounded
        # XXX: one of these return statements made the program crash...
        return 77   # Indicate a bounded sequence





