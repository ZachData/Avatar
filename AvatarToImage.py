import cv2
import os
import time
import numpy as np
from PIL import Image


path = r'C:\Users\M\Desktop\Avatar'
paths = []

for folders in os.walk(path):
	for videos in folders[2::3]:
		for video in videos:
			if video[-4:] == '.m4v': 
				# print(folders[0])
				# print(video)
				paths.append(folders[0] + '\\' + video)


for video in paths:
	print(video[:-4], 'video')
	os.mkdir(video[:-4])
	break
	vidcap = cv2.VideoCapture(video)
	def getFrame(sec):
		# vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*100)
		hasFrames,image = vidcap.read()
		if hasFrames:
			image = np.array(image)
			print(image)
			print(np.shape(image))
			# image = Image.fromarray(image)
			# image.show()
			# time.sleep(15)
			# cv2.imwrite("image"+str(count)+".jpg", image)	 # save frame as JPG file
		return hasFrames
	sec = 0
	frameRate = 12 #//it will capture image in each 0.5 second
	count=1
	success = getFrame(sec)
	while success:
		count = count + 1
		sec = sec + frameRate
		sec = round(sec, 2)
		success = getFrame(sec)
		print(count)
