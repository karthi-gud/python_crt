# write a python program to create an employee class and deceare the states  and create 5 objects using different constructors 
class employee:
    def __init__(self,employeename,empid,job,salary,location,dept):
        self.employeename=employeename
        self.empid=empid
        self.job=job
        self.salary=salary
        self.location=location
        self.dept=dept
        print("hey im a 6 parameter constructor")
    def __init__(self,employeename,empid,job,salary,location,dept):
        self.employeename=employeename
        self.empid=empid
        self.job=job
        self.salary=salary
        self.location=location
        self.dept=dept
        print("hey im a 5 parameter constructor")
    def __init__(self,employeename,empid,job,salary,location):
        self.employeename=employeename
        self.empid=empid
        self.job=job
        self.salary=salary
        self.location=location
        print("hey im a 4 parameter constructor")   
    def __init__(self,employeename,empid,job,salary):
        self.employeename=employeename
        self.empid=empid
        self.job=job
        self.salary=salary
        print("hey im a 3 parameter constructor")
    def __init__(self,employeename,empid,job):
        self.employeename=employeename
        self.empid=empid
        self.job=job
        print("hey im a 2 parameter constructor")
    def __init__(self,employeename):
        self.employeename=employeename
        print("hey im a 1 parameter constructor")
    def display(self):
        print("heyim no parameter employee constructor")
e1 = employee("John Doe", 101, "Software Engineer", 60000, "New York", "IT")
e2 = employee("Jane Smith", 102, "Data Analyst", 55000, "San Francisco", "Data Science")
e3 = employee("Alice Johnson", 103, "Project Manager", 70000, "Los Angeles", "Management")
e4 = employee("Bob Brown", 104, "UX Designer", 50000, "Chicago", "Design")
e5 = employee("Charlie White", 105, "DevOps Engineer", 65000, "Seattle", "Operations")  
e1.display()
e2.display()
e3.display()
e4.display()
e5.display()


#######    THE CORRECTED VERSION OF THE CODE  ########3
class Employee:
    def __init__(self, employeename, empid=None, job=None, salary=None, location=None, dept=None):
        self.employeename = employeename
        self.empid = empid
        self.job = job
        self.salary = salary
        self.location = location
        self.dept = dept
        print(f"Employee created: {self.employeename}, {self.empid}, {self.job}, {self.salary}, {self.location}, {self.dept}")

    def display(self):
        print(f"Name: {self.employeename}, ID: {self.empid}, Job: {self.job}, Salary: {self.salary}, Location: {self.location}, Dept: {self.dept}")

# Creating objects with different "constructors"
e1 = Employee("John Doe", 101, "Software Engineer", 60000, "New York", "IT")
e2 = Employee("Jane Smith", 102, "Data Analyst", 55000, "San Francisco")
e3 = Employee("Alice Johnson", 103, "Project Manager", 70000)
e4 = Employee("Bob Brown", 104, "UX Designer")
e5 = Employee("Charlie White")

e1.display()
e2.display()
e3.display()
e4.display()
e5.display()