import tkinter as tk
from app import MiniJiraApp
from db import init_db

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = MiniJiraApp(root)
    root.mainloop()