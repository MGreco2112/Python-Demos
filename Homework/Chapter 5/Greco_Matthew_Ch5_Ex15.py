#create a program that takes five test grades and computes an average

#initialize constant to handle the number of scores to be computed to 5
NUMBER_OF_SCORES = 5

#define main function
def main():
    #call/transfer control to the take grades function. Store return value in total_grades variable
    total_grades = take_grades()

    #divide total grades variable by the number of scores constant to compute averaged grade
    #store in averaged grades var
    averaged_grades = total_grades / NUMBER_OF_SCORES

    #call/transfer control to the compute average function, passing averaged grades var as an argument
    compute_average(averaged_grades)

#define take grades function
def take_grades():
    #initialize accumulator variable total grades to 0 to accumulate input grades from user
    total_grades = 0.0

    #declare for loop using range 1 to number of scores constant + 1
    #the reason for adding 1 to number of scores is to allow the score_number iterator variable to be output in the prompt as a counter
    #for the number of scores left to calculate
    for score_number in range(1, NUMBER_OF_SCORES + 1):
        #add the score passed via input, cast as float, to the total grades variable
        #the prompt details what current score number out of total score numbers is being requested
        total_grades += float(input(f"Enter grade number {score_number} of {NUMBER_OF_SCORES} grades: "))

    #return the added total of grades. Control passes back to main function
    return total_grades

#define the compute average function, taking one parameter
def compute_average(averaged_grades):
    #define four constants for the minimum scores of A, B, C, and D grades
    #an F minimum score is not required as anything less tahn a D is considered an F
    A_MINIMUM_SCORE = 90
    B_MINIMUM_SCORE = 80
    C_MINIMUM_SCORE = 70
    D_MINIMUM_SCORE = 60

    #initialize letter grade var to an empty string
    #this var will hold which letter grade the averaged grades belong to
    letter_grade = ''

    #if averaged grades is greater or equal to A MINIMUM SCORE
    if averaged_grades >= A_MINIMUM_SCORE:
        #assign letter grade to 'A'
        letter_grade = 'A'
    #else if averaged grades is greater or equal to B MINIMUM SCORE
    elif averaged_grades >= B_MINIMUM_SCORE:
        #assign letter grade to 'B'
        letter_grade = 'B'
    #else if averaged grades is greater or equal to C MINIMUM SCORE
    elif averaged_grades >= C_MINIMUM_SCORE:
        #assign letter grade to 'C'
        letter_grade = 'C'
    #else if averaged grades is greater or equal to D MINIMUM SCORE
    elif averaged_grades >= D_MINIMUM_SCORE:
        #assign letter grade to 'D'
        letter_grade = 'D'
    #if averaged grade is less than D MINIMUM SCORE
    else:
        #assign letter grade to 'F'
        letter_grade = 'F'

    #display the averaged score of the number of grades placed into the program and the letter grade computed from the current function
    #control is passed back to main
    print(f"Your average scores of {averaged_grades:.2f} results in a {letter_grade} score.")

#call main function, program terminates after control leaves main function scope
main()