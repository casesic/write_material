import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
img=cv.imread('D:\Program Files\opencv\W2.jpg')
#缩放dst = cv.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
#参数:dsize缩放后的图像大小,dst但是在 Python 里面没有任何意义。一般不传参或者设成 None,fx, fy :x 和 y 方向上的缩放比例，
res=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)#cv.INTER_CUBIC(慢速)
#或者
height,width=img.shape[:2]
res=cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)
#平移，
rows,cols=img.shape[:2]
M=np.float32([[1,0,100],[0,1,50]])
#位移为(100,50),cv.warpAffine()第三个参数是输出图像的大小，是(宽度，高度)的形式，宽度=列数，高度=行数
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
#旋转, 第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例,来c获得变换矩阵
M1=cv.getRotationMatrix2D(((cols-1)/2,(rows-1)/2),90,1)
ans=cv.warpAffine(img,M1,(cols,rows))
cv.imshow('ans',ans)
cv.waitKey(0)
#仿射变换,平行线在输出图像仍是平行线
rows,cols,ch=img.shape
pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
M2=cv.getAffineTransform(pts1,pts2)
dst1=cv.warpAffine(img,M2,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst1),plt.title('Output')
plt.show()
#透视变换,直线在变换后仍为直线
pts1=np.float32([[56,65],[368,52],[28,387],[289,390]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])
M3=cv.getPerspectiveTransform(pts1,pts2)
dst2=cv.warpPerspective(img,M3,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input1')
plt.subplot(122),plt.imshow(dst2),plt.title('Output')
plt.show()
cv.destroyAllWindows()


