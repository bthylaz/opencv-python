import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread("E:/Camera Roll/opencv/test2.png")
    target = cv.imread("E:/Camera Roll/opencv/target2.png")
    cv.imshow("template image", tpl)
    cv.imshow("target", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, 255, 2)
        cv.imshow("match-" + np.str(md), target)


print("--------------hi,python--------------")
# 读入图像
src = cv.imread("E:/Camera Roll/opencv/1.png")
# print(src)
# 先创建一个窗口，后加载图像
# cv.namedWindow("input image" ,cv.WINDOW_AUTOSIZE)
# 显示图像
# cv.imshow("input image", src)
template_demo()

cv.waitKey(0)
cv.destroyAllWindows()
