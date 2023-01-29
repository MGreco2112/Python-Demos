def diagonalDifference(arr):
    leftSum = 0
    rightSum = 0
    
    pointer = 0
    revPointer = len(arr) - 1
    
    for index in range(len(arr)):
        leftSum += arr[index][pointer]
        rightSum += arr[index][revPointer]
        
        pointer += 1
        revPointer -= 1
            
    
    return abs(leftSum - rightSum)
