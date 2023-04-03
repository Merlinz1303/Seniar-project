import cv2
import parinya
import pyrebase
import time
import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

cap2 = cv2.VideoCapture(1)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)


yolo = parinya.YOLOv3('coco.names','yolov3-tiny.cfg','yolov3-tiny.weights')

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
img_folder = '/home/merlinz/Desktop/open-cv/camera1'
last_detec2 = 'none'
last_image_name2 = 'none'
last_detec_time2 = 0
img_folder2 = '/home/merlinz/Desktop/open-cv/camera2'


while True :

    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    
    model = yolo.detect(frame)
    model2 = yolo.detect(frame2)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.imshow("Camera1",frame)
    cv2.imshow("Camera2",frame2)
    
    time = datetime.datetime.now()
    if ret :
        for d in model :
            current_time = str(time.day)+'-'+str(time.month)+'-'+str(time.year)+'_'+str(time.hour)+':'+str(time.minute)+':'+str(int(time.second))
            label,lrft,top,width,height = d
            a = d[0]
            b = a[0] + a[1] + a[2]
            if b=="per":
                print(b)
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
            elif b=="dog":
                print(b)
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
            elif b=="cat":
                print(b)
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
        for d2 in model2 :
            current_time = str(time.day)+'-'+str(time.month)+'-'+str(time.year)+'_'+str(time.hour)+':'+str(time.minute)+':'+str(int(time.second))
            label,lrft,top,width,height = d2
            a2 = d2[0]
            b2 = a2[0] + a2[1] + a2[2]
            if b2=="per":
                print(b2)
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
            elif b2=="cat":
                print(b2)
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
            elif b2=="dog":
                print(b2)
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

    if cv2.waitKey(1) == 27 & 0xFF == ord('q') :
        break

cap.release()
cap2.release()
cv2.destroyAllWindows()
