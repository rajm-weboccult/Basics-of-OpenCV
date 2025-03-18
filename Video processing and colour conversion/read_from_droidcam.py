import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error:Could not open video stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to get frame")
        break

    cv2.imshow('DroidCam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
