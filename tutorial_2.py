import cv2 as cv
import numpy as np


def access_pixels(image):  # 改变像素
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height: %s channel:%s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixel_demo", image)


def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)


def create_image():
    '''
    img = np.zeros([400,400,3],np.uint8)
    cv.imshow("new image",img)
    # img[: , : , 0] = np.ones([400,400])*255
    img[:, :, 2] = np.ones([400, 400]) * 255
    cv.imshow("new image",img)

    img = np.ones([400,400,1],np.uint8)
    img = img * 0
    cv.imshow("new image",img)
    cv.imwrite("E:/Camera Roll/demo.png",img)
    '''
    m1 = np.ones([3, 3], np.uint8)
    m1.fill(12222.38)
    print(m1)

    m2 = m1.reshape([1, 9])
    print(m2)


print("--------------hi,python--------------")
src = cv.imread("E:/Camera Roll/opencv/1.png")  # blue green red
cv.namedWindow("input image", cv.WINDOW_NORMAL)
cv.imshow("input image", src)
t1 = cv.getTickCount()
access_pixels(src)
create_image()
inverse(src)
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency()
print("time : %s ms" % (time * 1000))
cv.waitKey(0)
cv.destroyAllWindows()
