import cv2 as cv
import numpy as np


def measure_object(image):
    dst = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(dst, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value: %s" % ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)  # 矩形的坐标获取
        rate = min(w, h) / max(w, h)
        print("rectangle rate : %s" % rate)
        mm = cv.moments(contour)
        print(type(mm))
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        # cv.rectangle(dst,(x,y),(x+w,y+h),(0,0,255),2)
        print("contour area %s" % area)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] > 6:
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
        if approxCurve.shape[0] == 4:
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)
        # if approxCurve.shape[0] == 3:
        #     cv.drawContours(dst,contours,i,(255,0,0),2)
    cv.imshow("measure-contours", dst)


print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/sanjiao.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
measure_object(src)

cv.waitKey(0)
cv.destroyAllWindows()
