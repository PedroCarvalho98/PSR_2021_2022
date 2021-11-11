#!/usr/bin/python3
# -------------------------
# @Time      : $ {DATE} $ {TIME}
# @Author    : Pedro Carvalho
# -------------------------
import cv2

def main():
    # initial setup

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    capture = cv2.VideoCapture(0)
    window_name = 'A6-Ex3'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    while (True):
        _, image = capture.read()  # get an image from the camera
        height, width, _ = image.shape
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert to grayscale
        faces = face_cascade.detectMultiScale(gray, 1.1, 4) # Detect the faces
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # add code to show acquired image
        cv2.imshow(window_name,image)
        # add code to wait for a key press
        choice = cv2.waitKey(1)
        if choice == ord('q'):
            print("You pressed the letter q so you terminated the record")
            break

    capture.release()
if __name__ == '__main__':
    main()