#create if else logic (initial version no elif) that takes float value and prints letter grade

#grading scale:
    #90+ = A
    #80+ = B
    #70+ = C
    #60+ = D
    #< 60 = F

#declair constants
A_START_RANGE = 90
B_START_RANGE = 80
C_START_RANGE = 70
D_START_RANGE = 60

#take user input, parse as float
grade = float(input("Enter your current grade: "))

if grade >= D_START_RANGE: #if grade is greater than F range, enter evaluation block for specific grade
    if grade >= A_START_RANGE: #if grade within A Range
        print("A")
    else:
        if grade >= B_START_RANGE:
            print("B")
        else:
            if grade >= C_START_RANGE:
                print("C")
            else:
                if grade >= D_START_RANGE:
                    print("D")
else: #otherwise print F grade
    print("F")


#refactor using elif

# grade = float(input("Enter your current grade: "))

# if grade >= A_START_RANGE:
#     print("A")
# elif grade >= B_START_RANGE:
#     print("B")
# elif grade >= C_START_RANGE:
#     print("C")
# elif grade >= D_START_RANGE:
#     print("D")
# else:
#     print("F")