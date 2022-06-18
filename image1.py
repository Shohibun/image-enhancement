#Brightness
import cv2 
import numpy as np

img = cv2.imread("ibunOne.jpg")
imgbaru = np.zeros(img.shape, img.dtype) 
contrast = 1.0
brightness = 100 

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for z in range(img.shape[2]):
            imgbaru[y,x,z] = np.clip(contrast*img[y,x,z] + brightness, 0, 255)

cv2.imshow('brightness', imgbaru)
cv2.waitKey(0)
cv2.destroyAllWindows()