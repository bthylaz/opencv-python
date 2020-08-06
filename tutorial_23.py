import cv2 as cv
import numpy as np


def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))  # 水平线
    binary = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel=kernel)
    cv.imshow("open-result",binary)

# def open_demo(image):
#     print(image.shape)
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#     cv.imshow("binary", binary)
#     kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
#     dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel=kernel)
#     cv.imshow("open_demo", dst)


def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(30,30))
    binary = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("close-result",binary)

print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/zimu.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
open_demo(src)
# close_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
