#Create program that allows User to input a number 0 - 36
#output the color of the pocket on the roulette wheel
#0 is green, 1 - 10 odd pockets are red, even black
#11 - 18 odd are black, even are red
#19 - 28 odd are red, even are black
#29 - 36 odd are black, even are red
#output error message if input is outside of range 0 - 36

#get user input, store in roulette choice
roulette_choice = int(input("Enter your Roulette Wheel choice (0-36): "))

#determine if roulette_choice variable is greater than or equal to 0 and roulette_choice is less than or equal to 36
if roulette_choice >= 0 and roulette_choice <= 36: #if true, enter code block for number determination

    choice_is_even = roulette_choice % 2 == 0 #create bool flag checking if roulette_choice is even or odd    
    
    if roulette_choice == 0: #roulette_choice is equal to 0 case
        print("green") #print green
    
    elif roulette_choice >= 1 and roulette_choice <= 10: #roulette_choice greater than or equal to 1 and less than or equal to 10
        if choice_is_even: #determine if choice_is_even flag is true (indicating that roulette_choice is an even number)
            print("black") #print black
        else:
            print("red") #print red
    
    elif roulette_choice >= 11 and roulette_choice <= 18: #if roulette_choice greater than or equal to 11 and less or equal to 18
        if choice_is_even: #if bool flag is true (even number)
            print("red") #print red
        else: #if odd number
            print("black") #print black

    elif roulette_choice >= 19 and roulette_choice <= 28: #if roulette_choice greater or equal to 19 and less or equal to 28
        if choice_is_even: #if bool flag is true (even number)
            print("black") #print black
        else: #if bool flag is false (odd number)
            print("red") #print red
    
    else: #if roulette_choice greater than 28 but less than 37 (as defined in parent If condition and filtered by prior if/elifs)
        if choice_is_even: #if bool flag is true (even number)
            print("red") #print ed
        else: #if bool flag is false (odd number)
            print("black") #print black
            
else: #if false, enter code block for error message
    print(f"Invalid Selection: {roulette_choice} is outside of range 0 - 36.") #print error message