# '/Users/chenbingan/Documents/TechX/Hackathon/files/口述电影43号 2020-08-08 20.49.05.mp4'
# 
from moviepy.editor import *
# 没错仍旧是moviepy
import re
from tk import *
import wave
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import scipy.io.wavfile as wavf


start_time = time.time()
test_path = 'filepath'
moviefile = 'filepath'

start_time1 = time.time()

def extract_audio(moviefile):
	video = VideoFileClip(moviefile)
	audio = video.audio
	target_path = re.sub('.mp4', '.wav', moviefile)
	# same path as the file (initialized but could be changed)
	audio.write_audiofile(target_path)
	
	return target_path
end_time1 = time.time()
print("Time of the first: " + str(end_time1 - start_time1))

start_time2 = time.time()
def get_framrate(moviefile):
	start_time2 = time.time()
	f = wave.open(extract_audio(moviefile))
	SampleRate = f.getframerate()
	return SampleRate
end_time2 = time.time()
print("time of the second: " + str(end_time2 - start_time2))



# moviefile is the import variable from the website
start_time3 = time.time()
def read_wave_data(file_path):
	import time
	start_time3 = time.time()
	#open a wave file, and return a Wave_read object
	f = wave.open(file_path,"rb")
	#read the wave's format infomation,and return a tuple
	params = f.getparams()
	#get the info
	nchannels, sampwidth, framerate, nframes = params[:4]
	#Reads and returns nframes of audio, as a string of bytes. 
	str_data = f.readframes(nframes)
	#close the stream
	f.close()
	#turn the wave's data to array
	wave_data = np.fromstring(str_data, dtype = np.short)
	#for the data is stereo,and format is LRLRLR...
	#shape the array to n*2(-1 means fit the y coordinate)
	wave_data.shape = -1, 2
	#transpose the data
	wave_data = wave_data.T
	#calculate the time bar
	time = np.arange(0, nframes) * (1.0/framerate)
	
	return wave_data
end_time3 = time.time()
print("Time of the third: " + str(end_time3 - start_time3))


start_time4 = time.time()
def get_num(out_path):
	ou1 = (read_wave_data(extract_audio(out_path)))[0]

	#ou2 = (read_wave_data(extract_audio(out_path)))[1]
	
	return ou1
end_time4 = time.time()
print("Time of the fourth" + str(end_time4 - start_time4))


start_time5 = time.time()
def set_bond_filt(target_array):
	

	filted_array = []
	cout = 0
	cout2 = 0
	for i in list(target_array):
		if True:
			cout2 += (1/44100)
		if i < 100:
			filted_array.append(i)
			cout += (1/44100)

	
	

	return filted_array, cout, cout2
end_time5 = time.time()
print("Time of the fifth: " + str(end_time5 - start_time5))


start_time6 = time.time()
def array_to_audio(samples):

	fs = get_framrate(moviefile)
	out_f = 'filepath'
	wavf.write(out_f, fs, samples)
	
	
end_time6 = time.time()
print("Time of the sixth" + str(end_time6 - start_time6))



start_time7 = time.time()
def make_label(end_list):
	
	blank_labels = []

	for data_point in range(1, len(end_list)):

		blank_labels.append(data_point / 44100)
	
	


	return blank_labels
end_time7 = time.time()
print("Time of the seventh: " + str(end_time7 - start_time7))

start_timen = time.time()
c = (read_wave_data(extract_audio(test_path)))[0]
hihiiiiii = list((read_wave_data(extract_audio(test_path)))[0])
end_timen = time.time()
print("Total Time (maybe): " + str(end_timen - start_timen))


start_time8 = time.time()
def match():
	
	pointer_b = 0
	pointer_c = 0
	d = []

	while pointer_c < len(c):
		val = c[pointer_c]
		while True:
			if (make_label(hihiiiiii))[pointer_b] == val:
				d.append(hihiiiiii[pointer_b])
				pointer_b += 1
				break
			else:
				pointer_b += 1
		pointer_c += 1
		return d

match()

end_time8 = time.time()
print("time of the last " + str(end_time8 - start_time8))

# -------------- print(match())

# print('Type:' + str(type((read_wave_data(extract_audio(test_path)))[0])))

# print(make_label(hihiiiiii))


'''
array_to_audio(np.array(set_bond_filt(get_num(test_path))[0]))
print('\u001b[31m' + str(set_bond_filt(get_num(test_path))[1]) + '\u001b[37m')
print('\u001b[31m' + str(set_bond_filt(get_num(test_path))[2]) + '\u001b[37m')
'''

end_time = time.time()

print(('\u001b[33m -------> Total Time : ' + str(end_time - start_time) + '\u001b[37m'))