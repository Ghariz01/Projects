class Student:
    def __init__(self,name,surname,age,st_id):
        self.grades = []
        self.name = name
        self.surname = surname
        self.age = age
        self.st_id = st_id
    def grade(self,grd):
        if grd >=0 and grd <=100:
            self.grades.append()
        elif grd <=0 and grd >=100:
            print("Please insert valid numbers")
class Graduate(Student):
    def __init__(self,name,surname,age,st_id,theses_topic,supervisor):
        super().__init__(name,surname,age,st_id)
        self.theses_topic = theses_topic
        self.supervisor = supervisor
        self.publication = []
        self.theses_compl = False
        self.progress = 0
    def upd_prog(self,value):
        self.progress = value
    def has_graduated(self):
        if self.calgr()>=80 and self.progress >=80:
            self.theses_compl = True
    def __str__(self):
        base_str = super().__str__()
        return(f"{base_str}has graduated{self.print_grad_ornot}")
    def print_grad_ornot(self):
        if self.theses_compl:
            return("Student has graduated")
        else:
            return("Student has not graduated")