import cv2
import time
import datetime
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import supervision as sv
import pyrebase


#cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

#cap2 = cv2.VideoCapture(1)
#cap2.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

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
box_annotator = sv.BoxAnnotator(thickness = 2 ,text_thickness = 2 ,text_scale = 1)

results = model.predict(source = "0" ,show =True)
results2 = model.predict(source = "1" ,show =True)

for r in result:
    name = model.names[int(c)]
    
print(name)

