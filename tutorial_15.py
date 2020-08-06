import cv2 as cv
import numpy as np


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down" + str(i),dst)
        temp = dst.copy()
    return pyramid_images


def lapalian_demo(image):           # 图片必须满足2^n的尺寸
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1,-1,-1):
        if(i-1) < 0:
            expand = cv.pyrUp(pyramid_images[i],dstsize=image.shape[:2])
            lpls = cv.subtract(image,expand)
            cv.imshow("lapalian_down_" + str(i),lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_images[i - 1], expand)
            cv.imshow("lapalian_down_" + str(i), lpls)

print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/lena.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
# pyramid_demo(src)
lapalian_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
