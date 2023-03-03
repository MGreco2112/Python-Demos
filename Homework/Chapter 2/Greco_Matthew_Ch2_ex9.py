celcius = 0 #input for celcius at 0
    
farenheit = (9/5) * celcius + 32 #divide 9/5, multiply by celcius, add 32

print(farenheit) #print farenheit
   
#function solution
def celciusToFar(cel): #define function celciusToFar with cel as parementer
    return (9/5) * cel + 32 #return a value of 9/5 times the argument value for cel, then add 32

print(celciusToFar(0)) #prints the function call of the celciusToFar function with 0 passed as an argument