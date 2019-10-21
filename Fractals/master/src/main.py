import sys
from Config import Config
from ImagePainter import ImagePainter
import FractalFactory
from GradientFactory import makeGradient
# Process command-line arguments, allowing the user to select their fractal
config = Config()
# max iterations comes from config
if len(sys.argv) == 1:
    print("FractalFactory: Creating default fractal")
    print("GradientFactory: Creating default color gradient")
    gradient = makeGradient()
    fractal = FractalFactory.makeFractal(config.createConfiguration('data/branches.frac'))
elif len(sys.argv) == 2:
    print("GradientFactory: Creating default color gradient")
    gradient = makeGradient()
    fractal = FractalFactory.makeFractal(config.createConfiguration(sys.argv[1]))

else:
    gradient = makeGradient(sys.argv[2])
    fractal = FractalFactory.makeFractal(config.createConfiguration(sys.argv[1]))

imagePainter = ImagePainter(fractal, gradient)
imagePainter.paint()



