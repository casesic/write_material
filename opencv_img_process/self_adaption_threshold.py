import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
#以灰度图读入，不然adaptiveThreahold报错
img=cv.imread('D:\Program Files\opencv\photo3.jpg',0)
#medianBulr中值滤波器
img=cv.medianBlur(img,5)
ret,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
#自适应阈值处理,阈值计算：cv.ADAPTIVE_THRESH_MEAN_C:阈值是邻近区域的平均值-C，cv.ADAPTIVE_THRESH_GAUSSIAN_C:阈值是邻域值的高斯加权和-C，邻域的大小，C
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
titles=['Original Image','Global Thresholding(v=127)','Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']
images=[img,th1,th2,th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
 