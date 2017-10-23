import tkinter   as tk
import os
import numpy
import cv2
from PIL import Image,ImageTk

LARGE_FONT = ("Verdana", 12)
im = Image.open('1.jpg')
im = im.resize((300, 300), Image.ANTIALIAS)

n_plate = Image.open("./cropped/plate/8.jpg")
n_plate  = n_plate.resize((100, 150), Image.ANTIALIAS)
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def load():

    photo = ImageTk.PhotoImage(im)
    cv = tk.Canvas()
    cv.pack(side='top', fill='both', expand='yes')
    cv.place(x=0, y=0)
    cv.create_image(10, 10, image=photo, anchor='nw')
    app.mainloop()

def plate():
    photo = ImageTk.PhotoImage(n_plate)
    cv = tk.Canvas()
    cv.pack(side='top', fill='both', expand='yes')
    cv.place(x = 0, y = 320)
    cv.create_image(10, 10, image=photo, anchor='nw')
    app.mainloop()
def tilt():
    photo2 = n_plate.rotate(90)
    photo2.show()
    photo2 = ImageTk.PhotoImage(n_plate)
    cv2 = tk.Canvas()

    cv2.pack(side='top', fill='both', expand='yes')
    cv2.place(x=500, y=320)

    cv2.create_image(10, 10, image=photo2, anchor='nw')
    app.mainloop()
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ANPR Bangla", font=LARGE_FONT)
        label.pack(pady=1, padx=100)


        button1 = tk.Button(self, text = "Load Image", command =load )
        button2 = tk.Button(self, text = "Show Plate", command = plate)
        button3 = tk.Button(self, text = "Tilt", command = tilt)


        button1.pack(padx=100)
        button2.pack()
        button3.pack()

app = SeaofBTCapp()
app.mainloop()