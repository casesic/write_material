import numpy as np 
import cv2 as cv 
#创造一个黑色画布
img=np.zeros((512,512,3),np.uint8)#zeros(shape, dtype=float, order=‘C’)shape:形状，dtype:数据类型，可选参数，默认numpy.float64
#画一条蓝线
#lineType 表示绘制直线的线性，默认为 LINE_8
#shift 表示点坐标的小数位数，默认为 0。
#cv.line(img, pt1, pt2, color[, thickness=1, lineType=LINE_8, shift=0]) → img
cv.line(img,(0,0),(511,511),(255,0,0),5)
#长方形
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
#圆，中心坐标和半径，-1表示圆被填充
cv.circle(img,(477,63),63,(0,0,255),-1)
#椭圆# 参数 1.目标图片  2.椭圆圆心  3.长短轴长度  4.偏转角度  5.圆弧起始角度  6.终止角度  7.颜色  8.是否填充
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#多边形
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#-1 表示自适应该维度大小,返回一个 shape = (n, 1, 2) 的 ndarray
pts=pts.reshape((-1,1,2))
#第三个参数是False，得到连接所有点的折线，而不是封闭的形状
cv.polylines(img,[pts],True,(0,255,255))
#添加文本
font=cv.FONT_HERSHEY_SIMPLEX
#图像，文本，想放的位置的坐标，字体类型，字体大小，颜色，厚度，LineType
cv.putText(img,'OpenCv',(10,500),font,4,(255,255,255),2,cv.LINE_AA)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()


