import cv2
from tracker import *


cap = cv2.VideoCapture(r"C:\Users\GauravKunal\Desktop\DS\AI\#2 DL\#3 Computer Vision\#1 OPENCV\#6 OpenCV Projects\#2 26 May Object Tracking from highways\highway.mp4")

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()