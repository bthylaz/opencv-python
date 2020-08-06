import cv2 as cv
import numpy as np


def lapalian_demo(image):
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    dst = cv.filter2D(image,cv.CV_32F,kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    # dst = cv.Laplacian(image,cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo",lpls)

def sobel_demo(image):
    grad_x = cv.Sobel(image,cv.CV_32F,1,0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x",gradx)
    cv.imshow("gradient-y", grady)

    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradient",gradxy)



print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/lena.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
# sobel_demo(src)
lapalian_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
