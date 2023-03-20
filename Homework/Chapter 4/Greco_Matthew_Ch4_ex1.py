#running total for bugs collected over five days

#initialize total variable outside loop
bug_total = 0

#define for loop using range to 5
for days in range(5):
    #take user input parsed as int, store in daily total
    daily_total = int(input("Enter number of bugs collected today: "))
    #increment bug_total by user input value in daily_total
    bug_total += daily_total

#print bug_total
print(f"Number of bugs collected over five days: {bug_total}")