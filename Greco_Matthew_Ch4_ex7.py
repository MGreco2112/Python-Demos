#Write a set of nested loops that display 10 rows of # characters. There should be 15 # characters in each row.

#define outer for loop to range 10
for i in range(10):
    #initialize string var output
    output = ""

    #define inner loop for range 15
    for j in range(15):

        #concatonate '#' to output var
        output += '#'
    
    #print output string
    print(output)