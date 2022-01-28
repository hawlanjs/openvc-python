import cv2
import numpy as np

img = cv2.imread("lena.png")
kernel = np.ones((5,5),np.uint8)


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("hawlan",imgGray)
cv2.imshow("hawlan Blure",imgBlur)
cv2.imshow("hawlan Canny",imgCanny)
cv2.imshow("hawlan normal",img)
cv2.imshow("hawlan Dialation",imgDialation)
cv2.imshow("hawlan Eroded",imgEroded)
cv2.waitKey(0)
