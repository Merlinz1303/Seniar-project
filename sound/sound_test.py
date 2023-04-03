import sounddevice as sd
import wavio as wv
from scipy.io.wavfile import write
import wave 
import librosa 
import librosa.display
import soundfile as sf
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import IPython.display as ipd
from itertools import cycle
import seaborn as sns
import time 
import pyrebase

freq = 44100
duration = 5 
detect_sound = float(20)
num = 0
while True :
	
	###### recording #######
	recording = sd.rec(int(duration * freq),samplerate = freq, channels=1)
	print ('start record')
	sd.wait()
	name = 'recording'+str(num)+'.wav'
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
		
	num += 1
	#time.sleep(3)
	
