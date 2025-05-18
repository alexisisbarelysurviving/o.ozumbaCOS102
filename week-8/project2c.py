import tkinter as tk
from tkinter import messagebox


class Location:
    location_names = ["PAU", "Epe"]

    def __init__(self, location, weight):
        self.location = location
        self.weight = weight
        self.location_verification = False
        self.delivery_fee = 0

    def check_location(self):
        if self.location in Location.location_names:
            self.location_verification = True
        else:
            self.location_verification = False

    def check_weight_and_calculate_fee(self):
        if not self.location_verification:
            return "Invalid location. Try again."

        if self.location == "PAU":
            self.delivery_fee = 2000 if self.weight >= 10 else 1500
        elif self.location == "Epe":
            self.delivery_fee = 5000 if self.weight >= 10 else 4000

        return self.delivery_fee


def show_delivery_fee(fee):
    window = tk.Toplevel(root)
    window.title("Delivery Fee")
    window.geometry("300x100")
    label = tk.Label(window, text=f"Your Delivery Fee is ₦{fee}")
    label.pack(pady=20)


def go():
    location = location_entry.get().strip()
    try:
        weight = float(weight_entry.get().strip())
    except ValueError:
        messagebox.showerror("Error")
        return

    delivery = Location(location, weight)
    delivery.check_location()
    result = delivery.check_weight_and_calculate_fee()

    show_delivery_fee(result)


# GUI Setup
root = tk.Tk()
root.title("Delivery System")
root.geometry("400x200")

# Weight input
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Location input
location_label = tk.Label(root, text="Location (Epe or PAU):")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Go", command=go)
submit_button.pack(pady=10)

# Run the app
root.mainloop()
