#Compound Interest

#input the principle amount into the account (float)
principle = float(input("Enter the principle amount "))
#input the interest rate for the account (float)
interestRate = float(input("Enter the interest rate on the account "))
#input the number of times interest is compounded during the year (int), 4 for quarterly or 12 for monthly
timesPerYear = int(input("How often will interest accrew on the account? "))
#input the number of years the account will be left to earn interest
years = int(input("How many years will the account accrew interest? "))
#divide interestRate by timesPerYear, plus 1, store into variable rateTimesYears
rateTimesYears = interestRate / timesPerYear + 1
#multiply rateTimesYears by the principle, into new variable rateTimesPrinciple
rateTimesPrinciple = rateTimesYears * principle
#multiply times per year times years, store into new variable modifiedYears
modifiedYears = timesPerYear * years
#raise rateTimesPrinciple to the power of modifiedYears into account variable
account = rateTimesPrinciple ** modifiedYears
#print account variable
print(f"${account:,.2f}")

#This is wrong, fix tomorrow