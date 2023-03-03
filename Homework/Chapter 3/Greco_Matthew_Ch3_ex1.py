#Day Of The Week Input

#Ask the user for a number between 1 and 7
#print the day of the week that corrosponds with that number
#print an error message if input is beyond that range

#ask for user input
day_of_week = int(input("Enter a number between 1 and 7: "))

#determine if day_of_week value is within defined constraints
if day_of_week >= 1 and day_of_week <= 7:
    #determine exact value of day_of_week and print corrosponding day
    if day_of_week == 1:
        print("Sunday")
    elif day_of_week == 2:
        print("Monday")
    elif day_of_week == 3:
        print("Tuesday")
    elif day_of_week == 4:
        print("Wednesday")
    elif day_of_week == 5:
        print("Thursday")
    elif day_of_week == 6:
        print("Friday")
    elif day_of_week == 7:
        print("Saturday")
#print error message if value outside constraints
else:
    print(f"Input ({day_of_week}) is outside of the defined constraints.")