#while loop, iterates 10 times
#asks user for input of a number
#adds number to prior numbers stored in variable outside loop
#prints value in total var once loop finishes iterating

#initialize iterations variable to 10
iterations = 10

#initialize running total var to 0
user_total = 0

#define loop to check iterations > 0
while iterations > 0:
    #take int input, add to user_total
    user_total = user_total + int(input("Enter a number to add: "))

    #decrement iterations variable
    iterations = iterations - 1

#print value held in user_total
print(f"Your total is: {user_total}")