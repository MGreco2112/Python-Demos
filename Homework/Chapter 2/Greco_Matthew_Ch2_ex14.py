#Compound Interest

#ask user for input of principle in account, store as principle
principle = float(input("Enter the account principle: "))
#ask user for annual interest rate, store as interestRate
interestRate = float(input("Enter the annual interest rate for the account: "))
#ask user for times per year interest will accrew on the account, store as timesPerYear
timesPerYear = int(input("Enter the number of times per year interest will accrew on the account: "))
#ask user for number of years the account will accrew interest, store as years
years = int(input("Enter the number of years the account will accrew interest: "))
#divide interestRate by 100 to account for percentage, divide that by timesPerYear, add one. Store in modifiedRate
modifiedRate = (interestRate / 100) / timesPerYear + 1
#multiply timesPerYear by years. Store in exponent
exponent = timesPerYear * years
#raise modifiedRate to the power of exponent. Store in exponentRate
exponentRate = modifiedRate ** exponent
#multiply principle by exponentRate. Store in amount
amount = principle * exponentRate
#print formatted amount
print(f"${amount:,.2f}")
