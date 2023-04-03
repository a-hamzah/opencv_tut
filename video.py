import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, vid = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    my_img_frame = np.zeros(vid.shape, np.uint8)
    
    tiny_img = cv2.resize(vid, (0, 0), fx=0.5, fy=0.5)
    
    my_img_frame[:height//2, :width//2] = cv2.rotate(tiny_img, cv2.ROTATE_180)
    my_img_frame[height//2:, :width//2] = tiny_img
    my_img_frame[:height//2, width//2:] = cv2.rotate(tiny_img, cv2.ROTATE_180)
    my_img_frame[height//2:, width//2:] = tiny_img

    cv2.imshow('webcam', my_img_frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()