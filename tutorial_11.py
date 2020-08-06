import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 统计和绘制2D直方图
def hist2d_dem(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [32, 32], [0, 180, 0, 256])  # bins可调，调到自己喜欢的效果
    # cv.imshow("hist2d",hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histgram")
    plt.show()


# 直方图的反向投影
def back_projection_demo():
    sample = cv.imread("E:/Camera Roll/opencv/sample.png")
    target = cv.imread("E:/Camera Roll/opencv/target.png")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show images
    cv.imshow("sample", sample)
    cv.imshow("target", target)

    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])  # 绘制2D直方图
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)  # 归一化
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)  # 反向投影
    cv.imshow("backProjectionDemo", dst)


print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/target.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)

hist2d_dem(src)
# back_projection_demo()

cv.waitKey(0)
cv.destroyAllWindows()
