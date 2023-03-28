if __name__ == '__main__':
    x = int(input()) #take inputs from system for three coordinates and one test number
    y = int(input())
    z = int(input())
    n = int(input())
    
    output = [] #initialize output array
    
    for outer in range(x + 1):
        for middle in range(y + 1):
            for inner in range(z + 1): #define triple nested loop for each permutation of coordinates
                if outer + middle + inner != n: #test sum of coordinates so that they are not equal to test number
                    output.append([outer, middle, inner]) #append subarray to output array
    
    print(output) #print output array
