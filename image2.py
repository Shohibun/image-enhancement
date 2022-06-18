#Grayscale 
import cv2 
import numpy as np

img = cv2.imread('sinigelut!.jpg')
h,w = img.shape[:2]
new_h, new_w = int(h/12),int(w/12)

resizeImg = cv2.resize(img, (new_w,new_h))
gray = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
