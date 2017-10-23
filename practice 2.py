import tkinter   as tk
import os
import numpy
import cv2
from PIL import Image,ImageTk

LARGE_FONT = ("Verdana", 12)
im = Image.open("1.jpg")
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
    cv.create_image(10, 10, image=photo, anchor='nw')
    app.mainloop()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)

        label.pack(pady=100, padx=100)
        label.place(x=120, y=120)

        button1 = tk.Button(self, text = "Load Image", command =load())

        # button2 = tk.Button(self, text = "show image", command = qf)

        button1.pack()
        button1.place(anchor = 'n',height = 50, width = 50, x = 0, y = 50 )
        # button2.pack()


app = SeaofBTCapp()
app.mainloop()