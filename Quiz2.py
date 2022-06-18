#Histogram Equalization 
import cv2
import numpy as np

name = 'sinigelut!.jpg'
img = cv2.imread(name, 0)
equalizer = cv2.equalizeHist(img)

gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
equalizer2 = cv2.cvtColor(equalizer, cv2.COLOR_GRAY2BGR)

result = np.hstack((gray, equalizer2))

cv2.imshow(f'{name} (Histogram Equalization)', result)
cv2.waitKey()
cv2.destroyAllWindows()