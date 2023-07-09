import cmake
import face_recognition_models
import cv2
import numpy as np
import csv
import datetime as datetime
video_capture=cv2.VideoCapture(0)


#load known faces
tejas_img=face_recognition.load_image