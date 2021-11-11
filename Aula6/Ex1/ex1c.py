#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import numpy as np
import cv2


def mouse_paint(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        if params == 82 or params == 114:
            image[x, y] = (0, 0, 255)
        if params == 71 or params == 103:
            image[x, y] = (0, 255, 0)
        if params == 66 or params == 98:
            image[x, y] = (255, 0, 0)

def main():
    # Create white window
    global image
    image = np.ones((600, 400, 3)) * 255
    window_name = "Paint - Whiteboard"
    cv2.imshow(window_name, image)
    image = image.astype(np.uint8)
    print(image.dtype)
    print(image[0, 0][0])
    print("Paint - Whiteboard")

    while True:
        print("Colors to write: ")
        print("Press r for Red")
        print("Press g for Green")
        print("Press b for Blue")
        print("Press s to Stop")

        choice = cv2.waitKey(0);
        # print(choice)
        print("Tecla pressionada: " + chr(choice))
        if choice == 83 or choice == 115:
            break

        cv2.setMouseCallback(window_name, mouse_paint, choice)



if __name__ == '__main__':
    main()