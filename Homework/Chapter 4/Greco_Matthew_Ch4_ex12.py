#calculate factorial of a number provided by user
#number must be positive
#calculate factorial and print final output

#initialize base number to a value of -1
base_number = -1

#initialize output variable to 1
output = 1

#validate input via while loop, iterate loop if base_number is less or equal to 0 (invalid inputs)
while base_number <= 0:
    #prompt user for valid positive number
    base_number = int(input("Enter a positive number to calculate the factorial of: "))

    #check given input and provide warning if loop must iterate again
    if base_number < 1:
        print("Invalid Input: Try Again")

#define loop for range 1 to < base_number + 1
for fact in range(1, base_number + 1):
    #multiply current loop iteration by value stored in output variable
    output *= fact

#output final factorial, comma formatted for clarity
print(f"Factorial Output is {output:,}.")