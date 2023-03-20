#have user provide int input
#multiply number by 10, assign to var called product
#while product < 100, iterate loop

#initialize product variable to 0
product = 0

#define while loop checking value of product, iterate while product is less than 100
while product < 100:
    product = int(input("Enter a number: ")) #take int input and assign value to product

    product = product * 10 #multiply product's current value by 10

    print(product) #print value of product for clarity

    #return to while definition to check that product is less than 100
