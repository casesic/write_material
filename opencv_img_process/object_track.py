import cv2 as cv 
import numpy as np 
cap=cv.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    #inRange()用于将指定值范围的像素选出来。如果像素的值满足指定的范围，则这个像素点的值被置为255，否则值被置为0。三通道
    #dst = cv.inRange( src, lowerb, upperb[, dst] )
    mask=cv.inRange(frame,lower_blue,upper_blue)
    #mask掩膜对所选图像进行遮盖
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    #判断是否按下esc键
    k=cv.waitKey(5)&0xFF
    if k==27:
        break
cv.destroyAllWindows()