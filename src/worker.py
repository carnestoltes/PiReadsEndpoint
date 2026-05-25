# worker.py

import time

from camera import Camera
from hmi_detector import find_hmi_screen
from image_processor import (
    warp_perspective,
    preprocess
)

from ocr_engine import read_text
from parser import extract_values


latest_data = {}

camera = Camera()


def worker_loop():

    global latest_data

    while True:

        frame = camera.get_frame()

        if frame is None:
            continue

        screen = find_hmi_screen(frame)

        if screen is None:

            latest_data = {
                "screen_found": False
            }

            time.sleep(1)
            continue

        warped = warp_perspective(
            frame,
            screen
        )

        processed = preprocess(
            warped
        )

        text = read_text(
            processed
        )

        values = extract_values(
            text
        )

        latest_data = {
            "screen_found": True,
            "values": values,
            "raw_text": text,
            "timestamp": time.time()
        }

        time.sleep(1)
