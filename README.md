## Pi Reads Endpoint

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4GB-6cc04a?logo=raspberrypi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)
![Tesseract](https://img.shields.io/badge/OCR-Tesseract-lightgrey)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![JSON](https://img.shields.io/badge/Output-JSON-000000?logo=json&logoColor=white)

## Requirements
- Raspberry Pi 4 or 5 (recommend with 4 GB of RAM at least)
- Pi Camera

## System Architecture

```mermaid
flowchart TD

A[Camera image] --> B[Find display / screen region]
B --> C[Perspective correction] --> |crop and straighten| D[Resize to standard size]
D --> E[OCR / digit detection]
E --> F[Parse values]
F --> G[GET /values] --> |JSON|
```

## Software Stack

- Python
- [OpenCV](https://opencv.org/)
- [Tesseract OCR](https://tesseract-ocr.github.io/)
- [FastAPI](https://fastapi.tiangolo.com/)

