from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
from cv2 import cv2

ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 2, 4: 1}
CHOICE_PER_QUESTION = 5

image = cv2.imread("test_01.png")
image = cv2.resize(image, (525, 700))
