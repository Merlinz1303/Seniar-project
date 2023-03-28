import cv2 
import parinya
import pyrebase
import time
import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

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

num = 0
last_detec = 'none'
last_image_name = 'none'
last_detec_time = 0

while True :
	_, frame = cap.read()
	model = yolo.detect(frame)
	cv2.imshow("Frame",frame)
	time = datetime.datetime.now()
	for d in model :
		current_time = str(time.day)+'-'+str(time.month)+'-'+str(time.year)+'_'+str(time.hour)+':'+str(time.minute)+':'+str(int(time.second))
		label,lrft,top,width,height = d
		a = d[0] 
		b = a[0] + a[1] + a[2]
		if num == 10 :
			num = 0
		if b == "per" :
			print(b)
			detec_type = "person"
			last_detec = "Person"
			last_detec_time = current_time
			img_name = 'Detection_Person_'+current_time+'.jpg'
			last_image_name = img_name
			cv2.imwrite('/home/merlinz/Desktop/code/img/'+img_name,frame)
			data = {"Type" : detec_type,"Last_Detection_Type" : last_detec,
						"Last_Detect_Time":last_detec_time,"Image_name" : img_name,"Last_Image_Name":last_image_name}
			img_path = 'image/'+img_name
			img_local = '/home/merlinz/Desktop/code/img/'+img_name
			db.child("Detection").set(data)	
			storage.child(img_path).put(img_local)
		if b == "dog" :
			print(b)
			detec_type = "dog"
			last_detec = "dog"
			last_detec_time = current_time
			img_name = 'Detection_Person_'+current_time+'.jpg'
			last_image_name = img_name
			cv2.imwrite('/home/merlinz/Desktop/code/img/'+img_name,frame)
			data = {"Type" : detec_type,"Last_Detection_Type" : last_detec,
						"Last_Detect_Time":last_detec_time,"Image_name" : img_name,"Last_Image_Name":last_image_name}
			img_path = 'image/'+img_name
			img_local = '/home/merlinz/Desktop/code/img/'+img_name
			db.child("Detection").set(data)	
			storage.child(img_path).put(img_local)
		if b == "cat" :
			print(b)
			detec_type = "cat"
			last_detec = "cat"
			last_detec_time = current_time
			img_name = 'Detection_Person_'+current_time+'.jpg'
			last_image_name = img_name
			cv2.imwrite('/home/merlinz/Desktop/code/img/'+img_name,frame)
			data = {"Type" : detec_type,"Last_Detection_Type" : last_detec,
						"Last_Detect_Time":last_detec_time,"Image_name" : img_name,"Last_Image_Name":last_image_name}
			img_path = 'image/'+img_name
			img_local = '/home/merlinz/Desktop/code/img/'+img_name
			db.child("Detection").set(data)	
			storage.child(img_path).put(img_local)
		else :
			detec_type = "none"
			data = {"Type" : detec_type,"Last_Detection_Type" : last_detec,
						"Last_Detect_Time":last_detec_time,"Last_Image_Name":last_image_name}
			db.child("Detection").set(data)		

	cv2.waitKey(1)
