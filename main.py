import cv2
import mss
import numpy
import time

from pynput.mouse import Button, Controller


def get_monitors():
    pass


def main():

    mouse = Controller()
    threshold = 0.90

    with mss.mss() as sct:

        while True:
            screenshot = numpy.array(sct.grab(sct.monitors[1]))
            icon_img = cv2.imread('icon.png', cv2.IMREAD_UNCHANGED)

            result = cv2.matchTemplate(screenshot, icon_img, cv2.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            print(max_val)
            print(max_loc)

            if max_val >= threshold:
                mouse.position = max_loc
                mouse.click(Button.left, 1)

            time.sleep(5)


if __name__ == "__main__":
    main()
