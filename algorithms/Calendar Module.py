# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar #import calendar module

date = input() #take input line of month day year format

month = int(date[0:2]) #parse inputs as ints through substrings
day = int(date[3:5])
year = int(date[6:])

weekday_num = calendar.weekday(year, month, day) #generate weekday number through calendar.weekday

#test state of weekday_num and print capitalized day name based on value
if weekday_num == 6:
    print("SUNDAY")
elif weekday_num == 0:
    print("MONDAY")
elif weekday_num == 1:
    print("TUESDAY")
elif weekday_num == 2:
    print("WEDNESDAY")
elif weekday_num == 3:
    print("THURSDAY")
elif weekday_num == 4:
    print("FRIDAY")
else:
    print("SATURDAY")