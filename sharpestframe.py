import cv2 as cv
import numpy as np
import extcolors 
from PIL import Image

def fft(img) :
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    fft = np.fft.fftn(grey)
    fshift = np.fft.fftshift(fft,axes=(-2,-1))
    magnitude = 20 * np.log(np.abs(fshift))
    mean = np.mean(magnitude)
    rms = np.sqrt(np.mean(magnitude**2))
    return rms

cap = cv.VideoCapture("haha4.mp4")
length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
res, img0 = cap.read()
for i in range ( 1, length) :
    res ,img = cap.read()
    if (fft(img) > fft(img0)) :
       img0 = img
       print(i)

canny = cv.Canny(img0, 50, 50)  
# canny = cv2.resize(canny, (640, 480), cv2.INTER_AREA)
cv.imshow("Canny", canny)

M = cv.moments(canny)
cX, cY = 0, 0

if M['m00'] != 0:
    cX = int(M['m10']//M['m00'])
    cY = int(M["m01"]//M["m00"])

# print(cX, cY)
mask  = np.zeros(img0.shape[:2], dtype = "uint8")

img0 = cv.cvtColor(img0, cv.COLOR_BGR2HSV)
total_hue = 0
total_saturation = 0
total_value = 0
counter = 1
square = 20
for x in range(cX-square, cX+square):
    for y in range(cY-square, cY+square):
        if img0[x, y][1] :
            total_hue += img0[x, y][0]
            total_saturation += img0[x, y][1]
            total_value += img0[x, y][2]
            counter += 1
print(total_hue//counter, total_saturation//counter, total_value//counter)
img0 = cv.cvtColor(img0, cv.COLOR_HSV2BGR)
cv.circle(mask, (cX, cY), 20, (255, 255, 255), thickness=-1)
with_center = cv.bitwise_and(img0, img0, mask = mask)
cv.imshow("centroid", with_center)
cv.imshow( "lap" , img0)
cv.waitKey(0)
cv.destroyAllWindows()