roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VII", "IX", "X"]

selected_number = int(input("Enter a number between 1 and 10: "))

if selected_number >= 1 and selected_number <= 10:
    print(roman_numerals[selected_number - 1])
else:
    print("Invalid selection, please try again.")