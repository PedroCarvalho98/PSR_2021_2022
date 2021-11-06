#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='Ask for image path')
    parser.add_argument('--image1', type=str, help='Path to image')
    args = vars(parser.parse_args())
    print(args)

    image = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image

    cv2.imshow('window', image)  # Display the image

    image_bright = image + 20
    cv2.imshow('window2', image_bright)  # Display the image_bright

    # cv2.waitKey(0)  # wait for a key press before proceeding
    cv2.waitKey(1000)  # wait for 1000 ms
    cv2.destroyAllWindows()

    print(type(image))
    print(image.shape)

    image2 = cv2.imread('../images/atlascar.png', cv2.IMREAD_COLOR)  # Load an image
    image3 = cv2.imread('../images/atlascar2.png', cv2.IMREAD_COLOR)  # Load an image
    cv2.imshow('window3', image2)  # Display the image
    cv2.waitKey(3000)  # wait for 1000 ms
    cv2.imshow('window3', image3)  # Display the image
    cv2.waitKey(3000)  # wait for 1000 ms

if __name__ == '__main__':
    main()