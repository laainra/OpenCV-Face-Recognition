import cv2
import tkinter as tk
from tkinter import filedialog

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create a function to open a file dialog and select an image file
def select_image():
    # Open a file dialog and get the path of the selected file
    path = filedialog.askopenfilename(initialdir='/', title='Select an image', filetypes=[('Image files', '*.jpg *.jpeg *.png *.bmp')])
    
    # Read the selected image
    img = cv2.imread(path)
    # Resize the image to 1280x720
    img = cv2.resize(img, (1280, 720))
    
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()

# Create a Tkinter window
root = tk.Tk()
# Set the width and height of the window
window_width = 960
window_height = 480

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates of the top-left corner of the window
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

# Set the position of the window to the center of the screen
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

root.config(bg="#9272ad")

# Add label with text "Welcome to Python Recognition" above the button
label_top = tk.Label(root, text="Welcome to Python Recognition", font=("Poppins", 50), fg="purple")
label_top.pack()

# Create a button to select an image

frame = tk.Frame(root)

# add button to the frame
button = tk.Button(root, text='Select Image', command=select_image, width="20", height="3" ,bg="#d099ff", fg="purple")

# set position of button in the frame
button.pack(side='top', padx=50, pady=100)

# Add label with text "by LALA" below the button
label_bottom = tk.Label(root, text="by LALA", fg="purple", font=("Poppins", 30))
label_bottom.pack(side=tk.BOTTOM)

# Run the Tkinter event loop
root.mainloop()
