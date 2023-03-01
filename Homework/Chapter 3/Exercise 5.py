#create a weight conversion from kilos to newtons
#the newtonic weight formula is kilos * 9.8 = weight
#if object weighs more than 500 newtons, print object is too heavy
#if object weighs less than 100 newtos, print object is too light

#declare constant
NEWTON_CONVERSION_MULTIPLE = 9.8

#take user input
kilos = float(input("Enter the item's weight in kilos: "))

#apply newton conversion multiple to input value to determine weight in newtons
newtons = kilos * NEWTON_CONVERSION_MULTIPLE

#comparison
if newtons > 500: #if newtons greater than 500
    print("Item is too heavy") #output item is too heavy
elif newtons < 100: #if newtons less than 100
    print("Item is too light") #output that item is too light
else: #otherwise
    print(f"Your object weighs {newtons} in Newtons") #print weight in newtons