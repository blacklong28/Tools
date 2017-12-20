#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np

import cv2
##修改handle.py
##由于处理的视频较多，故添加功能：可以自动读取同目录下所有视频，并按规律命名

##path为视频所在路径
path="../SAOD_Cut_Video"
for video_file in os.listdir(path):
	p = 0 
	video_path = os.path.join(path,video_file)
	if os.path.isdir(video_path):
		print("Error by lxz:Is a dir!\n")
	else:
		p=p+1
		cap = cv2.VideoCapture(video_path)
		t = 0
		f = 0 
		while(1):
			t = t+1
			f = f+1#跳帧
			# get a frame
			ret, frame = cap.read()
			#跳帧部分 每跳5帧取一帧
			if f <=5:
				continue
			f = 0
			if ret == False:
				print('ret==False')
				break 
			# show a frame
			cv2.imshow("capture", frame)
			#frame_resize = cv2.resize(frame,(960,540))
			if t <=9:
				name_str = '00000'+str(t)
			elif t>=10 and t<=99:
				name_str = '0000'+str(t)
			elif t>=100 and t<=999:
				name_str = '000'+str(t)
			elif t>=1000 and t<=9999:
				name_str = '00'+str(t)
			elif t>=10000 and t<=99999:
				name_str = '0'+str(t)
			cv2.imwrite("./images/"+os.path.splitext(video_file)[0]+name_str+".jpg",frame)
			#cv2.imwrite("./"+name_str+"re.jpg",frame_resize)
			if cv2.waitKey(100) & 0xFF == ord('q'):
				break
		cap.release()
		cv2.destroyAllWindows() 

