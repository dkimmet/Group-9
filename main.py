import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
import cv2
from numpy import result_type
from signature import match


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

#removed def capture_image_from_cam_into_temp(sign=1):

# def captureImage(ent,sign=1);



def checkSimilarity(window, path1, path2):
    result = match(path1=path1, path2=path2)
    if(result <= THRESHOLD):
        messagebox.showerror("Failure: Signatures Do Not Match",
                             "Signatures are "+str(result)+f" % similar!!")
        pass
    else:
        messagebox.showinfo("Success: Signatures Match",
                            "Signatures are "+str(result)+f" % similar!!")
    return True


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


uname_label = tk.Label(root, text="Please select two signatures to compare:", font=("Helvetica", 14, "bold"))
uname_label.place(x=90, y=50)

img1_message = tk.Label(root, text="Signature 1", font=10)
img1_message.place(x=10, y=120)

image1_path_entry = tk.Entry(root, font=10)
image1_path_entry.place(x=150, y=120)

img1_capture_button = tk.Button(
    root, text="Capture", font=10, command=lambda: captureImage(ent=image1_path_entry, sign=1))
img1_capture_button.place(x=400, y=90)

img1_browse_button = tk.Button(
    root, text="Browse", font=10, command=lambda: browsefunc(ent=image1_path_entry))
img1_browse_button.place(x=400, y=140)

image2_path_entry = tk.Entry(root, font=10)
image2_path_entry.place(x=150, y=240)

img2_message = tk.Label(root, text="Signature 2", font=10)
img2_message.place(x=10, y=250)

img2_capture_button = tk.Button(
    root, text="Capture", font=10, command=lambda: captureImage(ent=image2_path_entry, sign=2))
img2_capture_button.place(x=400, y=210)

img2_browse_button = tk.Button(
    root, text="Browse", font=10, command=lambda: browsefunc(ent=image2_path_entry))
img2_browse_button.place(x=400, y=260)

compare_button = tk.Button(
    root, text="Compare", font=10, command=lambda: checkSimilarity(window=root,
                                                                   path1=image1_path_entry.get(),
                                                                   path2=image2_path_entry.get(),))

compare_button.place(x=200, y=320)
root.mainloop()
