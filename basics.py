import cv2

img = cv2.imread('assets/logo.jpg', 0)

cv2.imshow('bingo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()