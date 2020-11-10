from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
from cv2 import cv2


def Split2(image, wraped):
    img = image
    print(img.shape)
    # height = img.shape[0]
    height, width, _ = img.shape

    # Cut the image in half
    width_cutoff = width // 2
    s1 = img[30:height-10, 10:width_cutoff]
    s2 = img[30:height-10, width_cutoff:10]

    w1 = wraped[30:height, 10:width_cutoff]
    w2 = wraped[30:height, width_cutoff:10]

    return s1, s2, w1, w2


def Split3(image, wraped):
    pass
