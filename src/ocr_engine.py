import pytesseract

def read_text(image):

    config = (
        '--oem 3 '
        '--psm 6 '
        '-c preserve_interword_spaces=1'
    )

    return pytesseract.image_to_string(
        image,
        config=config
    )
