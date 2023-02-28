import cv2
import numpy as np

img = cv2.imread('assets/cat1.jpg', 0)      # Loading an image

height, width = img.shape[:2]       # getting height and width of the image
# print(height, width)


Tx, Ty = height/8, width/8     # units to be translated

# defining translation matrix
trans_matrix = np.float32([[1, 0, Tx], [0, 1, Ty]])
# print(trans_matrix)

translated = cv2.warpAffine(
    img, trans_matrix, (width, height))  # translation function

cv2.imshow('original', img)     # printing the images
cv2.imshow('translated', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
