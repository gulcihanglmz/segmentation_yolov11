# Calculate Area with Segmentation Mask

This repository contains a script to calculate the fill ratio (percentage of white pixels) within a segmentation mask, after cropping a specified percentage of the mask's borders. The script processes images in bulk and saves the results with the calculated fill ratio displayed on the original images.

Additionally, it includes a reference to a script for converting COCO format annotations to YOLO format for use in object detection workflows.

---

## Features
- Crop segmentation masks by a given percentage from all edges.
- Calculate the percentage of white pixels (filled area) in the cropped mask.
- Overlay the calculated fill ratio on the original image.
- Process multiple images from a specified input folder.
- Save the processed images with the fill ratio annotation to an output folder.

---

## Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- NumPy

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/calculate-area-segmentation-mask.git
   cd calculate-area-segmentation-mask

## Download the script:
Follow the instructions provided in the JSON2YOLO repository for converting COCO annotations.
```bash
https://github.com/ultralytics/JSON2YOLO/blob/main/general_json2yolo.py


