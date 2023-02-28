import cv2
import numpy as np

# Load the image
img = cv2.imread('assets/cat1.jpg', 0)

# Define the four source points
src_pts = np.float32([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]],
                      [0, img.shape[0]]])
# Define the four destination points
dst_pts = np.float32([[0, 0], [img.shape[1] * 0.75, 0],
                      [img.shape[1], img.shape[0]], [0, img.shape[0] * 0.75]])

# Calculate the homography matrix
H, _ = cv2.findHomography(src_pts, dst_pts)

# Apply the homography transformation
result = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))

# Display the original and result images
cv2.imshow('Original Image', img)
cv2.imshow('Result Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
