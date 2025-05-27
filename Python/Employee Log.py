class Person:
    def __init__(self,name,age):
        self.name = name
        if age < 0:
            raise ValueError("Invalid Age")
        else:
            self.age = age

    def __str__(self):
        return (f"To onoma einai {self.name} kai i ilikia {self.age}")
    

class Department:
    def __init__(self,name_depart):
        self.name_depart = name_depart
        self.employee_list = []

    def add_employees(self,employee_1):
        if isinstance(employee_1 , Employee):
            self.employee_list.append(employee_1)

    def __len__(self):
        return len(self.employee_list)
    
class Employee(Person):
    def __init__(self,name,age,employee_id,name_depart):
        Person.__init__(self,name,age)
        Department.__init__(self,name_depart)
        self.employee_id = employee_id
        self.salary = 0
        self.leaves = 25
        self.used_leaves = 0
        self.position = "Junior"

    def Promote(self,new_position):
        old_position = self.position
        self.position = new_position
        return(f"The employee with name {self.name} has been promoted from {old_position} to {new_position}")
    
    def add_leaves(self,days):
        if self.used_leaves + days > self.leaves:
            print(f"you have only {self.leaves} days left")
        else:
            self.used_leaves += days
            print(f"{self.name} pire {days} meres kai apomenoun {self.leaves - self.used_leaves}")
    
    def calc_remaindays(self):
        calc = self.leaves - self.used_leaves
        return(f"{self.name} exei {calc} days from {self.leaves}")
    
    def get_employee_info(self):
        return(f"name = {self.name} age = {self.age} employee id {self.employee_id} department {self.name_depart}")
    
    def work(self):
        print(f"{self.name} employee works on {self.name_depart}")

class Manager(Employee):
    def __init__(self,name,age,employee_id,name_depart):
        super().__init__(name,age,employee_id,name_depart)


    def get_index(self):
        indetification = super().get_employee_info()
        indetification["role"] = "Manager"

    def __eq__(self,other):
        return self.name_depart == other.name_depart and self.salary == other.salary
    
    def __lt__(self,other):
        return self.name_depart < other.name_depart and self.salary < other.salary




