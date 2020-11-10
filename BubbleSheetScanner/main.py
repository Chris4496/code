# USAGE
# python test_grader.py --image images/test_01.png

# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
from cv2 import cv2
import time
import random


from wrapePaper import warpedPaper
from correctPaper import correct
from split import Split2

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                 help="path to the input image")
# args = vars(ap.parse_args())

# define the answer key which maps the question number
# to the correct answer


# load the image, convert it to grayscale, blur it
# slightly, then find edges
# image = cv2.imread("test_01.png")

# grab the test take


ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 2, 4: 1}
size = (525, 700)
CHOICE_PER_QUESTION = 5

image = cv2.imread("test_01.png")
paper, wraped = warpedPaper(image, (525, 700))
result = correct(paper, wraped, CHOICE_PER_QUESTION, ANSWER_KEY)
cv2.imshow("Exam", result)
cv2.waitKey(0)

# ------------------------------------------------------

ANSWER_KEY = {n: random.randint(0, 3) for n in range(17)}
print(ANSWER_KEY)
size = (810, 1440)
CHOICE_PER_QUESTION = 4

image = cv2.imread('bubbleTest4.jpg')
# cv2.imshow('test0', image)
paper, wraped = warpedPaper(image, (810, 1440))
cv2.imshow('test1', paper)
left, right, leftW, rightW = Split2(paper, wraped)
cv2.imshow('test2', left)
# cv2.imshow('test3', right)
# time.sleep(5000)
left_result = correct(left, leftW, CHOICE_PER_QUESTION, ANSWER_KEY)
cv2.imshow("test4", left_result)

cv2.waitKey(0)
