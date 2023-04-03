import cv2
import time
import datetime
import cvzone

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
cap.set(cv2.CAP_PROP_FPS, 60)
fpsreader = cvzone.FPS()


cap2 = cv2.VideoCapture(1)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
cap2.set(cv2.CAP_PROP_FPS, 60)
fpsreader2 = cvzone.FPS()

fps_start = 0
fps = 0


while True :
    
    ret , frame = cap.read()
    ret2 , frame2 = cap2.read()
    
    #fps_end = time.time()
    #time_diff = fps_end - fps_start
    #fps = 1/(time_diff)
    #fps_start = fps_end
    font = cv2.FONT_HERSHEY_SIMPLEX
    #fps_text = "FPS :  {:.2f}".format(fps)
    
    #cv2.putText(frame, fps_text, (50,50) ,font ,1 ,(0,0,255),2)
    #cv2.putText(frame2, fps_text, (50,50) ,font ,1 ,(0,0,255),2)
    fps,frame = fpsreader.update(frame)
    fps2,frame2 = fpsreader.update(frame2)
    
    print(fps)
    print(fps2)
    
    
    cv2.imshow("Camera 1",frame)
    cv2.imshow("Camera 2",frame2)

    cv2.waitKey(1)

cap.release()
cap2.release()
cv2.destroyAllWindows()


