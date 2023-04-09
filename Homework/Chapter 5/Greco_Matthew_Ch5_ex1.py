#Write a program that takes a distance in Kilometers and displays that distance converted to Miles

#define main function
def main():
    #ask user for kilometer input, cast as float, store into kilometers variable
    kilometers = float(input("Enter a Kilometer distance to convert to miles\n(ex: 10, 10.5): "))

    #call the kilo_to_miles function, passing kilometers var as argument. Store into miles variable
    miles = kilo_to_miles(kilometers)

    #print formatted string displaying original input value of kilometers and converted value of miles
    print(f"{kilometers} kilometers is equal to {miles} miles.")

#define kilo_to_miles with single parameter
def kilo_to_miles(kilo):
    #initialize float constant of conversion value for kilometers to be multiplied by
    CONVERSION_RATE = 0.6214
    #initialize output value to ve returned after math operation
    output = 0

    #multiply passed argument value by conversion rate constant, store into output var
    output = kilo * CONVERSION_RATE

    #return output variable
    return output

#call main function to begin program flow
main()