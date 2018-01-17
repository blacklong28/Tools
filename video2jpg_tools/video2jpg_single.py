#!/usr/bin/env python
# -*- coding: utf-8 -*-

#作者:blacklong617
#适用于视频个数少的情况
#将视频跳帧的转成图片

import os
import numpy as np

import cv2



cap = cv2.VideoCapture("./records/vlc-record-2017-11-14-11h36m49s-rtsp___192.168.0.130_live1.sdp-.mp4")
##
##
t = 0
#IMG_1279.MOV 0~1999  |||  IMG_1280.MOV 2000~3599 |||  IMG_1280.MOV 3600~
f = 0 
while(1):
    t = t+1
    f = f+1#
    # get a frame
    ret, frame = cap.read()
    ##跳帧部分
    if f <=8:
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
    cv2.imwrite("./image/"+'20171114113649'+name_str+".jpg",frame)
    #cv2.imwrite("./"+name_str+"re.jpg",frame_resize)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 
