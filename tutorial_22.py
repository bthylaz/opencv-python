import cv2 as cv
import numpy as np

# 腐蚀
def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst  = cv.erode(binary,kernel)
    cv.imshow("erode_demo", dst)

def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst  = cv.dilate(binary,kernel)
    cv.imshow("dilate_demo", dst)

print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/shuzi.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)
erode_demo(src)
dilate_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
