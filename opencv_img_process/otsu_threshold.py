import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
img=cv.imread('D:\Program Files\opencv\photo3.jpg',0)
ret1,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
ret2,th2=cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#cv.GaussianBlur( InputArray src, OutputArray dst, Size ksize,double sigmaX,(高斯核函数在X方向的标准偏差), double sigmaY = 0,int borderType = BORDER_DEFAULT );
blur=cv.GaussianBlur(img,(5,5),0)
ret3,th3=cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
images=[img,0,th1,
        img,0,th2,
        blur,0,th3]
titles=['Original Noisy Image','Histogram','Global Thresholding(v=127)',
        'Original Noisy Image','Histogram',"Ostu's Thresholding",
        'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,3*i+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
    #plt.hist()也就是这个作用。将一个大区间划分为等间隔的小区间，并统计每个区间上样本出现的频数之和。
    plt.subplot(3,3,3*i+2),plt.hist(images[i*3],256)
    plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,3*i+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([])
plt.show()
    