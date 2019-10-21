from julia import Julia
from mandelbrot import Mandelbrot
from Pheonix import Pheonix

def makeFractal(configuration):
    if configuration['type'] == 'julia':
        fractal = Julia(configuration['name'], configuration['centerX'], configuration['centerY'],
                      configuration['axisLength'], configuration['creal'], configuration['cimag'])
    elif configuration['type'] == 'pheonix':
        fractal = Pheonix(configuration['name'], configuration['centerx'], configuration['centery'], configuration['axislength'])
    else:
        fractal = Mandelbrot(configuration['name'], configuration['centerx'], configuration['centery'],
                        configuration['axislength'])

    return fractal

def printDictionary(configuration):
    print(configuration['pixels'])
