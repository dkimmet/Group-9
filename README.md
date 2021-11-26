# Signature verification

This Application helps mathematically evaluate the similarity of the uploaded signature to the database. 
When a match doesn't reach 85% certainty, the program will open a single window for the user to compare the next closest match.
This program uses the skimage.metrics package.

# Prerequisites
## Install the following packages using pip
 1. python -m pip install -U scikit-image
 2. python -m pip install matplotlib
 3. python -m pip install scipy
 4. python -m pip install numpy


Original Source code this project was cloned from: https://github.com/omrawal/Signature-Matching
