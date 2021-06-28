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
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
edges = cv.Canny(img,50,50)

'''imgp = cv.cvtColor(img0, cv.COLOR_BGR2RGB)
imgp = Image.fromarray(imgp)


colors, pixel_count = extcolors.extract_from_image(imgp)
print(colors)
print (pixel_count)'''
cv.imshow( "lap" , img0)
cv.waitKey(0)