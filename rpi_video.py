from picamera import PiCamera
from subprocess import Popen, PIPE
import threading
from time import sleep
import os, fcntl
import cv2

iframe = 0

camera = PiCamera()

#Yolo v3 is a full convolutional model. It does not care the size of input image, as long as h and w are multiplication of 32

#camera.resolution = (160,160)
#camera.resolution = (416, 416)
#camera.resolution = (544, 544)
camera.resolution = (608, 608)
#camera.resolution = (608, 288)

sleep(0.1)

#spawn darknet process
yolo_proc = Popen(["./darknet",
            "detect",
            "./cfg/yolov3-tiny.cfg",
            "./yolov3-tiny.weights",
            "-thresh","0.1"],
            stdin = PIPE, stdout = PIPE)
fcntl.fcntl(yolo_proc.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

def predict():
	try:
		camera.capture('frame.jpg')
		yolo_proc.stdin.write('frame.jpg')
	except Exception:
        	pass

predict()
