import os
import cv2
from tkinter import messagebox
from skimage.metrics import structural_similarity as ssim
import numpy as np

def match(path1): #                                    
    # read the images
    img1 = cv2.imread(path1)
    # turn images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # resize images for comparison
    img1 = cv2.resize(img1, (100, 100))
    best_image = path1
    best_score = 0
    path = "./assets/"
    #for loop files in directory
    for image in os.listdir(path):
        # read the images
        if image.endswith(".png"):
            # read the images     
            imgDatabase = cv2.imread(path + image)
            imgDatabase = cv2.cvtColor(imgDatabase, cv2.COLOR_BGR2GRAY)
            imgDatabase = cv2.resize(imgDatabase, (100,100))
        # compare the images
            score = ssim(img1, imgDatabase)
            print(image, score)
            if score > 0.85:
                similarity_value = "{:.2f}".format(ssim(img1, imgDatabase)*100)
                messagebox.showinfo("Found","Signature file " + image + " matches")
                return float(similarity_value), path+image
            #find the best match
            if score > best_score:
                best_score = score
                best_image = image
                print("Print this here " + best_image, best_score) # remove later  
    return float(best_score), path + best_image

