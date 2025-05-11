class Location():

    def __init__(self, location):
        self.location = location
        self.location_verification = False

    location_names = ["PAU", "Epe"]
    
    def check_location(self):
        if self.location in Location.location_names:
            print('location accessible')
            self.location_verification = True
            
so = Location(input('What is your location: '))
 
so.check_location()

import tkinter as tk 
from tkinter import messagebox

def yourdeliveryfee(fee):
    window = tk.Toplevel(root)
    window.title("Delivery Fee")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Your Delivery Fee is {fee}\n")
    label_1.pack()


def go():
    weight = weight_entry.get()
    location = location_entry.get()

    if weight >= 10 and location == "PAU":
        yourdeliveryfee(2000)
    if weight <= 10 and location == "PAU":
        yourdeliveryfee(1500)
    if weight >= 10 and location == "Epe":
        yourdeliveryfee(5000)
    if weight <= 10 and location == "Epe":
        yourdeliveryfee(4000)
    else:
        messagebox.showerror("invalid", "try again")

# Create main window
root = tk.Tk()
root.title("Delivery System")
root.geometry("500x200")

# Create username label and entry
username_label = tk.Label(root, text="Weight:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(root, text="Location (Epe or PAU):")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Go", command=go)
submit_button.pack()

# Run the main event loop
root.mainloop()



