import cv2 as cv 
import numpy as np 
img1=cv.imread('D:\Program Files\opencv\W2.jpg')
img2=cv.imread('D:/Program Files/opencv/tree.jpg')
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]
img2gray=cv.cvtColor(img2,cv.COLOR_BGR2BGRA)
#对单通道数组应用固定阈值操作cv.threshold(src, thresh, maxval, type[, dst])
#thresh	表示阈值，取值范围 0~255。
#maxval	表示填充色，取值范围 0～255，一般取255。
#type表示变换类型。1.cv.THRESH_BINARY表示大于阈值时置 255，否则置 0。
#dst表示返回阈值变换的输出图像。
ret,mask=cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
#bitwise_not(src,dst):是对二进制数据进行“非”操作
mask_inv=cv.bitwise_not(mask)
#cv2.bitwise_and(src1, src2, mask = None)mask：掩模图像，只有在需要对特定区域进行操作时才使用
img1_bg=cv.bitwise_and(roi,roi)
img2_fg=cv.bitwise_and(img2,img2)
dst=cv.add(img1_bg,img2_fg)#报错，不知道为啥
img1[0:rows,0:cols]=dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
