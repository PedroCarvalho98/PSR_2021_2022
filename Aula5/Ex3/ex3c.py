#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import argparse
import cv2
import numpy as np
from functools import partial

# Global variables


def onTrackbar(threshold, image_src, window):
    # Add code here to threshold image_gray and show image in window
    _, image_thresholded = cv2.threshold(image_src, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window, image_thresholded)

def mouse_handler(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("X: " + str(x) + " Y: " + str(y))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window - Ex3a'
    image_gray = None

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    # add code to create the trackbar ...
    cv2.imshow('Original', image)  # Display the image
    cv2.createTrackbar("Trackbar Binary", window_name, 1, 255, partial(onTrackbar, image_src = image_gray, window = window_name))
    cv2.setMouseCallback(window_name, mouse_handler)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()