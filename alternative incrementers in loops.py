#loops with alternative incremeter values

#range object format (START, STOP, STEP)
#START: integer to begin loop at (default is 0)
#STOP: termination condition, when counter no longer less than STOP, loop terminates
#STEP: at what rate the value of count is modified after each iteration (default is 1)

for count in range(0, 10, 2):
    print(count)

print()

#decrimenting loop
#same format as before, just start is larger than stop with a negative incrementer
for count in range(10, 0, -1):
    print(count)

print()

#set string to be reversed
toReverse = "Backwards"
#generate new empty string to be built
output = ""

#print original string for reference
print(toReverse)

#begin loop, start at last index of string via len(x) - 1, run until index is -1, decrement by a value of 1
for index in range(len(toReverse) - 1, -1, -1):
    #store character of string in variable
    character = toReverse[index]

    #manipulate character casing if either last or first index of string by flipping case
    if (index == len(toReverse) - 1):
        character = character.upper()
    elif (index == 0):
        character = character.lower()

     #concatonate character to output   
    output += character

#after loop terminates, print reversed and correctly cased output string
print(output)
