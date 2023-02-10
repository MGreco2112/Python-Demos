price = float(input("Enter the price "))
discount = float(input("Enter the discount percentage "))
PERCENT = 100
modDiscount = discount/PERCENT
subtractedAmount = modDiscount * price
finalPrice = price - subtractedAmount

print(finalPrice)