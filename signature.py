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

    path = "./assets/"
    #for loop files in directory
    for file in os.listdir(path):
        # read the images
        score=0
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
                return float(similarity_value)


    
 #   similarity_value = "{:.2f}".format(ssim(img1, img2)*100)
    # print("answer is ", float(similarity_value),
    #       "type=", type(similarity_value))
  
    return float(0)


# ans = match("D:\\Code\\Git stuff\\Signature-Matching\\assets\\1.png",
#             "D:\\Code\\Git stuff\\Signature-Matching\\assets\\3.png")
# print(ans)
# print(type(ans))
