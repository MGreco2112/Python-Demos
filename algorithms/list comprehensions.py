if __name__ == '__main__':
    x = int(input()) #take inputs from system for three coordinates and one test number
    y = int(input())
    z = int(input())
    n = int(input())
    
    # output = [] #initialize output array
    
    # for outer in range(x + 1):
    #     for middle in range(y + 1):
    #         for inner in range(z + 1): #define triple nested loop for each permutation of coordinates
    #             if outer + middle + inner != n: #test sum of coordinates so that they are not equal to test number
    #                 output.append([outer, middle, inner]) #append subarray to output array
    
    # print(output) #print output array

    # List Comprehension example for understanding of desired output

    #1) define multiple variables
    #2) create for loops with these iterable variables using ranges of coordinates plus 1 for <= conditional
    #3) utilize if statement to check conditional for comprehension case
    #4) wrap within print statement so coordinates are printed within an array inside of comprehension array
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i+j+k != n])
