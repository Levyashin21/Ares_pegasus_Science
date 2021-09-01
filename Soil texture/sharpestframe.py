import cv2 as cv
import numpy as np

# calculating fourier transformatuion
def fft(img) :
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    fft = np.fft.fftn(grey)
    fshift = np.fft.fftshift(fft,axes=(-2,-1))
    magnitude = 20 * np.log(np.abs(fshift))
    mean = np.mean(magnitude)
    rms = np.sqrt(np.mean(magnitude**2))
    return rms

# finding the sharpestest image
cap = cv.VideoCapture("haha4.mp4")
length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
res, img0 = cap.read()
for i in range ( 1, length) :
    res ,img = cap.read()
    if (fft(img) > fft(img0)) :
       img0 = img
    
cv.imshow( "lap" , img0)
cv.waitKey(0)
cv.destroyAllWindows()
