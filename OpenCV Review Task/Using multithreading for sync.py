import cv2
import numpy as np
import threading
import queue
import time

RTSP_URLS=[
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=1&subtype=0",
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=2&subtype=0",
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=3&subtype=0"
]
#Video captures and frame queues
caps=[cv2.VideoCapture(url) for url in RTSP_URLS]
queues=[queue.Queue(maxsize=1) for _ in caps]

def grab_frames(cap, q):
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        if q.full():
            try:
                q.get_nowait()
            except queue.Empty:
                pass
        q.put(frame)

#threads for each camera
threads= []
for c, q in zip(caps, queues):
    t=threading.Thread(target=grab_frames,args=(c, q),daemon=True)
    t.start()
    threads.append(t)

prev_frames=[None]*len(RTSP_URLS)

try:
    while True:
        start=time.time()
        grid=[]
        for i, q in enumerate(queues):
            try:
                frame=q.get_nowait()

                #Bilateral filter and cropping bottom 10%
                filtered=cv2.bilateralFilter(frame, 15, 95, 95)
                cropped=filtered[:int(filtered.shape[0] * 0.9), :]

                #Get difference frame
                diff=cv2.absdiff(cropped,prev_frames[i]) if prev_frames[i] is not None else np.zeros_like(cropped)
                prev_frames[i]=cropped.copy()

                # Resize and append to grid
                resized_filtered,resized_diff=[cv2.resize(f,(400, 200))  for f in [cropped, diff]]
                grid.append(cv2.hconcat([resized_filtered,resized_diff]))

            except queue.Empty:
                continue

        if grid:
            cv2.imshow("Cameras",cv2.vconcat(grid))

        passed_time=time.time()-start
        time.sleep(max(0, 0.033-passed_time))

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
finally:
    for c in caps:
        c.release()
    cv2.destroyAllWindows()