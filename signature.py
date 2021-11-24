import os
import cv2
from tkinter import messagebox
from skimage.metrics import structural_similarity as ssim


# TODO add contour detection for enhanced accuracy


def match(path1, path2):
    # read the images
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    # turn images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # resize images for comparison
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    best_file = path1
    best_score = 0
    path = "./assets/"
    #for loop files in directory
    for file in os.listdir(path):
        # read the images
        #score=0    might be needed for future use-------
        if file.endswith(".png"):
            print(file)
            # read the images     
            img3 = cv2.imread(path + file)
            img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
            img3 = cv2.resize(img3, (300, 300))
        # compare the images
            score = ssim(img1, img3)
            print(file, score)
            if score > 0.85:
                similarity_value = "{:.2f}".format(ssim(img1, img3)*100)
                messagebox.showinfo("Found","Signature file " + file + " matches")
                return float(similarity_value), path+file
            #find the best match
            if score > best_score:
                best_score = score
                best_file = file
                print("Print this here " + best_file, best_score) # remove later


  
    return float(best_score), path + best_file

