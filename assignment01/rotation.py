import cv2
import numpy as np

img = cv2.imread('assets/cat1.jpg', 0)      # Loading an image
height, width = img.shape[:2]

center = (height/2, width/2)


rot_matrix = cv2.getRotationMatrix2D(center, 90, 0.5)

rotated_img = cv2.warpAffine(img, rot_matrix, (width, height))

cv2.imshow('original', img)     # printing the images
cv2.imshow('euclidean', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
