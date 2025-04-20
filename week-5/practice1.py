import tkinter as tk

def button_click():
    msgbox.showinfo("info", "welcome to cos 102 gui app!\n")
    result = msgbox.askyesno("confirmation", "do you want to continue?")

root = tk.Tk()
root.title("home page")
root.geometry("300x100")

label = tk.Label(root, text="hello friend\n")
label.pack()

button = tk.Button(root,text="Click me!", command=button_click)
button.pack()

button.config(fg="red", bg="yellow")
root.mainloop()