# Signature verification

This Application helps mathematically evaluate the similarity of the uploaded signature to the database. 
When a match doesn't reach 85% certainty, the program will open a single window for the user to compare the next closest match.
This program uses the skimage.metrics package.

## Prerequisites
1. Python >=3.6
2. OpenCV
3. Scipy
4. Scikit-image


## Run
1. `pip install requirements.txt`
2. `python main.py`


Source code: https://github.com/omrawal/Signature-Matching
