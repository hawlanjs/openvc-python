import cv2
import numpy as np

img = cv2.imread("lena.png")
print(img.shape)

imgCropped = img[0:200,200:500]
imgResize = cv2.resize(img,(300,200))
cv2.imshow("hawlanResize",imgResize)
cv2.imshow("hawlan",img)
cv2.imshow("test",imgCropped)

cv2.waitKey(0)
