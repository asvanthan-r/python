class  Employee:
    empId: int 
    name: str 
    email: str 

class FullEmp(Employee):
    salary: str 

class PartEmp(Employee):
    hours: int 

fte = FullEmp()
pte = PartEmp()

fte.name = "asvanth"
fte.empId = 4444
fte.email = "sdds@"
fte.salary = 5300562

pte.name = "Jj"
pte.empId = 2323
pte.email = "233232@"
pte.hours = 53

print(f"Name: {fte.name}, ID: {fte.empId}, Email: {fte.email}, Salary: {fte.salary}")
print(f"Name: {pte.name}, ID: {pte.empId}, Email: {pte.email}, Hours: {pte.hours}")