## Alpha estimation from binary image masks:
Estimates alpha channel given RGB image and its corresponding binary mask.

## Requirements:
* Python3.6
* alphax

## Usage
* Install alphax latest version.
``` 
pip install alphax==2.0
``` 
* Use the below snippets to execute
``` 
from alphax.estimate import edge_estimator
import cv2

estimate_ = edge_estimator("alpha_data/image/RGB.jpg","alpha_data/mask/MASK.png")

cv2.imwrite("output_alpha.png",estimate_)
``` 
