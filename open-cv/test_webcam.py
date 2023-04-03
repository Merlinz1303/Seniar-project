import cv2
#import parinya
#import pyrebase
import time
import datetime

cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

cap2 = cv2.VideoCapture(1)
#cap2.set(cv2.CAP_PROP_FRAME_WIDTH,1280 )
#cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True :

    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
 

    if ret :
        cv2.imshow("Camera1",frame)
    if ret2 :
        cv2.imshow("Camera2",frame2)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    

cap.release()
cap2.release()
cv2.destroyAllWindows()
