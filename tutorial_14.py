import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)
    # 分成小块来处理
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row + ch, col:cw + col]
            # ret,dst = cv.threshold(roi,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU) #全局
            # 高于255赋值为白色
            # dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
            # gray[row:row + ch,col:cw + col] = dst
            print(np.std(roi), np.mean(roi))
            dev = np.std(roi)
            if dev < 15:
                gray[row:row + ch, col: col + cw] = 255
            else:
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 全局
                gray[row:row + ch, col:cw + col] = dst
    cv.imwrite("E:/Camera Roll/opencv/result_binary1.png", gray)


print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/big1.png")
# print(src)
# 先创建一个窗口，后加载图像
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# # 显示图像
# cv.imshow("input image", src)
big_image_binary(src)

cv.waitKey(0)
cv.destroyAllWindows()
