#Konversi citra berwarna ke citra grayscale 
import cv2

path_file = "sinigelut!.jpg"

img = cv2.imread(path_file)
grey = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

cv2.imshow(f"{path_file} ORI", img)
cv2.imshow(f"{path_file} Filteran", grey)
cv2.waitKey()
cv2.destroyAllWindows()