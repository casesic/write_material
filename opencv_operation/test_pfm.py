import cv2 as cv
import numpy as np 
img=cv.imread('D:\Program Files\opencv\photo3.jpg')
#getTickCount函数返回一个参考事件(比如机器被打开的那一刻)到这个函数被调用的那一刻时钟周期的数量，如果你在函数之前和之后调用它，你可以得到执行一个函数所使用的时钟周期数
e1=cv.getTickCount() 
#range(start,stop,step)
for i in range(5,49,2):
    #medianBlur函数使用中值滤波器来平滑（模糊）处理一张图片，像素点邻域灰度值的中值来代替该像素点的灰度值
    #int ksize: 滤波模板的尺寸大小，必须是大于1的奇数，如3、5、7等
    img=cv.medianBlur(img,i)
e2=cv.getTickCount()
#getTickFrequency()：返回CPU一秒中所走的时钟周期数，因此可以以秒为单位对某运算时间计时。
t=(e2-e1)/cv.getTickFrequency()
cv.imshow('img',img)
cv.waitKey(0)
print(t)
cv.destroyAllWindows()

