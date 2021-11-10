#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import cv2
import argparse
import numpy as np

def main():
    # Process arguments
    parser = argparse.ArgumentParser(description='Ask for image path')
    parser.add_argument('--image1', required=True, type=str, help='Path to image')
    args = vars(parser.parse_args())
    print(args)

    # # Ex 2a)
    # # Load image
    # image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    # image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
    # # Process image
    # retval, image_processed = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    #
    # # Visualization
    # cv2.imshow('Original', image_original)  # Display the image
    # cv2.imshow('Gray', image_gray)  # Display the image
    # cv2.imshow('Processed', image_processed)  # Display the image
    #
    # cv2.waitKey(0)  # wait for a key press before proceeding

    # # Ex 2b)
    # # Load image
    # image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    # image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
    # # Process image
    # _, image_processed = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    # image_thresholded = image_gray > 128
    #
    # # Visualization
    # print(type(image_original))
    # print(image_original.shape)
    # print('Tipo de dados imagem original: ')
    # print(image_original.dtype)
    # print('Tipo de dados imagem thresholded com opencv: ')
    # print( image_processed.dtype)
    # print('Tipo de dados imagem thresholded com numpy:  ')
    # print(image_thresholded.dtype)
    #
    # cv2.imshow('Original', image_original)  # Display the image
    # cv2.imshow('Processed with opencv', image_processed)  # Display the image
    # cv2.imshow('Processed with numpy', image_thresholded.astype(np.uint8) * 255)  # Display the image
    #
    # cv2.waitKey(0)  # wait for a key press before proceeding

    # # Ex 2c)
    # # Load image
    # image_original_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    # # Process image
    # image_b, image_g, image_r = cv2.split(image_original_rgb)
    #
    # _, image_processed_b = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    # _, image_processed_g = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    # _, image_processed_r = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)
    #
    # new_image_rgb = cv2.merge((image_processed_b, image_processed_g, image_processed_r))
    #
    # # Visualization
    #
    # cv2.imshow('Original', image_original_rgb)  # Display the image
    # cv2.imshow('Processed b', image_processed_b)  # Display the image
    # cv2.imshow('Processed g', image_processed_g)  # Display the image
    # cv2.imshow('Processed r', image_processed_r)  # Display the image
    # cv2.imshow('New image', new_image_rgb)  # Display the image
    #
    # cv2.waitKey(0)  # wait for a key press before proceeding

    # Ex 2d)
    # # Load image
    # image_original_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    # image_b, image_g, image_r = cv2.split(image_original_rgb)
    # ranges = {'b' : {'min' : 0 , 'max': 50},
    #           'g' : {'min' : 70, 'max' : 256},
    #           'r' : {'min' : 0, 'max' : 50}}
    #
    # # Process image
    # mins = np.array([ranges['b']['min'],ranges['g']['min'], ranges['r']['min']])
    # maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    # image_processed = cv2.inRange(image_original_rgb, mins, maxs)
    #
    # # Visualization
    #
    # cv2.imshow('Original', image_original_rgb)  # Display the image
    # cv2.imshow('Processed b', image_processed)  # Display the image
    #
    # cv2.waitKey(0)  # wait for a key press before proceeding

    # Ex 2e)
    # # Load image
    # image_original_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    # image_b, image_g, image_r = cv2.split(image_original_rgb)
    # image_hsv = cv2.cvtColor(image_original_rgb, cv2.COLOR_BGR2HSV)
    # ranges = {'b' : {'min' : 60 , 'max': 100},
    #           'g' : {'min' : 150, 'max' : 256},
    #           'r' : {'min' : 60, 'max' : 100}}
    #
    # # Process image
    # mins = np.array([ranges['b']['min'],ranges['g']['min'], ranges['r']['min']])
    # maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    # image_processed = cv2.inRange(image_hsv, mins, maxs)
    #
    # # Visualization
    #
    # cv2.imshow('Original', image_original_rgb)  # Display the image
    # cv2.imshow('Processed b', image_processed)  # Display the image
    #
    # cv2.waitKey(0)  # wait for a key press before proceeding

    # Ex 2f)
    # Load image
    image_original_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    image_b, image_g, image_r = cv2.split(image_original_rgb)
    ranges = {'b' : {'min' : 0 , 'max': 50},
              'g' : {'min' : 70, 'max' : 256},
              'r' : {'min' : 0, 'max' : 50}}

    # Process image
    mins = np.array([ranges['b']['min'],ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image_original_rgb, mins, maxs)
    # Conversion from numpy from uint8 to bool
    mask = mask.astype(np.bool)

    image_processed = image_original_rgb.copy()
    image_processed[mask] = (image_processed[mask] * 0.2).astype(np.uint8)

    print(image_original_rgb.dtype)
    print(mask.dtype)
    print(image_processed.dtype)

    # Visualization
    cv2.imshow('Original', image_original_rgb)  # Display the image
    cv2.imshow('Mask', mask.astype(np.uint8) * 255)  # Display the image
    cv2.imshow('Processed', image_processed)  # Display the image

    cv2.waitKey(0)  # wait for a key press before proceeding

if __name__ == '__main__':
    main()