import tkinter   as tk
import os
import numpy
import cv2
from PIL import Image,ImageTk
global counter


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

def find_plate(im):
    import cv2

    import numpy as np

    img = cv2.imread(im)

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    noise_removal = cv2.bilateralFilter(img_gray, 9, 75, 75)

    equal_histogram = cv2.equalizeHist(noise_removal)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morph_image = cv2.morphologyEx(equal_histogram, cv2.MORPH_OPEN, kernel, iterations=15)

    sub_morp_image = cv2.subtract(equal_histogram, morph_image)

    ret, thresh_image = cv2.threshold(sub_morp_image, 0, 255, cv2.THRESH_OTSU)

    canny_image = cv2.Canny(thresh_image, 250, 255)

    canny_image = cv2.convertScaleAbs(canny_image)

    kernel = np.ones((3, 3), np.uint8)

    dilated_image = cv2.dilate(canny_image, kernel, iterations=1)

    new, contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    screenCnt = None
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.06 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break
    final = cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

    mask = np.zeros(img_gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    new_image = cv2.bitwise_and(img, img, mask=mask)

    y, cr, cb = cv2.split(cv2.cvtColor(new_image, cv2.COLOR_RGB2YCrCb))
    y = cv2.equalizeHist(y)
    final_image = cv2.cvtColor(cv2.merge([y, cr, cb]), cv2.COLOR_YCrCb2RGB)
    cv2.namedWindow("Enhanced Number Plate", cv2.WINDOW_NORMAL)
    cv2.imshow("Enhanced Number Plate", final_image)
    cv2.waitKey()






class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ANPR Bangla", font=LARGE_FONT)
        label.pack(pady=1, padx=100)

        cars = os.listdir("./car/")
        print(cars[2])

        button1 = tk.Button(self, text = "Load Image",
                            command =lambda :find_plate(cars[2]))



        button1.pack()


app = SeaofBTCapp()
app.mainloop()