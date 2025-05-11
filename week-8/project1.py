import random as rd

class Employee():

    def __init__(self, name):
        self.name = name

    Employees_names = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", 
    "Michell Taiwo", "Abraham Jones" , "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]

    Task = ["Loading", "Transporting", "Reveiwing Orders", "Customer Service", "Delivering Items"] 

    def check_employee(self):
        if self.name in Employee.Employees_names:
            self.employee_name_verification == True
            print('You are an employee')
            
    def take_attendance(self):
        if self.employee_name_verification == True:
            self.attendance_taken == True
            print('Employee is present')

    def assign_task(self):
        if self.attendance_taken == True:
            self.assign_task_verification = True
            print(f'The task assigned to you is {rd.choice(self.Task)}')

    def refuse_access(self):
        if self.employee_name_verification == False:
            print ('You are not a verified employee, please reach HR for authorization')
        if self.attendance_taken == False:
            print ('You are not a verified employee, please reach HR for authorization')
        if self.assign_task_verification == False:
            print ('You are not a verified employee, please reach HR for authorization')


staff1 = Employee(input('What is your name: '))