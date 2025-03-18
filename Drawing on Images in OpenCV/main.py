import numpy as np
import cv2

# Create a black image
image = np.ones((400, 400, 3), dtype="uint8")*255

#image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.rectangle(image, (50, 50), (150, 150), (255, 0, 0), thickness=2)

#cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.circle(image, (200, 200), 50, (0, 255, 0), thickness=2)

#cv2.polylines(image, [pts], isClosed, color, thickness)
points = np.array([[300, 300], [350, 250], [400, 300], [350, 350]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(image, [points], isClosed=True, color=(0, 0, 255), thickness=2)

#image = cv2.putText(image,'OpenCV',org,font,fontScale,color,thickness, cv2.LINE_AA)
cv2.putText(image, 'OpenCV', (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow('Image with Shapes', image)
cv2.imwrite("output_image.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()