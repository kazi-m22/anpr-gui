import cv2

import numpy as np

img = cv2.imread("./1.jpg")


img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)


noise_removal = cv2.bilateralFilter(img_gray,9,75,75)


equal_histogram = cv2.equalizeHist(noise_removal)



kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
morph_image = cv2.morphologyEx(equal_histogram,cv2.MORPH_OPEN,kernel,iterations=15)



sub_morp_image = cv2.subtract(equal_histogram,morph_image)

ret,thresh_image = cv2.threshold(sub_morp_image,0,255,cv2.THRESH_OTSU)

canny_image = cv2.Canny(thresh_image,250,255)


canny_image = cv2.convertScaleAbs(canny_image)


kernel = np.ones((3,3), np.uint8)

dilated_image = cv2.dilate(canny_image,kernel,iterations=1)


new,contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours= sorted(contours, key = cv2.contourArea, reverse = True)[:10]

screenCnt = None
for c in contours:
 peri = cv2.arcLength(c, True)
 approx = cv2.approxPolyDP(c, 0.06 * peri, True)

 if len(approx) == 4:
  screenCnt = approx
  break
final = cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)




mask = np.zeros(img_gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)


y,cr,cb = cv2.split(cv2.cvtColor(new_image,cv2.COLOR_RGB2YCrCb))
y = cv2.equalizeHist(y)
final_image = cv2.cvtColor(cv2.merge([y,cr,cb]),cv2.COLOR_YCrCb2RGB)
cv2.namedWindow("Enhanced Number Plate",cv2.WINDOW_NORMAL)
cv2.imshow("Enhanced Number Plate",final_image)
cv2.waitKey()