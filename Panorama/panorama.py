""" this code was written by harshit batra 

as part of ares pegasus 1.0 rover """

import cv2 as cv 

images = []  # list to store images

for i in range (0,2) :      # storing three images 
    read = cv.imread(f"panorama{i}.jpg")
    images.append(read)   

panorama = cv.Stitcher_create()
status , panorama_img = panorama.stitch(images) #panorama img is final image
