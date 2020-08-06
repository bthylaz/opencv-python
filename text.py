'''
第一节学了基本图片的读入、显示、删除、保存
'''
import cv2 as cv
import numpy as np

print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/target.png")
# print(src)
# 先创建一个窗口，后加载图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图像
cv.imshow("input image", src)


cv.waitKey(0)
cv.destroyAllWindows()
