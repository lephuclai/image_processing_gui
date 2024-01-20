import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2 


root = tk.Tk()
root.geometry("1000x600")
root.title("Image Processing Program")
root.config(bg="white")
file_path = ""
file_name = ""

def add_image():
    global file_path
    file_path = filedialog.askopenfilename()
    
    global file_name 
    file_name = file_path
    file_name = file_name.split('.')[0]
    
    global org_image
    org_image = Image.open(file_path)
    
    canvas.config(width=org_image.width, height=org_image.height)
    image = ImageTk.PhotoImage(org_image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")
    
def view_original():
    image = org_image
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
    
def save_as_png(canvas):
    # save postscipt image 
    canvas.postscript(file=file_name + '.eps', pagewidth=org_image.width, pageheight=org_image.height) 
    # use PIL to convert to PNG 
    img = Image.open(file_name + '.eps') 
    # img.convert()
    img.save(file_name + '_result.png', 'png') 
    
left_frame = tk.Frame(root, width=200, height=600, bg="white")
left_frame.pack(side="left", fill="y")

canvas = tk.Canvas(root, width=750, height=600)
canvas.pack()

image_button = tk.Button(left_frame, text = "Add Image", command = add_image, bg = "white")
image_button.pack(pady=15)

image_orginal = tk.Button(left_frame, text = "Orginal Image", command=view_original, bg = "white")
image_orginal.pack(pady=15)

covert_button = tk.Button(left_frame, text = "Convert Gray", command=image_process, bg = "white")
covert_button.pack(pady=15)

save_button = tk.Button(left_frame, text = "Save Image", command = lambda: save_as_png(canvas), bg = "white")
save_button.pack(pady=15)

root.mainloop()
