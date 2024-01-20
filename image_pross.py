import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk
import cv2 


root = tk.Tk()
root.geometry("1000x600")
root.title("Image Processing Program")
root.config(bg="white")
file_path = ""


def add_image():
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")
    
def view_original():
    image = Image.open(file_path)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")    
    
def image_process():
    #replace with your func here
    image = cv2.imread(file_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    image = Image.fromarray(gray_image)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

left_frame = tk.Frame(root, width=200, height=600, bg="white")
left_frame.pack(side="left", fill="y")

canvas = tk.Canvas(root, width=750, height=600)
canvas.pack()

image_button = tk.Button(left_frame, text="Add Image", command=add_image, bg="white")
image_button.pack(pady=15)

image_orginal = tk.Button(left_frame, text="Orginal Image", command=view_original, bg="white")
image_orginal.pack(pady=15)

covert_button = tk.Button(left_frame, text="Convert Gray", command=image_process, bg="white")
covert_button.pack(pady=15)

save_button = tk.Button(left_frame, text="Save Image", bg="white")
save_button.pack(pady=15)

root.mainloop()
