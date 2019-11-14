#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# @author: lxz

# @Module function：根据图片尺寸过滤图片
# @Version:0.0.1
# @Date:20191101
# @Description 
# 过滤./img 文件夹下的图片
# 过滤条件 宽大于30像素 高大于80像素
# 并行化处理
# 将过滤以后的图片保存在./img_save文件夹下

import cv2
import sys
import os
from multiprocessing.dummy import Pool as ThreadPool

path = './img'
path_save = './img_save'

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
    pool = ThreadPool(10)
    results = pool.map(select, imgs)
    pool.close()
    pool.join()
