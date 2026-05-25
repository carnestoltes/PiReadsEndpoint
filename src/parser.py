import re


def extract_values(text):

    result = {}

    patterns = {
        "temperature":
            r"TEMP(?:ERATURE)?\s*:?\s*([\d.]+)",

        "pressure":
            r"PRESS(?:URE)?\s*:?\s*([\d.]+)",

        "flow":
            r"FLOW\s*:?\s*([\d.]+)",

        "rpm":
            r"RPM\s*:?\s*([\d.]+)"
    }

    for key, pattern in patterns.items():

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            result[key] = float(match.group(1))

    return result
