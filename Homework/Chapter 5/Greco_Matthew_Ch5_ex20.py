#Create a random number guessing game that asks the player to guess a random number between 1 and 100
#If number guessed is not equal to number generated, program should respond in what direction (high or low) player's guess was and to guess again
#If number guessed is equal, program should congradulate player and generate another number to guess

#OPTIONAL: add a guess counter that tracks the number of guesses the player makes. When a correct guess is made, display guess count

import random #import random module for generating random numbers

RANDOM_FLOOR = 1 #initalize random floor constant to 1, the smallest inclusive value for randint
RANDOM_CEILING = 100 #initialize the random ceiling constant to 100, the largest inclusive value for randint
player_guess_count = 1 #initialize global variable player_guess_count to 1 (this serves as the initial guess value the player will make)


def main(): #define main function

    random_number = generate_number() #initialize random number var with the return value of the generate_number function

    print("Random Number Guessing Game!") #print a welcome message to the player

    player_guessed_number = take_guess() #initialize the player guessed number var with the return value of the take guess function

    check_answer(random_number, player_guessed_number) #call the check answer function, passing the generated random number and the guessed number as arguments

    continue_game_check = input("Do you want to continue playing? y/n (case sensitive): ") #initialize the continue_game_check variable with the return of input
                                                                                           #asking for case sensitive y/n character values

    if continue_game_check == 'y': #if continue_game_check var holds char y
        main() #call the main function to start a new round
    else: #otherwise
        print("Thank you for playing! Goodbye!") #print goodbye message

def generate_number(): #define generate number function

    generated_number = random.randint(RANDOM_FLOOR, RANDOM_CEILING) #initialize the generated number var with the return of randint, with floor and ceiling constants passeed as args

    return generated_number #return generated number

def take_guess(): #define take guess function

    player_guessed_number = 0 #initialize player_guessed_number var to 0 for input validation check

    while player_guessed_number < RANDOM_FLOOR or player_guessed_number > RANDOM_CEILING: #define while loop condition to test if player enters beyond constraints allowed by floor and ceiling
        player_guessed_number = int(input("Enter an integer between 1 and 100 inclusive: ")) #store integer guess by player input in player guessed number var

        if player_guessed_number < RANDOM_FLOOR or player_guessed_number > RANDOM_CEILING: #if player guesesd number falls outside of allowed constraints, print error message
            print("Invalid entry, try again:")

    return player_guessed_number #return validated player guessed number var

def check_answer(generated_number, guessed_number): #define check answer function with two parameters
    global player_guess_count #grant scope access to modify player guess count global var through function
    
    while guessed_number != generated_number: #begin while loop to run while player's guess is not equal to random generated integer
        player_guess_count += 1 #if guess is not correct, player guess count global var is incremented
        
        if guessed_number > generated_number: #if guessed number is greater than random generated int
            print("Too High!") #print too high
        else: #if it's lower than generated int
            print("Too Low!") #print too low
        
        guessed_number = take_guess() #reassign value of guessed number to the return value of take guess function, prompting user to provide more input
            

    print(f"Correct! You answered {generated_number} in {player_guess_count} guesses!") #if loop is bypassed by guessed number equaling the generated one, print the number and guess count

    player_guess_count = 1 #reset global guess count to 1 for optional further rounds of the game

#call main function to begin program
main()