import tkinter as tk 
from tkinter import messagebox

def yourdeliveryfee(fee):
    window = tk.Toplevel(root)
    window.title("Delivery Fee")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Your Delivery Fee is {fee}\n")
    label_1.pack()


def go():
    weight = int(weight_entry.get())
    location = location_entry.get()

    if weight >= 10 and location == "PAU":
        yourdeliveryfee(2000)
    elif weight <= 10 and location == "PAU":
        yourdeliveryfee(1500)
    elif weight >= 10 and location == "Epe":
        yourdeliveryfee(5000)
    elif weight <= 10 and location == "Epe":
        yourdeliveryfee(4000)
    else:
        messagebox.showerror("invalid", "try again")

# Create main window
root = tk.Tk()
root.title("Delivery System")
root.geometry("500x200")

# Create username label and entry
weight_label = tk.Label(root, text="Weight:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Create password label and entry
location_label = tk.Label(root, text="Location (Epe or PAU):")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Go", command=go)
submit_button.pack()

# Run the main event loop
root.mainloop()


