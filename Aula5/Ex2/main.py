#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import cv2
import argparse

def main():
    # Process arguments
    parser = argparse.ArgumentParser(description='Ask for image path')
    parser.add_argument('--image1', type=str, help='Path to image')
    args = vars(parser.parse_args())
    print(args)

    # Load image
    image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
    # Process image
    retval, image_processed = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    # Visualization
    cv2.imshow('Original', image_original)  # Display the image
    cv2.imshow('Gray', image_gray)  # Display the image
    cv2.imshow('Processed', image_processed)  # Display the image

    cv2.waitKey(0)  # wait for a key press before proceeding

if __name__ == '__main__':
    main()