import cv2
import numpy as np

img = cv2.imread('assets/cat1.jpg', 0)      # Loading an image
height, width = img.shape[:2]
# defining euclidean transformation matrix for theta = 30 and Tx = 200, Ty = 200
# sin(30) = 0.5 and cos(30) = 0.86

mat = np.float32([[0.86, -0.5, 200], [0.5, 0.86, 200]])

result = cv2.warpAffine(img, mat, (width, height))

cv2.imshow('original', img)     # printing the images
cv2.imshow('euclidean', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
