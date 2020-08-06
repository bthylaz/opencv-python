import cv2 as cv
import numpy as np


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)  # 高斯双边
    cv.imshow("bi_demo", dst)


def shift_demo(image):  # 均值迁移
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)


if __name__ == '__main__':
    print("--------------hi,python--------------")
    src = cv.imread("E:/Camera Roll/opencv/1.png")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)

    bi_demo(src)
    shift_demo(src)
    cv.waitKey(0)
    cv.destroyAllWindows()
