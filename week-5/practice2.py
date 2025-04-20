import tkinter as tk 
from tkinter import messagebox
from PIL import  Image, ImageTk

def welcomemessage(username):
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is python gui with tkinter")
    label_2.pack()

    root.mainloop()

def submit():
    username = username_entry.get()
    password =password_entry.get()

    if username == "mary" and password == "cos102":
        welcomemessage(username)
    else:
        messagebox.showerror("login", "invalid username or password")
# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the main event loop
root.mainloop()


