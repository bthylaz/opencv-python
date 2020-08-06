import cv2 as cv
import numpy as np


# 两张图片合并
def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


def logic_demo(m1, m2):
    # dst = cv.bitwise_and(m1,m2)
    # dst = cv.bitwise_or(m1,m2)
    image = cv.imread("E:/Camera Roll/opencv/1.png")
    cv.imshow("image1", image)
    dst = cv.bitwise_not(image)
    cv.imshow("logic_demo", dst)


def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1 - c, b)  # 参数分别为：图1，图1的权重，图2，图2的权重，权重和添加的值为3，输出图片sr
    cv.imshow("con_bri_demo", dst)


def others(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]

    print(M1)
    print(M2)

    print(dev1)
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


print("--------------hi,python--------------")
src1 = cv.imread("E:/Camera Roll/opencv/2.png")
src2 = cv.imread("E:/Camera Roll/opencv/3.png")
print(src1.shape)
print(src2.shape)
'''
	参数1：窗口的名字
	参数2：窗口类型，CV_WINDOW_AUTOSIZE 时表明窗口大小等于图片大小。不可以被拖动改变大小。
	CV_WINDOW_NORMAL 时，表明窗口可以被随意拖动改变大小。
'''
# cv.namedWindow("image1" ,cv.WINDOW_AUTOSIZE)
# cv.imshow("image1", src1)
# cv.imshow("image2", src2)
src = cv.imread("E:/Camera Roll/opencv/bea1.png")
cv.imshow("image2", src)
contrast_brightness_demo(src, 1.2, 10)  # 图片，对比度，亮度
# add_demo(src1,src2)
# subtract_demo(src1,src2)
# divide_demo(src1,src2)
# multiply_demo(src1,src2)
# others(src1,src2)
# logic_demo(src1,src2)


cv.waitKey(0)
cv.destroyAllWindows()
