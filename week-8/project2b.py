import tkinter as tk
from tkinter import messagebox


class Location():

    def __init__(self, location, weight):
        self.location = location
        self.weight = weight
        self.location_verification = False
        self.yourdeliveryfee = 0
        

    location_names = ["PAU", "Epe"]
    
    def check_location(self):
        if self.location in Location.location_names:
            print('location accessible')
            self.location_verification = True

    def check_weight(self):
        if self.location_verification == True:
            if self.weight >= 10 and self.location == "PAU":
                self.yourdeliveryfee = 2000
            if self.weight <= 10 and self.location == "PAU":
                self.yourdeliveryfee(1500)
            if self.weight >= 10 and self.location == "Epe":
                self.yourdeliveryfee(5000)
            if self.weight <= 10 and self.location == "Epe":
                self.yourdeliveryfee(4000)
            else:
                print ("invalid", "try again")
          
          
def yourdeliveryfee(fee):
    window = tk.Toplevel(root)
    window.title("Delivery Fee")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Your Delivery Fee is {fee}\n")
    label_1.pack()

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

            

