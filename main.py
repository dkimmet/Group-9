import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
import cv2
from numpy import result_type
from signature import match
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Mach Threshold
THRESHOLD = 85


def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)  # add this



def checkSimilarity(window, path1): #                  here path2

    result, path3 = match(path1=path1)  #              here   , path2=path2
    print(result)
    if(result <= THRESHOLD):
        messagebox.showerror("Signatures Do Not Match",
                             "No matching signatures! Signature file " + path3 +
                              " is the closest match at "+str(result)+f" %")
        
        img1 = cv2.imread(path1)
        img2 = cv2.imread(path3)
        # create figure
        fig = plt.figure(figsize=(10, 7))
        #fig = pylab.gcf()
        fig.canvas.manager.set_window_title('Human Verification')
  
        # setting values to rows and column variables
        rows = 1
        columns = 2

        fig.add_subplot(rows, columns, 1)
        plt.imshow(img1)
        plt.axis('off')
        plt.title("Received Signature from Doctor")

        # Adds a subplot at the 2nd position
        fig.add_subplot(rows, columns, 2)
    
        # showing image
        plt.imshow(img2)
        plt.axis('off')
        plt.title("Closest Signature Match")
        plt.show()
        #pass
    else:
        messagebox.showinfo("Success: Match Found",
                            "Signatures are "+str(result)+f" % similar!!")
    #return True


root = tk.Tk()
root.title("Group 9 Verify Doctor Signature")
root.geometry("500x400") # width x height
#center root window
root.update_idletasks()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
x = w/2 - size[0]/2
y = h/2 - size[1]/2
root.geometry("%dx%d+%d+%d" % (size + (x, y)))
#end of centering


uname_label = tk.Label(root, text="Please upload a signature to compare \nagainst the database. "
, font=("Helvetica", 14, "bold"))
uname_label.place(x=85, y=50)

img1_message = tk.Label(root, text="Signature path", font=("Helvetica", 14, "bold"))
img1_message.place(x=10, y=120)

image1_path_entry = tk.Entry(root, font=10)
image1_path_entry.place(x=150, y=120)

img1_browse_button = tk.Button(
    root, text="Browse", font=("Helvetica", 14), command=lambda: browsefunc(ent=image1_path_entry))
img1_browse_button.place(x=400, y=120)
"""
image2_path_entry = tk.Entry(root, font=10)
image2_path_entry.place(x=150, y=240)

img2_message = tk.Label(root, text="Signature 2", font=("Helvetica", 14, "bold"))
img2_message.place(x=10, y=250)


img2_browse_button = tk.Button(
    root, text="Browse", font=("Helvetica", 14), command=lambda: browsefunc(ent=image2_path_entry))
img2_browse_button.place(x=400, y=240)"""

compare_button = tk.Button(
    root, text="Compare", font=10, command=lambda: checkSimilarity(window=root,
                                                                   path1=image1_path_entry.get(),
                                                                   ))       # here path2=image2_path_entry.get(),

compare_button.place(x=200, y=320)
root.mainloop()
