#calculate employee salary if they are paid pennies each day doubling
#format output as dollars, not as pennies
#ask user for number of days, then iterate output

#take user input for number of days to calculate
count_of_days = int(input("How many days do you wish to calculate pay for: "))

#print table header
print(f"| Day  |  Daily Pay |")

#define loop ranging from 1 while counter < count_of_days
for day in range(1, count_of_days + 1):
    #calculate daily pay in pennies, raising day to the power of day (penny count doubles each day)
    daily_pay = day ** day
    #format pay in percent of a dollar (divide by 100)
    daily_dollars = daily_pay / 100

    #print formatted day and daily_dollars values into table
    print(f"| {day:<4d} | {daily_dollars:>10,.2f} |")