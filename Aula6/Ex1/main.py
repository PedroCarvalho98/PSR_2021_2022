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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image

    if len(image.shape) > 2:
        height, width, _ = image.shape  # Vê se a imagem e a cores
    else:
        height, width = image.shape

    cv2.circle(image, (round(width/2), round(height/2)), 10, (0, 0, 255), -1)
    cv2.putText(image, "PSR", (round(width/2) - 30,round(height/4) - 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA )
    cv2.imshow("Window", image)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()