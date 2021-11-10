#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import argparse
import json

import cv2
import numpy as np
from functools import partial

def onTrackbar_B_min(threshold, image_src, window, rang):
    rang['b']['min'] = threshold
    mins = np.array([rang['b']['min'], rang['g']['min'], rang['r']['min']])
    maxs = np.array([rang['b']['max'], rang['g']['max'], rang['r']['max']])
    mask = cv2.inRange(image_src, mins, maxs)
    cv2.imshow(window, mask)
def onTrackbar_B_max(threshold, image_src, window, rang):
    rang['b']['max'] = threshold
    mins = np.array([rang['b']['min'], rang['g']['min'], rang['r']['min']])
    maxs = np.array([rang['b']['max'], rang['g']['max'], rang['r']['max']])
    mask = cv2.inRange(image_src, mins, maxs)
    cv2.imshow(window, mask)
def onTrackbar_G_min(threshold, image_src, window, rang):
    rang['g']['min'] = threshold
    mins = np.array([rang['b']['min'], rang['g']['min'], rang['r']['min']])
    maxs = np.array([rang['b']['max'], rang['g']['max'], rang['r']['max']])
    mask = cv2.inRange(image_src, mins, maxs)
    cv2.imshow(window, mask)
def onTrackbar_G_max(threshold, image_src, window, rang):
    rang['g']['max'] = threshold
    mins = np.array([rang['b']['min'], rang['g']['min'], rang['r']['min']])
    maxs = np.array([rang['b']['max'], rang['g']['max'], rang['r']['max']])
    mask = cv2.inRange(image_src, mins, maxs)
    cv2.imshow(window, mask)
def onTrackbar_R_min(threshold, image_src, window, rang):
    rang['r']['min'] = threshold
    mins = np.array([rang['b']['min'], rang['g']['min'], rang['r']['min']])
    maxs = np.array([rang['b']['max'], rang['g']['max'], rang['r']['max']])
    mask = cv2.inRange(image_src, mins, maxs)
    cv2.imshow(window, mask)
def onTrackbar_R_max(threshold, image_src, window, rang):
    rang['r']['max'] = threshold
    mins = np.array([rang['b']['min'], rang['g']['min'], rang['r']['min']])
    maxs = np.array([rang['b']['max'], rang['g']['max'], rang['r']['max']])
    mask = cv2.inRange(image_src, mins, maxs)
    cv2.imshow(window, mask)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    parser.add_argument('-o', '--operation', action='store_true', help='Select HSV operation instead of BGR.\n')
    args = vars(parser.parse_args())
    # print(args)

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    window_name = 'window - Ex3d'
    image_to_process = None
    if args['operation']:   # if the user uses hsv operation
        image_to_process = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    else:
        image_to_process = image

    ranges = {'b' : {'min' : 100 , 'max': 200},
              'g' : {'min' : 100, 'max' : 200},
              'r' : {'min' : 100, 'max' : 200}}

    cv2.imshow('Original', image)  # Display the image
    cv2.imshow('To processed', image_to_process)  # Display the image

    cv2.createTrackbar("Min B/H", window_name, 1, 255, partial(onTrackbar_B_min, image_src = image_to_process, window = window_name, rang = ranges))
    cv2.createTrackbar("Max B/H", window_name, 1, 255, partial(onTrackbar_B_max, image_src = image_to_process, window = window_name, rang = ranges))
    cv2.createTrackbar("Min G/S", window_name, 1, 255, partial(onTrackbar_G_min, image_src = image_to_process, window = window_name, rang = ranges))
    cv2.createTrackbar("Max G/S", window_name, 1, 255, partial(onTrackbar_G_max, image_src = image_to_process, window = window_name, rang = ranges))
    cv2.createTrackbar("Min R/V", window_name, 1, 255, partial(onTrackbar_R_min, image_src = image_to_process, window = window_name, rang = ranges))
    cv2.createTrackbar("Max R/V", window_name, 1, 255, partial(onTrackbar_R_max, image_src = image_to_process, window = window_name, rang = ranges))

    cv2.waitKey(0)

    # file_name = 'limits.json'
    # with open(file_name, 'w') as file_handle:
    #     print('writing dictionary d to file ' + file_name)
    #     json.dump(ranges, file_handle)  # ranges is the dicionary

if __name__ == '__main__':
    main()