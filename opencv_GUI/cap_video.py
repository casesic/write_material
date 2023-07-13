#从摄像机中捕获视频
import numpy as np 
import cv2 as cv 
cap=cv.VideoCapture(0)#参数是设备索引，用来指定哪个摄像机，通常情况下会有一台摄像机被连接
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    #一帧一帧捕获
    ret,frame=cap.read()#cap.read()返回一个真假，如果该帧被正确读取将是true，通过返回值检查视频是否结束
    if not ret:
        print("Can't receive frame(stream end?). Exiting...")
        break
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#cvtColor实现颜色转换，灰度图
    cv.imshow('frame',gray)
    if cv.waitKey(1)==ord('q'):
        break
cap.release()#释放捕捉
cv.destroyAllWindows()
