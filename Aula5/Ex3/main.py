#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import argparse
import cv2
import numpy as np

# Global variables
window_name = 'window - Ex3a'
image_gray = None


def onTrackbar(threshold):
    # Add code here to threshold image_gray and show image in window
    _, image_thresholded = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, image_thresholded)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    # add code to create the trackbar ...

    cv2.createTrackbar("Trackbar Binary", window_name, 1, 255, onTrackbar)
    cv2.imshow('Original', image)  # Display the image
    cv2.waitKey(0)

if __name__ == '__main__':
    main()