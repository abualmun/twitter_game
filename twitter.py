from cv2 import COLOR_BGR2GRAY, ROTATE_180, ROTATE_90_CLOCKWISE, VideoCapture, flip
import numpy as np
import cv2 
import glob

v_start = 50
v_step = 70
h_start = 180
h_step = 50
main = cv2.imread("main.jpg",1)
images = [cv2.imread(file) for file in glob.glob("avatars/*.png")]
height = int(main.shape[0])
width = int(main.shape[1])

def add_image(main,image,category,order):
    w,h,c = image.shape

    image = cv2.resize(image,(70,70))
    if category < 2:
        v_start = 0
    if order > 8:
        category += 1
    x_offset=h_start + h_step * order
    y_offset = v_start + v_step * category
    main[y_offset:y_offset+image.shape[0], x_offset:x_offset+image.shape[1]] = image
    
    output = main
    return output
output = main
output = add_image(output,images[0],0,0)
# output = add_image(output,images[0],0,0)
cv2.imshow('a',add_image(main,images[0],0,0))


print(main.shape)
test = cv2.line(main,(180,v_start),(width,v_start),(0,255,0),5)
test = cv2.line(main,(180,v_start + v_step*2),(width,v_start+ v_step*2),(0,255,0),5)

# print(len(images))
# print(main)

# cv2.imshow('test',main)
cv2.waitKey(0)

# output = main

cv2.imwrite('output.jpg',main)