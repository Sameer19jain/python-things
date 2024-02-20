import cv2
import numpy as np

img = cv2.imread("resources/gal.jpg")
kernal = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)
imgCanny = cv2.Canny(img, 150,200)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=5)
imgEroded = cv2.erode(imgDialation, kernal, iterations=3)


#cv2.imshow("image", imgGray)
#cv2.imshow("blur image", imgBlur)
#cv2.imshow("canny image", imgCanny)
cv2.imshow("dilation image", imgDialation)
cv2.imshow("eroded image", imgEroded)

cv2.waitKey(0)