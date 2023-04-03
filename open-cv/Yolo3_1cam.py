import cv2
import parinya
import pyrebase
import time
import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1440)


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
img_folder = '/home/merlinz/Desktop/open-cv/camera1/'


while True :

    ret, frame = cap.read()
    
    model = yolo.detect(frame)

    cv2.imshow("Camera1",frame)
    
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
                storage.child('Detection_Output').put(img_local)
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
                storage.child('Detection_Output').put(img_local)
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
                storage.child('Detection_Output').put(img_local)
            else :
                detect_type = "none"
                img_name = 'Car' +current_time+'.jpg'
                cv2.imwrite(img_local,frame)
                img_path = 'camera1/'+img_name
                data = {"Type" : detect_type ,"Last_Detection_Type" : last_detec ,"Last_Detect_time" : last_detec_time ,
                        "Last_Image_Name" : last_image_name}
                db.child("Detection").set(data)
                storage.child('Detection_Output').put(img_local)
        current_time = str(time.day)+'-'+str(time.month)+'-'+str(time.year)+'_'+str(time.hour)+':'+str(time.minute)+':'+str(int(time.second))
        detect_type = "none"
        img_name = 'Car' +current_time+'.jpg'
        img_local = img_folder + img_name
        cv2.imwrite(img_local,frame)
        img_path = 'camera1/'+img_name
        data = {"Type" : detect_type ,"Last_Detection_Type" : last_detec ,"Last_Detect_time" : last_detec_time ,
                "Last_Image_Name" : last_image_name}
        db.child("Detection").set(data)
        storage.child('Detection_Output').put(img_local)

    if cv2.waitKey(1) == 27 & 0xFF == ord('q') :
        break

cap.release()
cap2.release()
cv2.destroyAllWindows()
