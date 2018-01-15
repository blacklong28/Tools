# -*- coding: utf-8 -*-
#本脚本用于裁剪脚本同路径下png、jpg格式图片，与鼠标继续互动，鼠标左键点击第一次为裁剪区域左上角，第二次为右下角。
#

import cv2
import os

global img
global point1, point2
def on_mouse(event, x, y, flags, param):
    global img, point1, point2
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        point1 = (x,y)
        cv2.circle(img2, point1, 10, (0,255,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
        cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:         #左键释放
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5) 
        cv2.imshow('image', img2)
        min_x = min(point1[0],point2[0])     
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        cut_img = img[min_y:min_y+height, min_x:min_x+width]
        cv2.imwrite('./crop/'+os.path.splitext(image_file)[0]+'_crop.jpg', cut_img)

def main():
    global img
    global image_file
    path= os.getcwd()
    path= os.path.join(path,'original')
    #
    for image_file in os.listdir(path):
        image_path = os.path.join(path,image_file)
        print("image_path==\n",image_path)
        if os.path.isdir(image_path):
            print("Error by lxz: Is a dir !\n")

        elif os.path.splitext(image_file)[1]!='.png':
            continue
        else:
            print("image_name==",image_file)
            img = cv2.imread(image_path)
            cv2.namedWindow('image')
            cv2.setMouseCallback('image', on_mouse)
            cv2.imshow('image', img)
            cv2.waitKey(0)


if __name__ == '__main__':
    main()

