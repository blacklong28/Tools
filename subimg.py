
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import sys
import os
from multiprocessing.dummy import Pool as ThreadPool

path = './cloth_save'
path_save = './cloth_sub/cloth_sub_'

def select(img):

    img_path = os.path.join(path,img)
    if os.path.isdir(img_path):
        print("Error by lxz:Is a dir!\n")
    else:
        image = cv2.imread(img_path)
        print(image.shape)
        if image.shape[1]>30 and image.shape[0]>80:
            cv2.imwrite(path_save+'/'+img,image)

if os.path.isdir(path):
    imgs = os.listdir(path)
    # 并行运行
    # pool = ThreadPool(10)
    # results = pool.map(select, imgs)
    # pool.close()
    # pool.join()
    i=1
    
    for img in imgs:
        img_path = os.path.join(path,img)
        print("img No:{}".format(i))
        if os.path.isdir(img_path):
            print("Error by lxz:Is a dir!\n")
        else:
            image = cv2.imread(img_path)
        if i%10 == 1:
            cv2.imwrite(path_save+'1'+'/'+img,image)
        if i%10 == 2:
            cv2.imwrite(path_save+'2'+'/'+img,image)
        if i%10 == 3:
            cv2.imwrite(path_save+'3'+'/'+img,image)
        if i%10 == 4:
            cv2.imwrite(path_save+'4'+'/'+img,image)
        if i%10 == 5:
            cv2.imwrite(path_save+'5'+'/'+img,image)
        if i%10 == 6:
            cv2.imwrite(path_save+'6'+'/'+img,image)
        if i%10 == 7:
            cv2.imwrite(path_save+'7'+'/'+img,image)
        if i%10 == 8:
            cv2.imwrite(path_save+'8'+'/'+img,image)
        if i%10 == 9:
            cv2.imwrite(path_save+'9'+'/'+img,image)
        if i%10 == 0:
            cv2.imwrite(path_save+'10'+'/'+img,image)

        i +=1
