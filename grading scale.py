#create if else logic (initial version no elif) that takes float value and prints letter grade

#grading scale:
    #90+ = A
    #80+ = B
    #70+ = C
    #60+ = D
    #< 60 = F

#declare constants
A_START_RANGE = 90
B_START_RANGE = 80
C_START_RANGE = 70
D_START_RANGE = 60

#take user input, parse as float
grade = float(input("Enter your current grade: "))

if grade >= D_START_RANGE: #if grade is greater than F range, enter evaluation block for specific grade
    if grade >= A_START_RANGE: #if grade within A Range
        print("A") #print grade
    else: #else, if not within A Range
        if grade >= B_START_RANGE: #if grade within B Range
            print("B") #print grade
        else: #else, if not within B Range
            if grade >= C_START_RANGE: #if grade within C Range
                print("C") #print grade
            else: #else if not within C Range
                    print("D") #print D grage
else: #otherwise print F grade
    print("F")


#refactor using elif

# #take input from user, parse as float
# grade = float(input("Enter your current grade: "))

# #if grade within A Range
# if grade >= A_START_RANGE:
#     print("A") #print grade
# elif grade >= B_START_RANGE: #else if grade within B Range
#     print("B") #print grade
# elif grade >= C_START_RANGE: #else if grade within C Range
#     print("C") #print grade
# elif grade >= D_START_RANGE: #else if grade within D Range
#     print("D") #print grade
# else: #else
#     print("F") #print grade