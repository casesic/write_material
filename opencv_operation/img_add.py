import cv2 as cv 
import numpy as np 
#opencv加法是一个饱和操作
x=np.uint8([250])
y=np.uint8([10])
print(cv.add(x,y))#250+10=260=>255
#numpy加法是一个模数操作
print(x+y)#250+10=260%256=4
img1=cv.imread('D:\Program Files\opencv\photo3.jpg')
img2=cv.imread('D:\Program Files\opencv\W2.jpg')
#图像相加dst=cv.addWeighted(src1, alpha, src2, beta,gamma, dst, dtype)
#dst(I)=saturate(src1(I)∗alpha+src2(I)∗beta+gamma)
dst=cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()