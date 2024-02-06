from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox
import pickle
import datetime

root = Tk()
root.title("To-Do List")
root.geometry("600x700+400+100") 
root.resizable(True, True)

# Set background color
root.configure(bg="darkblue")

# Custom header frame
header_frame = Frame(root, 
  bg="darkblue",
  padx=10,
  pady=5
  )
header_frame.pack(fill=X)

# Title label in the header
title_label = Label(header_frame, 
text="To-Do List", 
font=("Segoe Print", 20, "bold"),
 bg="darkblue", 
 fg="white"
 )
title_label.pack()

# Define our font
my_font = Font(family="Segoe Print",
 size=16, 
 weight="bold"
 )

# Create frame
my_frame = Frame(root, bg="#e0e0e0")
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(
    my_frame,
    font=my_font,
    width=30,
    height=10, 
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none",
    bg="#e0e0e0",
    selectforeground="black"
)

my_list.pack(side=LEFT, fill=BOTH)