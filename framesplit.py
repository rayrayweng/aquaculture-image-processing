import math
import cv2
import os

count = 0
vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
if not os.path.exists(str(os.getcwd()) + "/frames"):
    os.mkdir(str(os.getcwd()) + "/frames")
while success:
    cv2.imwrite(str(os.getcwd()) + "/frames/frame%d.jpg" % count, image)
#    if os.path.exists(str(os.getcwd()) + "frame%d.jpg" % count):
#        os.remove(str(os.getcwd()) + "frame%d.jpg" % count)
#    else:
#        pass
    success,image = vidcap.read()
    count += 1
