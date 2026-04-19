# Color Detection using OpenCV
This project performs real-time color detection using a webcam. It detects **blue, green, and red** objects in the frame, removes noise, and draws bounding boxes with labels.
<img width="1362" height="810" alt="Output2" src="https://github.com/user-attachments/assets/1457fd56-d29d-4e21-a7f9-d751d6b49568" />
<img width="1352" height="806" alt="Output3" src="https://github.com/user-attachments/assets/3a746697-e047-48ed-88d2-f34837ac3fbf" />
<img width="1356" height="800" alt="Output4" src="https://github.com/user-attachments/assets/2eb78d7e-a3c4-4fd2-82e3-16ff9ca45ff5" />
<img width="1362" height="674" alt="Output7" src="https://github.com/user-attachments/assets/715f6c96-debb-4c0b-8e00-1189362abc2d" />


## Features
- Real-time webcam capture
- HSV-based color segmentation
- Noise removal using morphological operations
- Contour detection with bounding boxes
- Supports multiple colors simultaneously

## Tech Stack
- Python
- OpenCV (`cv2`)
- NumPy

## How It Works
1. Capture video from webcam
2. Convert frame from BGR to HSV
3. Create masks for:
   - Blue
   - Green
   - Red (two ranges for HSV wrap-around)
4. Apply noise removal:
   - Morphological Opening
   - Morphological Closing
5. Detect contours
6. Draw bounding boxes and labels on detected objects
7. Display:
   - Original frame
   - Mask
   - Result (masked output)

## Noise Removal
- Kernel: `5x5`
- Operations:
  - Opening (removes small noise)
  - Closing (fills gaps)

## Usage
### Install dependencies
```bash
pip install opencv-python numpy
```
