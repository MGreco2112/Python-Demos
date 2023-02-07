#basic, single employee routine

# hoursWorked = float(input("Enter hours worked: "))
# payRate = float(input("Enter hourly pay rate: "))

# grossWeekly = hoursWorked * payRate

# print("Employee's Gross Pay is: $" + str(format(grossWeekly, '.2f')))

#multiple employee payroll
employees = []

def payroll(hours, rate):
    return hours * rate

employeeCount = int(input("How many entries would you want to calculate? "))

while len(employees) < employeeCount:
    name = input("Enter Employee name: ")
    hoursWorked = float(input("Enter hours worked: "))
    payRate = float(input("Enter hourly pay rate: "))

    gross = payroll(hoursWorked, payRate)

    employees.append([name, gross])

for x in range(len(employees)):
    print(employees[x][0] + ": $" + str(format(employees[x][1], '.2f')))
