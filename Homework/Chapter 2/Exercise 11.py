#ask user for input male student count
maleCount = int(input("How many males are registered for class? "))
#ask user for input female student count
femaleCount = int(input("How many females are registered for class? "))
#calculate total in class
classTotal = maleCount + femaleCount
#divide male count by total in class
malePercentage = maleCount / classTotal
#divide female count by total in class
femalePercentage = femaleCount / classTotal
#multiply each by 100 to get int percentage
maleIntPercentage = malePercentage * 100
femaleIntPercentage = femalePercentage * 100
#print male and female percentages
print(f"Male percentage in class is {maleIntPercentage}%\nFemale percentage in class is {femaleIntPercentage}%")