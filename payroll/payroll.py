from employee import Employee

def payroll(hours, rate):
    return hours * rate

employees = []

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

for empl in employees:
    print(empl.name + ": $" + str(format(empl.grossPay, '.2f')))
