#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import numpy as np
import cv2

isdown = False
color = (255, 0, 0)

def mouse_paint(event, x, y, flags, params):
    # print(x, y)
    global image, window_name, isdown, color
    if event == cv2.EVENT_MOUSEMOVE:
        if isdown == True:
            image[y, x] = color
    if event == cv2.EVENT_LBUTTONDOWN:
        isdown = True
    if event == cv2.EVENT_LBUTTONUP:
        isdown = False

def main():
    # Create white window
    global image, window_name, choice
    image = np.ones((400, 600, 3)) * 255    #rows and columms
    window_name = "Paint - Whiteboard"
    cv2.imshow(window_name, image)
    image = image.astype(np.uint8)
    print("Paint - Whiteboard")
    cv2.setMouseCallback(window_name, mouse_paint)
    while True:
        print("Colors to write: ")
        print("Press r for Red")
        print("Press g for Green")
        print("Press b for Blue")
        print("Press s to Stop")

        choice = cv2.waitKey(20);
        cv2.imshow(window_name, image)
        cv2.waitKey(20)
        print("Tecla pressionada: " + str(choice))
        if choice != -1:
            if choice == ord('S') or choice == ord('s'):
                break
            if choice == ord('R') or choice == ord('r'):
                color = (0, 0, 255)
            if choice == ord('G') or choice == ord('g'):
                color = (0, 255, 0)
            if choice == ord('B') or choice == ord('b'):
                color = (255, 0, 0)




if __name__ == '__main__':
    main()