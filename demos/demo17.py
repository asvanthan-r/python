class Employee:
    __count =0
    def __init__(self):
        Employee.__count+=1
    def deisplay(self):
        print("Emp count", Employee.__count)
emp1 = Employee()
emp2 = Employee()

emp2.deisplay()

try:
    print(emp1.__count)
except AttributeError as e:
    print(e)
finally:
    emp2.deisplay()