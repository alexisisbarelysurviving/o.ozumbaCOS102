import sqlite3

def init_db():
    conn = sqlite3.connect("jira_clone.db") #connects to the database file 
    cursor = conn.cursor() #makes a cursor that runs sql commands
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """) #creates a table for projects if it doesnt already exist. id is a unique number that increases automatically, name is text that must be filled, description is optional text used to describle the project
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            title TEXT NOT NULL,
            status TEXT,
            severity TEXT,
            assignee TEXT,
            project_id INTEGER,
            FOREIGN KEY(project_id) REFERENCES projects(id)
        )
    """) #creates table for tickets if it lready doesnt exsist. title is the required ticket name, status severity and assignee are the optional text fields for tracking, and project id links the ticketv to a project. foreign key is to make sure project_id matches a real projects.id
    conn.commit() #saves all changes to database
    conn.close() #closes connection to database