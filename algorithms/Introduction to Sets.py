def average(array):
    height_sum = 0.0 #initialize height_sum var to explicit float val
    arr_set = set(array) #parse array input as a set, removing duplicate data
    
    for height in arr_set: #open for in loop within arr_set
        height_sum += height #add each element of the set to the height_sum variable
    
    output = height_sum / (len(arr_set)) #divide height_sum by the length of the set, place value into output variable
    
    return round(output, 3) #return the rounded value of output, rounding to the third decimal place
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)