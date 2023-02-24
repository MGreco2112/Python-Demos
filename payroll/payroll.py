from employee import Employee

def payroll(hours, rate):

    if hours > 40:
        output = 0.0

        overtime_hours = hours % 40
        regular_hours = hours - overtime_hours

        output = regular_hours * rate
        output += overtime_hours * (rate * 1.5)

        return output

    else:
        return hours * rate


employees = []

employeeCount = int(input("How many entries would you want to calculate? "))

while len(employees) < employeeCount:
    name = input("Enter Employee name: ")
    hoursWorked = float(input("Enter hours worked: "))
    payRate = float(input("Enter hourly pay rate: "))

    #creates new instance of object
    empl = Employee(name, hoursWorked, payRate)

    #calculates hours worked times hourly rate, stores in gross
    gross = payroll(empl.hoursWorked, empl.payRate)

    #calls object method
    empl.setGross(gross)

    employees.append(empl)

for empl in employees:
    print(f"{empl.name}: ${empl.grossPay:,.2f}")
