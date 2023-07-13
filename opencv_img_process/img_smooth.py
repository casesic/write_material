import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
img=cv.imread('D:\Program Files\opencv\photo3.jpg')
#简单来说，滤波操作就是图像对应像素与掩膜（mask）的乘积之和。
#滤波步骤：1对原始图像的边缘进行某种方式的填充（一般为0填充）。2.将掩膜划过整幅图像，计算图像中每个像素点的滤波结果
kernel=np.ones((5,5),np.float32)/25
#cv.filter2D将核与图像融合
#dst=cv.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
dst=cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.show()
#卷积操作也是卷积核与图像对应位置的乘积和。但是卷积操作在做乘积之前，需要先将卷积核翻转180度，之后再做乘积,会改变图像大小
#卷积步骤：1.180度翻转卷积核。2.不做边界填充，直接对图像进行相应位置乘积和。
#1.均值模糊
blur=cv.blur(img,(5,5))
#2.高斯模糊
blur=cv.GaussianBlur(img,(5,5),0)
#3.中值模糊
median=cv.medianBlur(img,5)
#4.双边滤波，保留边缘
#参数：img,以当前像素点为中心点的直径,sigmaColor是滤波处理时选取的颜色差值范围,
# sigmaSpace是坐标空间中的sigma值。它的值越大，说明有越多的点能够参与到滤波计算中来。当d>0时，无论sigmaSpace的值如何，d都指定邻域大小；否则，d与 sigmaSpace的值成比例。
blur=cv.bilateralFilter(img,9,75,75)
