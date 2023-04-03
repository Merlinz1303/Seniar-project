import cv2
import time
import datetime
from ultralytics import YOLO
import supervision as sv
import pyrebase

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

cap2 = cv2.VideoCapture(1)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

config = {
	'apiKey': "AIzaSyDeuDvt1c5fEfgdx3WWwaO5aj8c7BjW2ds",
	'authDomain': "realtime-database-a9abe.firebaseapp.com",
	'databaseURL': "https://realtime-database-a9abe-default-rtdb.asia-southeast1.firebasedatabase.app",
	'projectId': "realtime-database-a9abe",
	'storageBucket': "realtime-database-a9abe.appspot.com",
	'messagingSenderId': "792289007586",
	'appId': "1:792289007586:web:54b29d4fbb39b19f848bbb",
	'measurementId': "G-PWXMHG8Q8Z",
	'serviceAccount' :'ServiceAccount.json'
	}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage =firebase.storage()

last_detec = 'none'
last_image_name = 'none'
last_detec_time = 0
img_folder = '/Users/merlinz/Desktop/SeniarProject/Seniar-project-code/open-cv/camera1/'

last_detec2 = 'none'
last_image_name2 = 'none'
last_detec_time2 = 0
img_folder2 = '/Users/merlinz/Desktop/SeniarProject/Seniar-project-code/open-cv/camera2/'

model = YOLO("yolov8s.pt")
model2 = YOLO("yolov8s.pt")
box_annotator = sv.BoxAnnotator(thickness = 2 ,text_thickness = 2 ,text_scale = 1)

#fps_start = 0
#fps = 0

while True :
    ret , frame = cap.read()
    ret2 , frame2 = cap2.read()
    
    result = model(frame)[0]
    result2 = model2(frame2)[0]
    
    detections = sv.Detections.from_yolov8(result)
    detections2 = sv.Detections.from_yolov8(result2)
    
    
    labels = [f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
            ]
    labels2 = [f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections2
           ]
            
    frame = box_annotator.annotate(scene = frame ,detections = detections , labels = labels)
    frame2 = box_annotator.annotate(scene = frame2 ,detections = detections2 , labels = labels2)
    
    #fps_end = time.time()
    #time_diff = fps_end - fps_start
    #fps = 1/(time_diff)
    #fps_start = fps_end
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #fps_text = "FPS :  {:.2f}".format(fps)
    #cv2.putText(frame, fps_text, (50,50) ,font ,1 ,(0,0,255),2)
    
    cv2.imshow("Camera 1",frame)
    cv2.imshow("Camera 2",frame2)
    time = datetime.datetime.now()

    if ret :
        for r in result:
            for c in r.boxes.cls:
                name = model.names[int(c)]
                current_time = str(time.day)+'-'+str(time.month)+'-'+str(time.year)+'_'+str(time.hour)+':'+str(time.minute)+':'+str(int(time.second))
                if name=="person":
                    print(name)
                    detect_type = "person"
                    last_detec = "person"
                    last_detec_time = current_time
                    img_name = 'Detection_Person' +current_time+'.jpg'
                    img_local = img_folder + img_name
                    last_image_name = img_name
                    cv2.imwrite(img_local,frame)
                    img_path = 'camera1/'+img_name
                    data = {"Type" : detect_type ,"Last_Detection_Type" : last_detec ,"Last_Detect_time" : last_detec_time ,
                            "Image_name" : img_name , "Last_Image_Name" : last_image_name}
                    db.child("Detection").set(data)
                    storage.child(img_path).put(img_local)
                elif name=="dog":
                    print(name)
                    detect_type = "dog"
                    last_detec = "dog"
                    last_detec_time = current_time
                    img_name = 'Detection_Dog' +current_time+'.jpg'
                    img_local = img_folder + img_name
                    last_image_name = img_name
                    cv2.imwrite(img_local,frame)
                    img_path = 'camera1/'+img_name
                    data = {"Type" : detect_type ,"Last_Detection_Type" : last_detec ,"Last_Detect_time" : last_detec_time ,
                            "Image_name" : img_name , "Last_Image_Name" : last_image_name}
                    db.child("Detection").set(data)
                    storage.child(img_path).put(img_local)
                elif name=="cat":
                    print(name)
                    detect_type = "cat"
                    last_detec = "cat"
                    last_detec_time = current_time
                    img_name = 'Detection_Cat' +current_time+'.jpg'
                    img_local = img_folder + img_name
                    last_image_name = img_name
                    cv2.imwrite(img_local,frame)
                    img_path = 'camera1/'+img_name
                    data = {"Type" : detect_type ,"Last_Detection_Type" : last_detec ,"Last_Detect_time" : last_detec_time ,
                            "Image_name" : img_name , "Last_Image_Name" : last_image_name}
                    db.child("Detection").set(data)
                    storage.child(img_path).put(img_local)
                else :
                    detect_type = "none"
                    data = {"Type" : detect_type ,"Last_Detection_Type" : last_detec ,"Last_Detect_time" : last_detec_time ,
                            "Last_Image_Name" : last_image_name}
                    db.child("Detection").set(data)
    if ret2 :
        for r2 in result2:
            for c2 in r2.boxes.cls:
                name2 = model2.names[int(c2)]
                current_time = str(time.day)+'-'+str(time.month)+'-'+str(time.year)+'_'+str(time.hour)+':'+str(time.minute)+':'+str(int(time.second))
                if name2=="person":
                    print(name2)
                    detect_type2 = "person"
                    last_detec2 = "person"
                    last_detec_time2 = current_time
                    img_name2 = 'Detection_Person' +current_time+'.jpg'
                    img_local2 = img_folder2 + img_name2
                    last_image_name2 = img_name2
                    cv2.imwrite(img_local2,frame2)
                    img_path2 = 'camera2/'+img_name2
                    data2 = {"Type2" : detect_type2 ,"Last_Detection_Type2" : last_detec2 ,"Last_Detect_time2" : last_detec_time2 ,
                            "Image_name2" : img_name2 , "Last_Image_Name2" : last_image_name2}
                    db.child("Detection2").set(data2)
                    storage.child(img_path2).put(img_local2)
                elif name2=="cat":
                    print(name2)
                    detect_type2 = "cat"
                    last_detec2 = "cat"
                    last_detec_time2 = current_time
                    img_name2 = 'Detection_Cat' +current_time+'.jpg'
                    img_local2 = img_folder2 + img_name2
                    last_image_name2 = img_name2
                    cv2.imwrite(img_local2,frame2)
                    img_path2 = 'camera2/'+img_name2
                    data2 = {"Type2" : detect_type2 ,"Last_Detection_Type2" : last_detec2 ,"Last_Detect_time2" : last_detec_time2 ,
                            "Image_name2" : img_name2 , "Last_Image_Name2" : last_image_name2}
                    db.child("Detection2").set(data2)
                    storage.child(img_path2).put(img_local2)
                elif name2=="dog":
                    print(name2)
                    detect_type2 = "dog"
                    last_detec2 = "dog"
                    last_detec_time2 = current_time
                    img_name2 = 'Detection_Dog' +current_time+'.jpg'
                    img_local2 = img_folder2 + img_name2
                    last_image_name2 = img_name2
                    cv2.imwrite(img_local2,frame2)
                    img_path2 = 'camera2/'+img_name2
                    data2 = {"Type2" : detect_type2 ,"Last_Detection_Type2" : last_detec2 ,"Last_Detect_time2" : last_detec_time2 ,
                            "Image_name2" : img_name2 , "Last_Image_Name2" : last_image_name2}
                    db.child("Detection2").set(data2)
                    storage.child(img_path2).put(img_local2)
                else :
                    detect_type2 = "none"
                    data2 = {"Type2" : detect_type2 ,"Last_Detection_Type2" : last_detec2 ,"Last_Detect_time2" : last_detec_time2 ,
                             "Last_Image_Name2" : last_image_name2}
                    db.child("Detection2").set(data2)

    cv2.waitKey(1)

cap.release()
cap2.release()
cv2.destroyAllWindows()
