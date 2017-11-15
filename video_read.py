import cv2
import os
import numpy as np

count = 0
success = True
files = os.listdir('./videos/')


os.chdir('./videos/')
for v in files:

  vidcap = cv2.VideoCapture(v)

  success, image = vidcap.read()

  while success:
    success,image = vidcap.read()
    print('Read a new frame: ', success)

    cv2.imwrite("C:\\Users\\misbah\ \Documents\\Projects\\Python\\anpr_tkinter\\images\\frame%d.jpg" % count, image)     # save frame as JPEG file
    count += 1