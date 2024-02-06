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


# Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)



# Create entry box to add to the list
my_entry = Entry(
    root,
    font=("Helvetica", 24),
    width=30,
    bg="#e0e0e0",
    fg="black"
)
my_entry.pack(pady=10)

# Create a button frame
button_frame = Frame(root, bg="darkblue")
button_frame.pack(pady=10)

def delete_item():
    selected_indices = my_list.curselection()
    if not selected_indices:
        return

    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected item(s)?")
    if confirmation:
        for index in reversed(selected_indices):
            my_list.delete(index)

def add_item():
    task = my_entry.get()
    if task:
        my_list.insert(END, task)
        my_entry.delete(0, END)

def cross_off_item():
    selected_indices = my_list.curselection()
    for index in selected_indices:
        my_list.itemconfig(index, fg="#888888")
    my_list.selection_clear(0, END)

def uncross_item():
    selected_indices = my_list.curselection()
    for index in selected_indices:
        my_list.itemconfig(index, fg="#464646")
    my_list.selection_clear(0, END)

def delete_crossed():
    crossed_indices = [i for i in range(my_list.size()) if my_list.itemcget(i, "fg") == "#888888"]
    for index in reversed(crossed_indices):
        my_list.delete(index)

def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/gui/data",
        title="Save File",
        filetypes=(("Dat Files", ".dat"), ("All Files", ".*"))
    )
    if file_name:
        if not file_name.endswith(".dat"):
            file_name = f'{file_name}.dat'

        # Delete crossed off items before saving
        crossed_indices = [i for i in range(my_list.size()) if my_list.itemcget(i, "fg") == "#888888"]
        for index in reversed(crossed_indices):
            my_list.delete(index)

        # Grab all the items from the list
        items = [{"text": my_list.get(i), "crossed": my_list.itemcget(i, "fg") == "#888888"} for i in range(my_list.size())]

        # Open the file using a context manager
        with open(file_name, 'wb') as output_file:
            # Actually add the items to the file
            pickle.dump(items, output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/gui/data",
        title="Open File",
        filetypes=(("Dat Files", ".dat"), ("All Files", ".*"))
    )
    if file_name:
        # delete currently open list
        my_list.delete(0, END)

        # open the file
        try:
            with open(file_name, 'rb') as input_file:
                # load the data from the file
                items = pickle.load(input_file)

                # output stuff to the screen
                for item in items:
                    text = item["text"]
                    crossed = item["crossed"]

                    my_list.insert(END, text)
                    if crossed:
                        my_list.itemconfig(END - 1, fg="#888888")

        except pickle.UnpicklingError:
            messagebox.showerror("Error", "Invalid file format")

def delete_list():
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the entire list?")
    if confirmation:
        my_list.delete(0, END)

# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# add dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_list)

# add some buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete crossed", command=delete_crossed)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

# Main Loop
root.mainloop()
