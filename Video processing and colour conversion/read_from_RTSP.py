import cv2

# RTSP stream URL
rtsp_url = 'rtsp://username:password@IP_address:port/stream'

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open RTSP stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to get frame")
        break

    cv2.imshow('RTSP Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
