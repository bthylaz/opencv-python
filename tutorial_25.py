import cv2 as cv
import numpy as np


def watershed_demo():
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)
    # gray/binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    # 二值化 （ 灰度图，大于（小于）第二个参数赋值为第三个参数的颜色，方法）
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary-image", binary)

    # morphology operotion
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("mor-opt", sure_bg)

    # distance operation
    dist_transform = cv.distanceTransform(mb, 1, 5)
    ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    cv.imshow("sure-fg", sure_fg)

    # finding unkown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg, sure_fg)
    print("unknown : ", unknown)

    ret, markers1 = cv.connectedComponents(sure_fg)
    print(ret, markers1)

    # watershed transform
    markers = markers1 + 1
    markers[unknown == 255] = 0
    markers3 = cv.watershed(src, markers=markers)
    src[markers3 == -1] = [255, 0, 0]
    cv.imshow("result", src)


print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/circle.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
watershed_demo()

cv.waitKey(0)
cv.destroyAllWindows()
