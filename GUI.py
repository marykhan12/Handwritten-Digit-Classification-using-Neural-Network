from tkinter import *
import numpy as np
from PIL import ImageGrab
import tensorflow as tf

# Load the trained TensorFlow model
model = tf.keras.models.load_model('mnist_digit_model.h5')

window = Tk()
window.title("Handwritten Digit Recognition")
l1 = Label()

def MyProject():
    global l1

    widget = cv
    # Setting co-ordinates of canvas
    x = window.winfo_rootx() + widget.winfo_x()
    y = window.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()

    # Image is captured from canvas and is resized to (28 X 28) px
    img = ImageGrab.grab().crop((x, y, x1, y1)).resize((28, 28))

    # Converting rgb to grayscale image
    img = img.convert('L')

    # Convert the image to a numpy array and reshape it
    img_array = np.array(img)

    # Reshape to (1, 784) to match the input expected by the model
    img_array = img_array.reshape(1, 784)

    # Normalize pixel values to [0, 1]
    img_array = img_array / 255.0

    # Calling the model for prediction
    pred = model.predict(img_array)

    # Displaying the result
    l1 = Label(window, text="Digit = " + str(np.argmax(pred)), font=('Algerian', 20))
    l1.place(x=230, y=420)

lastx, lasty = None, None

# Clears the canvas
def clear_widget():
    global cv, l1
    cv.delete("all")
    l1.destroy()

# Activate canvas
def event_activation(event):
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y

# Draw on canvas
def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width=30, fill='white', capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y

# Label
L1 = Label(window, text="Handwritten Digit Recognition", font=('Algerian', 25), fg="blue")
L1.place(x=35, y=10)

# Button to clear the canvas
b1 = Button(window, text="1. Clear Canvas", font=('Algerian', 15), bg="orange", fg="black", command=clear_widget)
b1.place(x=120, y=370)

# Button to predict the digit drawn on the canvas
b2 = Button(window, text="2. Prediction", font=('Algerian', 15), bg="white", fg="red", command=MyProject)
b2.place(x=320, y=370)

# Setting properties of the canvas
cv = Canvas(window, width=350, height=290, bg='black')
cv.place(x=120, y=70)

cv.bind('<Button-1>', event_activation)
window.geometry("600x500")
window.mainloop()
