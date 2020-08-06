import cv2 as cv
import numpy as np


def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # cv.THRESH_BINARY_INV反选
    print("threshold value %s" % ret)
    cv.imshow("binary", binary)


def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("binary", binary)


# def threshold_custom(image):
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     h, w = gray.shape[:2]
#     m = np.reshape(gray, [1, w*h])
#     mean = m.sum() / (w*h)  # 求出整个灰度图像的平均值
#     print("mean:", mean)
#     ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
#     cv.imshow("threshold_custom", binary)

def threshold_custom(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (w * h)
    print("mean ：", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)  # cv.THRESH_BINARY_INV反选
    cv.imshow("binary", binary)


print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/target.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
# threshold_demo(src)
threshold_custom(src)
cv.waitKey(0)
cv.destroyAllWindows()
