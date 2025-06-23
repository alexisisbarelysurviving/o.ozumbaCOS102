import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

#creating a login window that allows users log in and putting in colour. default username is admin, default password is admin123
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - MiniJIRA")
        self.root.geometry("300x200")
        self.root.configure(bg='#2e2e2e')

        tk.Label(root, text="Username", bg='#2e2e2e', fg='white').pack(pady=(20, 5))
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)
        
        tk.Label(root, text="Password", bg='#2e2e2e', fg='white').pack(pady=5)
        self.password_entry = tk.Entry(root, show="*") #turns anything you type in here to asterix
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Login", command=self.check_login).pack(pady=15)

    def check_login(self):
        username = self.username_entry.get() #checks the input put in 
        password = self.password_entry.get()
        if username == "admin" and password == "admin123":
            self.root.destroy()
            main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.") #if its not the default we defined earlier, its scrapped


class MiniJiraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MIRA")
        self.root.configure(bg='#2e2e2e')
        self.font = ("Arial", 11)
        self.padding = {'padx': 10, 'pady': 5}
        self.create_widgets()  #this code creates the main app window by setting its title, background color, font, padding, and then the ui

    def create_widgets(self):  #this method creates and displays three tabs in the app with their colours as well
        tab_control = ttk.Notebook(self.root)
        self.project_tab = tk.Frame(tab_control, bg='#2e2e2e')
        self.ticket_tab = tk.Frame(tab_control, bg='#2e2e2e')
        self.filter_tab = tk.Frame(tab_control, bg='#2e2e2e')

        tab_control.add(self.project_tab, text='Projects')
        tab_control.add(self.ticket_tab, text='Tickets')
        tab_control.add(self.filter_tab, text='Filter')
        tab_control.pack(expand=1, fill="both") # expand and fill make the tabs grow and fill the whole window properly

        self.build_project_tab()
        self.build_ticket_tab()
        self.build_filter_tab()

    def build_project_tab(self): #this code creates all the sub components of the projects tab. like the name entry field, the description field, the create project field and the field where it displays already existsing projects 
        tk.Label(self.project_tab, text="Project Name", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.proj_name_entry = tk.Entry(self.project_tab, font=self.font)
        self.proj_name_entry.pack(**self.padding)

        tk.Label(self.project_tab, text="Description", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.proj_desc_entry = tk.Text(self.project_tab, height=4, width=40, font=self.font)
        self.proj_desc_entry.pack(**self.padding)

        tk.Button(self.project_tab, text="Create Project", command=self.add_project, font=self.font).pack(pady=10)

        tk.Label(self.project_tab, text="Existing Projects", bg='#2e2e2e', fg='white', font=self.font).pack(pady=(20, 0))
        self.project_list = tk.Text(self.project_tab, height=10, width=60, font=self.font)
        self.project_list.pack(**self.padding) #note that pad adds space around the widget so things aren't squished together and pack tells how and where to place things on the screen.
        self.refresh_project_list()

    def build_ticket_tab(self):
        tk.Label(self.ticket_tab, text="Title", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.title_entry = tk.Entry(self.ticket_tab, font=self.font)
        self.title_entry.pack(**self.padding)

        tk.Label(self.ticket_tab, text="Status", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.status_var = tk.StringVar(value="To Do")
        self.status_menu = tk.OptionMenu(self.ticket_tab, self.status_var, "To Do", "In Progress", "Done", command=self.update_status_color)
        self.status_menu.pack(**self.padding)
        self.status_menu.config(bg='red', font=self.font)

        tk.Label(self.ticket_tab, text="Severity", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.severity_var = tk.StringVar(value="Low")
        self.severity_menu = tk.OptionMenu(self.ticket_tab, self.severity_var, "Low", "Medium", "High", command=self.update_severity_color)
        self.severity_menu.pack(**self.padding)
        self.severity_menu.config(bg='green', font=self.font)

        tk.Label(self.ticket_tab, text="Assignee", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.assignee_entry = tk.Entry(self.ticket_tab, font=self.font)
        self.assignee_entry.pack(**self.padding)

        tk.Label(self.ticket_tab, text="Project ID", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.project_id_entry = tk.Entry(self.ticket_tab, font=self.font)
        self.project_id_entry.pack(**self.padding)

        tk.Button(self.ticket_tab, text="Add Ticket", command=self.add_ticket, font=self.font).pack(pady=15)

    def build_filter_tab(self):
        tk.Label(self.filter_tab, text="Filter by Project ID", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.filter_project_entry = tk.Entry(self.filter_tab, font=self.font)
        self.filter_project_entry.pack(**self.padding)

        tk.Label(self.filter_tab, text="Status", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.filter_status_var = tk.StringVar(value="")
        tk.OptionMenu(self.filter_tab, self.filter_status_var, "", "To Do", "In Progress", "Done").pack(**self.padding)

        tk.Label(self.filter_tab, text="Severity", bg='#2e2e2e', fg='white', font=self.font).pack(**self.padding)
        self.filter_severity_var = tk.StringVar(value="")
        tk.OptionMenu(self.filter_tab, self.filter_severity_var, "", "Low", "Medium", "High").pack(**self.padding)

        tk.Button(self.filter_tab, text="Search", command=self.filter_tickets, font=self.font).pack(pady=10)
        self.filter_result = tk.Text(self.filter_tab, height=10, font=self.font)
        self.filter_result.pack(**self.padding)

    def update_status_color(self, value):
        colors = {"To Do": "red", "In Progress": "yellow", "Done": "green"} #assigning colour values to the status options 
        self.status_menu.config(bg=colors.get(value, "white")) #config is used to update things after a widget is created. bg is for background colour and tells tkinyter what background colour the thing shou;d be 

    def update_severity_color(self, value):
        colors = {"Low": "green", "Medium": "yellow", "High": "red"}
        self.severity_menu.config(bg=colors.get(value, "white"))

    def add_project(self):
        name = self.proj_name_entry.get()
        desc = self.proj_desc_entry.get("1.0", tk.END).strip()
        if name:
            conn = sqlite3.connect("jira_clone.db") #connecting to database to save the information
            cursor = conn.cursor()
            cursor.execute("INSERT INTO projects (name, description) VALUES (?, ?)", (name, desc))
            conn.commit() #save new project into database
            conn.close() #then closes connection
            messagebox.showinfo("Success", "Project added!") #shows this when project has been added succsessfully 
            self.refresh_project_list()
        else:
            messagebox.showerror("Error", "Project name is required.") #displays an error if project name hasnt been specified 

    def refresh_project_list(self):
        conn = sqlite3.connect("jira_clone.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM projects") #gets all the project ids and names in the project table 
        projects = cursor.fetchall() #gets all results from the query and stores it in a list called projects 
        conn.close() #closes connection to the database

        self.project_list.delete("1.0", tk.END) #removes old project enteries
        for pid, name in projects:
            self.project_list.insert(tk.END, f"ID: {pid} | Name: {name}\n") #clears old project list, allows user to see the updated list

    def add_ticket(self):
        title = self.title_entry.get()
        status = self.status_var.get()
        severity = self.severity_var.get()
        assignee = self.assignee_entry.get()
        project_id = self.project_id_entry.get()

        if not title or not project_id:
            messagebox.showerror("Error", "Title and Project ID are required.") #displays error if project id and title are not properly stated
            return

        conn = sqlite3.connect("jira_clone.db") #connects to the database file
        cursor = conn.cursor() #makes a cursor to carry out sql commands
        cursor.execute("SELECT id FROM projects WHERE id = ?", (project_id,)) #searches for a project when an ID number is put in,the one assigned at the start
        if not cursor.fetchone():
            messagebox.showerror("Error", f"Project ID {project_id} does not exist.") #if no project is found this error is displayed
            conn.close() #closes database connection
            return

        cursor.execute("INSERT INTO tickets (title, status, severity, assignee, project_id) VALUES (?, ?, ?, ?, ?)",
                       (title, status, severity, assignee, project_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Ticket added!") #once all fields are commited, it registers the ticket into the database

    def filter_tickets(self):
        project_id = self.filter_project_entry.get()
        status = self.filter_status_var.get()
        severity = self.filter_severity_var.get() #gather information user put in

        conn = sqlite3.connect("jira_clone.db")
        cursor = conn.cursor()  #opens the database
        query = "SELECT title, status, severity, assignee FROM tickets WHERE 1=1"
        params = []  #starts checking all tickets to match the one the user put in

        if project_id:
            query += " AND project_id = ?"
            params.append(project_id)
        if status:
            query += " AND status = ?"  #looking for matching tickets
            params.append(status)
        if severity:
            query += " AND severity = ?"
            params.append(severity)

        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()

        self.filter_result.delete("1.0", tk.END) #clears all old results and shows the new based on input 
        for row in results:
            self.filter_result.insert(tk.END, f"Title: {row[0]}, Status: {row[1]}, Severity: {row[2]}, Assignee: {row[3]}\n")


#this part is to start to show the login page first. default user name is admin, default password is admin123.
#the function main_app starts the event loop and run the whole code 
def main_app():
    main_root = tk.Tk()
    app = MiniJiraApp(main_root)
    main_root.mainloop()

if __name__ == "__main__":
    login_root = tk.Tk()
    LoginWindow(login_root)
    login_root.mainloop()
