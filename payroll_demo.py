#basic, single employee routine

# hoursWorked = float(input("Enter hours worked: "))
# payRate = float(input("Enter hourly pay rate: "))

# grossWeekly = hoursWorked * payRate

# print("Employee's Gross Pay is: $" + str(format(grossWeekly, '.2f')))

#multiple employee payroll
#implementing Employee class
employees = []

class Employee:
    #python constructor, self indicates this class similar to 'this'. Fields come after
    def __init__(self, name, worked, pay):
        self.name = name
        self.hoursWorked = worked
        self.payRate = pay
    
    #custom method, self is used to assign value to field within class
    def setGross(self, gross):
        self.grossPay = gross

def payroll(hours, rate):
    return hours * rate

employeeCount = int(input("How many entries would you want to calculate? "))

while len(employees) < employeeCount:
    name = input("Enter Employee name: ")
    hoursWorked = float(input("Enter hours worked: "))
    payRate = float(input("Enter hourly pay rate: "))

    #creates new instance of object
    empl = Employee(name, hoursWorked, payRate)

    #calls object method
    empl.setGross(payroll(empl.hoursWorked, empl.payRate))

    employees.append(empl)

# for x in range(len(employees)):
#     print(employees[x][0] + ": $" + str(format(employees[x][1], '.2f')))

for empl in employees:
    print(empl.name + ": $" + str(format(empl.grossPay, '.2f')))
