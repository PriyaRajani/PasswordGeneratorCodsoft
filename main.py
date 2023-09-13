from tkinter import *
from random import randint

# CONSTANTS (Change colors of your choice)
PINK = "#FFC7EA"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FBF0B2"
BLUE = "#0E21A0"
VIOLET = "#D8B4F8"

root = Tk()
root.title('Strong Password Tool')
root.geometry("500x300")
root.configure(bg=VIOLET)


def new_rand():
    # Clearing the Entry Box

    pw_entry.delete(0, END)

    # Get Pass Length as integer
    pw_length = int(my_entry.get())

    # Pass Variable
    my_password = ''

    # Loop through pass length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    # Output password to screen
    pw_entry.insert(0, my_password)


# Copy to clipboard
def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())


# Label Frame
lf = LabelFrame(root, text="How Many Characters?", bg=VIOLET, fg=BLUE)
lf.grid(row=0, column=0, pady=30, padx=30)

# Entry Boxes
my_entry = Entry(lf, font=("Helvetica", 24), bg=PINK)
my_entry.grid(row=0, column=0, pady=20, padx=20)

pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg=VIOLET)
pw_entry.grid(row=1, column=0, pady=20)

# Creating a frame for buttons
my_frame = Frame(root, bg=VIOLET)
my_frame.grid(row=2, column=0, pady=20)

my_button = Button(my_frame, text="Generate Password", command=new_rand, bg=GREEN, fg=BLUE, highlightthickness=0)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy Into Clipboard", command=clipper, bg=GREEN, fg=BLUE, highlightthickness=0)
clip_button.grid(row=0, column=2, padx=10)

root.mainloop()
