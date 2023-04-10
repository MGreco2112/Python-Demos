#Property Tax Evaluation
#Tax is 60% of property's actual value
#write a program that takes in actual value of property and responds with the taxed amount

#define main function
def main():
    #ask for user input of dollar value on their property, cast as float, and assign to prop_value var
    prop_value = float(input("Enter the dollar value of your property value: $"))

    #call the property assessment function, passing property value as an argument. Control is passed to prop_assignment
    #the return value is assigned to assessed value var
    assessed_value = prop_assessment(prop_value)

    #print the assessed value of the property, formatted to two decimal places with comma insertion
    print(f"Your property has been assessed at ${assessed_value:,.2f}.")

    #call the prop_tax_evaluation function, passing the assessed value var as an argument. Control is passed to prop_tax_evaluation function
    #the return value is stored in the tax_amount var
    tax_amount = prop_tax_evaluation(assessed_value)

    #print the original input value of the property and the taxed rate of the evaluated value of the property, formatted to two decimal places
    #with comma insertion
    print(f"The property value of ${prop_value:,.2f} has an evaluated tax rate of ${tax_amount:,.2f}.")

#define prop_assessment function with value as a parameter
def prop_assessment(value):
    #initialize the assessment rate constant to decimal formatted 60%
    ASSESSMENT_RATE = 0.60
    #multiply parameter value of passed property value by the assessment rate, store in assessment value var
    assessment_value = value * ASSESSMENT_RATE

    #return assessment value from function, control is passed back to main function
    return assessment_value

#define prop_tax_evaluation function with assessed_value as a parameter
def prop_tax_evaluation(assessed_value):
    #initialize the property tax rate constant to 0.0072 to reflect the percentage of .72 for every $100 of assessed property value
    PROPERTY_TAX_RATE = 0.0072

    #multiply the parameter value passed into function (assessed property value) by the property tax rate
    #store in taxed assessment value var
    taxed_assessment_value = assessed_value * PROPERTY_TAX_RATE

    #return taxed assessment value from function, control is passed back to main function
    return taxed_assessment_value

#call main function, control is passed to main until the last line of main executes
#this returns control to this point. As there are no other function calls or lines of code present, the program terminates
main()