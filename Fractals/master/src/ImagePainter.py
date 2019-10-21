from tkinter import Tk, Canvas, PhotoImage, mainloop
from Gradient import Gradient

class ImagePainter:
    def __init__(self, fractalObject, gradientObject):
        self.__imageName = fractalObject.getName()
        self.__fractalObject = fractalObject
        self.__gradient = gradientObject
        self.__imageNameString = fractalObject.getName()

    def paint(self):
        window = Tk()
        img = PhotoImage(width=self.__fractalObject.getWidth(), height=self.__fractalObject.getWidth())
        # Save the image as a PNG
        img.write(f"{self.__imageName}.png")
        print(f"Wrote image {self.__imageName}.png")
        min = ((float(self.__fractalObject.getCenterX()) - (float(self.__fractalObject.getAxisLength()) / 2.0)),
               (float(self.__fractalObject.getCenterY()) - (float(self.__fractalObject.getAxisLength()) / 2.0)))

        max = ((float(self.__fractalObject.getCenterX()) + (float(self.__fractalObject.getAxisLength()) / 2.0)),
               (float(self.__fractalObject.getCenterY()) + (float(self.__fractalObject.getAxisLength()) / 2.0)))
        self.create_GUI_window(self.__fractalObject.getWidth(), window, img)
        size = abs(max[0] - min[0]) / float(self.__fractalObject.getWidth())
        for row in range(self.__fractalObject.getWidth(), 0, -1):
            for column in range(self.__fractalObject.getWidth()):
                x = min[0] + column * size
                y = min[1] + row * size
                column2 = self.__gradient.getColor(self.__fractalObject.count(complex(x, y)))
                img.put(column2, (column, self.__fractalObject.getWidth() - row))
            window.update()  # display a row of pixels
        mainloop()

    def create_GUI_window(self, width, window, img):

        canvas = Canvas(window, width=width, height=width, bg=self.__gradient.getColor(0))
        canvas.pack()

        canvas.create_image((self.__fractalObject.getSize(), self.__fractalObject.getSize()), image=img, state="normal")
        canvas.pack()



