import cv2
import numpy as np

img = cv2.imread('assets/cat1.jpg', 0)  # Loading an image

(height, width) = img.shape

# height, width = img.shape[:2]       # getting height and width of the image
print(height, width)

Tx, Ty = 300, -300  # units to be translated

# defining translation matrix
trans_matrix = np.float32([[1, 0, Tx], [0, 1, Ty]])
print(trans_matrix)

translated = cv2.warpAffine(img, trans_matrix,
                            (width, height))  # translation function

cv2.imshow('original', img)  # printing the images
cv2.imshow('translated', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
