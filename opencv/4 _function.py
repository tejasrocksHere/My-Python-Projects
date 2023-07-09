import cv2
import numpy as np
img=cv2.imread("i.jpg")
kernal=np.ones((5,5),np.uint8)
imggray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7,7),0)
imgcanny=cv2.Canny(img,101,110)

imgdil=cv2.dilate(imgcanny,kernal,iterations=1)
cv2.imshow("dilate",imgdil)
cv2.imshow("greyimg",imgblur)
cv2.imshow("canny",imgcanny)
cv2.waitKey()