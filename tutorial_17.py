import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    xgray = cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygray = cv.Sobel(gray,cv.CV_16SC1,0,1)
    #edge
    edge_output = cv.Canny(xgray,ygray,50,150)
    cv.imshow("Canny Edge",edge_output)

    dst = cv.bitwise_and(image,image,mask=edge_output)
    cv.imshow("Color Edge",dst)     #彩色边缘


print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/target.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
edge_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()