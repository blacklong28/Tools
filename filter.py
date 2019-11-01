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