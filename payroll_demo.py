#basic, single employee routine

hoursWorked = float(input("Enter hours worked: "))
payRate = float(input("Enter hourly pay rate: "))

grossWeekly = hoursWorked * payRate

print("Employee's Gross Pay is: $" + str(format(grossWeekly, '.2f')))