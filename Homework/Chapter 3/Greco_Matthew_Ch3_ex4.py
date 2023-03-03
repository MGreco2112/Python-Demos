roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VII", "IX", "X"] #initialize variable with array of Strings for Roman Numerals between 1 and 10 at indexes 0 - 9

selected_number = int(input("Enter a number between 1 and 10: ")) #take user input for a number between 10 and 10

if selected_number >= 1 and selected_number <= 10: #check if selected_number is greater or equal to one and less or equal to 10
    print(roman_numerals[selected_number - 1]) #if true print value at index selected_number - 1 (to account for zero based indexing) in array
else: #otherwise print error message
    print("Invalid selection, please try again.")