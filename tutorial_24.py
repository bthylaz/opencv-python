import cv2 as cv
import numpy as np


def top_hat_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    # 提升亮度
    cimage = np.array(gray.shape,np.uint8)
    cimage = 100;
    dst = cv.add(dst,cimage)
    cv.imshow("tophat",dst)


print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/target.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
top_hat_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
