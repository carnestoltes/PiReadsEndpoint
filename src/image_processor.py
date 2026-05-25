# image_processor.py

import cv2
import numpy as np


def warp_perspective(frame, points):

    pts = points.reshape(4,2)

    width = 900
    height = 500

    dst = np.array([
        [0,0],
        [width,0],
        [width,height],
        [0,height]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(
        pts.astype("float32"),
        dst
    )

    warped = cv2.warpPerspective(
        frame,
        M,
        (width, height)
    )

    return warped


def preprocess(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.equalizeHist(gray)

    blur = cv2.GaussianBlur(
        gray,
        (3,3),
        0
    )

    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh
