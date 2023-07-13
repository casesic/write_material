import cv2 as cv 
import numpy as np 
import sys
cap=cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
fourcc=cv.VideoWriter_fourcc(*'XVID')#指定fourcc代码，fourcc是一个四字节的编码，用于指定视频的解编码器
out=cv.VideoWriter('output.avi',fourcc,20.0,(640,480))#输出指定文件名，指定fourcc代码，传定每秒的帧数和帧大小
while True:
    ret,frame=cap.read()
    if not ret:
        print("Can't not receive frame")
        break
    frame=cv.flip(frame,0)#帧翻转， 0-垂直方向翻转，1-水平方向翻转，-1-水平、垂直方向同时翻转
    out.write(frame)
    cv.imshow("frame",frame)
    if cv.waitKey(1)==ord('q'):
        break;
out.release()
cap.release()
cv.destroyAllWindows()
    