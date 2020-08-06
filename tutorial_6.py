import cv2 as cv
import numpy as np


def blur_demo(image):  # 均值模糊
    dst = cv.blur(image, (15, 1))
    cv.imshow("blur_demo", dst)


def median_blur_demo(image):  # 中值模糊（椒盐噪声）
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)


def custom_blur_demo(image):
    # photo = np.ones([5,5],np.float32)/25
    # photo = np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)   #锐化
    photo = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
    dst = cv.filter2D(image, -1, kernel=photo)
    cv.imshow("custom_blur_demo", dst)


print("--------------hi,python--------------")
src = cv.imread("E:/Camera Roll/opencv/1.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# blur_demo(src)
# median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
