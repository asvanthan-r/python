class Student:
    def __init__(self, rollnum = None, name = None):
        self.rollnum = rollnum
        self.name = name
    def display_info(self):
        print(f"Rollnum: {self.rollnum}\n Name: {self.name}")

student1  = Student()
student2 = Student(22, 'we')

student1.display_info()
student2.display_info()