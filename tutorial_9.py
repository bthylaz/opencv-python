import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show("直方图")


def image_hist(image):
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [255], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 将图像从一个颜色空间转换为另一个颜色空间

    # 全局直方图均衡化，用于增强图像对比度，即黑的更黑，白的更白
    dst = cv.equalizeHist(gray)  # 均衡灰度图像的直方图
    cv.imshow("equalHist_demo", dst)

    # 局部直方图均衡化
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # 创建一个指向 cv: : CLAHE 类的智能指针并初始化它
    clahe_dst = clahe.apply(gray)
    cv.imshow("clahe", clahe_dst)
    # plt.hist(image.ravel(),256,[0,256])
    # plt.show("直方图")


# 创建直方图
def create_rgb_demo(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16 * 16 * 16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b / bsize) * 16 * 16 + np.int(g / bsize) * 16 + np.int(r / bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1

    return rgbHist


# 利用直方图比较相似性，用巴氏和相关性比较好
def hist_compare(image1, image2):
    hist1 = create_rgb_demo(image1)
    hist2 = create_rgb_demo(image2)
    match1 = cv.compareHist(hist1, hist2, method=cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, method=cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, method=cv.HISTCMP_CHISQR)
    print("巴氏距离：%s, 相关性: %s ,卡方:%s" % (match1, match2, match3))


print("--------------hi,python--------------")
src = cv.imread("E:/Camera Roll/opencv/1.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# image_hist(src)

image1 = cv.imread("E:/Camera Roll/opencv/2.png")
image2 = cv.imread("E:/Camera Roll/opencv/3.png")

hist_compare(image1, image2)
cv.imshow("image1", image1)
cv.imshow("image2", image2)

cv.waitKey(0)
cv.destroyAllWindows()
