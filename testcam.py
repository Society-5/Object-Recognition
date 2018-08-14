import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import cv2 as cv
from utils import visualization_utils as vis_util

cap = cv.VideoCapture(0)
image_np = cap.read()
while True:
    cv.imshow('object_detection', image_np, cv.resize( (800,600)))
    if(cv.waitKey(25) and 0xFF == ord(q)):
        cv.destroyAllWindows()
        break
