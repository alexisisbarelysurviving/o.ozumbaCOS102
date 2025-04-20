import tkinter as tk
from tkinter import messagebox
import csv

# Load CSV data into a list
employees = []
with open("GIG-logistics.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append(row)

# Function to check if the employee exists
def check_employee():
    name = name_entry.get().strip().lower()
    dept = dept_entry.get().strip().lower()
    found = False
    same_dept_people = []

    for emp in employees:
        if emp["Name"].strip().lower() == name and emp["Department"].strip().lower() == dept:
            found = True
        if emp["Department"].strip().lower() == dept and emp["Name"].strip().lower() != name:
            same_dept_people.append(emp["Name"])

    if found:
        message = "Welcome, " + name_entry.get() + "!\n\nOther people in " + dept_entry.get() + ":\n"
        for person in same_dept_people:
            message += "- " + person + "\n"
        messagebox.showinfo("Employee Found", message)
    else:
        messagebox.showwarning("Oops", "Employee not found!")

# GUI setup
window = tk.Tk()
window.title("Employee Checker")
window.geometry("350x250")

# Labels and entries
label1 = tk.Label(window, text="Enter your name:")
label1.pack()
name_entry = tk.Entry(window)
name_entry.pack()

label2 = tk.Label(window, text="Enter your department:")
label2.pack()
dept_entry = tk.Entry(window)
dept_entry.pack()

# Button to check
check_button = tk.Button(window, text="Check", command=check_employee)
check_button.pack(pady=20)

window.mainloop()
