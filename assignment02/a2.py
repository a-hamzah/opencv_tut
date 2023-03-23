import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('assets/pic.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(gray, (11, 11), 0)
edge = cv2.Canny(gray, 50, 150)

lines = cv2.HoughLines(edge, 1, np.pi / 180, 175)
# print(lines.shape)
# print(lines)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow("image", img)
cv2.waitKey()