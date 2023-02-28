import cv2

# Loading an image

img = cv2.imread('assets/animboy.jpeg', 0)

# Resizing an image

img = cv2.resize(img, (400, 400))

cv2.imshow('bingo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
