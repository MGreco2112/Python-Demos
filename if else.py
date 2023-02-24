#if else control flow in class demonstration

# temperature_farenheit = float(input("Enter the temperature in Farenheit: "))


# if temperature_farenheit <= 60:
#     print("Wear a coat.")
#     print("Wear a hat.")
#     print("Wear gloves.")
# else:
#     print("Go Swimming!")

name1 = input("Enter a name: ")
name2 = input("Enter another name: ")

if name1 == name2:
    print(f"The names are both {name1}!")
else:
    if name1 > name2:
        print(f"{name2} comes before {name1}")
    else:
        print(f"{name1} comes before {name2}")