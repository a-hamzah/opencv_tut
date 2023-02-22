import cv2

img = cv2.imread('assets/animboy.jpeg', -1)
img = cv2.resize(img, (100, 100))

cv2.imshow('bingo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
