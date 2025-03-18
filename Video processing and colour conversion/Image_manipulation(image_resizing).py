import cv2

image = cv2.imread('tiger.jpeg')

resized_image = cv2.resize(image, (300, 300))

cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
