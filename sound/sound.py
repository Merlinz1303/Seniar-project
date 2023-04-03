import sounddevice as sd
import wavio as wv
from scipy.io.wavfile import write
import wave 
import librosa 
import librosa.display
import soundfile as sf
import numpy as np
import matplotlib.pylab as plt
import time 
import pyrebase

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

freq = 44100
duration = 5 
detect_sound = float(34)
num = 0
while True :
	
	###### recording #######
	recording = sd.rec(int(duration * freq),samplerate = freq, channels=1)
	print ('start record')
	sd.wait()
	name = 'audio/recording'+str(num)+'.wav'
	write(name ,freq, recording)
	print('record complete')
	
	###### checking #######
	data, samplerate = librosa.load(name)
	data_trim, _ =librosa.effects.trim(data , top_db = 20)
	D = librosa.stft(data_trim)
	S_DB = librosa.amplitude_to_db(np.abs(D), ref=np.min)
	DB =  (S_DB[-1])
	print(DB[1])
	if DB[1] >= detect_sound  : 
		print ('Detection Sound' )
		audio_detect = {"Audio_Detection":"detect"}
		db.child("Audio_Detection").set(audio_detect)
		#audio_path = 'audio/'+name
		#storage.child(audio_path).put(data)
	else :
		audio_detect = {"Audio_Detection":"none"}
		db.child("Audio_Detection").set(audio_detect)
	num += 1
	#time.sleep(3)
	
