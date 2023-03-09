# read in person's name, five grades, compute average. Only use structures gone over in class up to date

student_name = input("Enter your name: ")

NUMBER_OF_GRADES = 5

first_grade = float(input("Enter the first grade you recieved: "))

second_grade = float(input("Enter the second grade you recieved: "))

third_grade = float(input("Enter the third grade you recieved: "))

fourth_grade = float(input("Enter the fourth grade you recieved: "))

fifth_grade = float(input("Enter the fifth grade you recieved: "))

average_grade = (first_grade + second_grade + third_grade + fourth_grade + fifth_grade) / NUMBER_OF_GRADES

print(f"{student_name}'s average grade is {average_grade}.")