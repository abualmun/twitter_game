from cv2 import COLOR_BGR2GRAY, ROTATE_180, ROTATE_90_CLOCKWISE, VideoCapture, flip
import numpy as np
import cv2 
import glob

start = 50

main = cv2.imread("main.jpg",1)
images = [cv2.imread(file) for file in glob.glob("avatars/*.png")]
height = int(main.shape[0])
width = int(main.shape[1])
print(main.shape)
test = cv2.line(main,(180,start),(width,start),(0,255,0),5)
# print(len(images))
# print(main)

cv2.imshow('test',main)
cv2.waitKey(0)

# output = main

cv2.imwrite('output.jpg',main)