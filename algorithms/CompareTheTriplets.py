def compareTriplets(a, b):
    output = [0, 0]
    
    for score in range(len(a)):
        if (a[score] > b[score]):
            output[0] = output[0] + 1
        elif (a[score] < b[score]):
            output[1] = output[1] + 1
    
    return output
