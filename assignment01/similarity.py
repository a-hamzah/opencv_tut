import cv2

# Load the image
img = cv2.imread('assets/cat1.jpg')

# Define the scale factor
scale = 1.0

# Define the rotation angle in degrees
angle = 45

# Define the translation amount in pixels
tx, ty = 50, -30

# Calculate the center of the image
h, w = img.shape[:2]
center = (w / 2, h / 2)

# Define the similarity matrix
M = cv2.getRotationMatrix2D(center, angle, scale)
print(M)
M[0, 2] += tx
M[1, 2] += ty

# Apply the similarity affine transformation
result = cv2.warpAffine(img, M, (w, h))

# Display the original and result images
cv2.imshow('Original Image', img)
cv2.imshow('Result Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
